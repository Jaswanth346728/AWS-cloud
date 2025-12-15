import json
import boto3
import urllib.parse
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")

    # Clients
    s3_client = boto3.client('s3')
    bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # OpenSearch
    opensearch_host = "jsccflonxnfp0qvn2tea.us-east-1.aoss.amazonaws.com"
    opensearch_index = "rag-index"

    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, "us-east-1", "aoss")

    opensearch_client = OpenSearch(
        hosts=[{"host": opensearch_host, "port": 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    try:
        for record in event["Records"]:
            bucket = record["s3"]["bucket"]["name"]
            key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
            print(f"Processing file: {key}")

            # Read file
            response = s3_client.get_object(Bucket=bucket, Key=key)
            text = response["Body"].read().decode("utf-8")

            chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
            if not chunks:
                chunks = [text]

            for i, chunk in enumerate(chunks, 1):
                print(f"\n===== CHUNK {i} =====")
                print(chunk[:200])

                # ---- Bedrock embedding request ----
                embed_request = {"inputText": chunk}

                bedrock_response = bedrock_client.invoke_model(
                    modelId="amazon.titan-embed-text-v2:0",
                    body=json.dumps(embed_request),
                    contentType="application/json"
                )

                body = json.loads(bedrock_response["body"].read())
                print("Bedrock Full Response:", body)

                embedding = body.get("embedding")

                # ---- Check for errors ----
                if embedding is None:
                    print(" ERROR: EMBEDDING IS NULL — SKIPPING THIS CHUNK")
                    continue

                print(f" Embedding length: {len(embedding)}")

                # ---- Create document for OpenSearch ----
                doc = {
                    "content": chunk,
                    "vector_field": embedding,
                    "source_file": key,
                    "chunk_id": i,
                    "timestamp": context.aws_request_id
                }

                # ---- Index into OpenSearch ----
                resp = opensearch_client.index(
                    index=opensearch_index,
                    body=doc
                )

                print(f"Indexed chunk {i} → doc ID {resp['_id']}")

        return {"statusCode": 200, "body": "Success"}

    except Exception as e:
        print(" ERROR:", str(e))
        raise e

