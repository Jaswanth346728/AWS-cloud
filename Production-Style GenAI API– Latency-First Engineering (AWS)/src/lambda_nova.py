import json
import time
import boto3

# Bedrock client initialized outside handler
bedrock = boto3.client("bedrock-runtime")

MODEL_ID = "amazon.nova-lite-v1:0"

def lambda_handler(event, context):
    start_time = time.time()
    print("Request received")

    prompt = "Explain what cloud latency means in one sentence."

    try:
        before_bedrock = time.time()

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ]
            })
        )

        after_bedrock = time.time()

        response_body = json.loads(response["body"].read())
        output_text = response_body["output"]["message"]["content"][0]["text"]

        total_time = time.time() - start_time

        print("RAW BEDROCK RESPONSE:", json.dumps(response_body))
        print(f"Bedrock inference time: {(after_bedrock - before_bedrock) * 1000:.2f} ms")
        print(f"Total Lambda execution time: {total_time * 1000:.2f} ms")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "model": "Amazon Nova Lite",
                "response": output_text,
                "total_execution_ms": round(total_time * 1000, 2)
            })
        }

    except Exception as e:
        print("Error invoking Bedrock:", str(e))
        raise e
