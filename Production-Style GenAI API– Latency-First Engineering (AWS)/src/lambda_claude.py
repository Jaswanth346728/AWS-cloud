import json
import time
import boto3

# Bedrock client initialized outside handler
bedrock = boto3.client("bedrock-runtime")

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

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
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 50,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        )

        after_bedrock = time.time()

        response_body = json.loads(response["body"].read())
        output_text = response_body["content"][0]["text"]

        total_time = time.time() - start_time

        print(f"Bedrock inference time: {(after_bedrock - before_bedrock) * 1000:.2f} ms")
        print(f"Total Lambda execution time: {total_time * 1000:.2f} ms")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "model": "Claude 3 Haiku",
                "response": output_text,
                "total_execution_ms": round(total_time * 1000, 2)
            })
        }

    except Exception as e:
        print("Error invoking Bedrock:", str(e))
        raise e
