
lambda   

import boto3
import json

ses = boto3.client("ses")

def lambda_handler(event, context):
    print("EVENT RECEIVED FROM BEDROCK:")
    print(json.dumps(event))

    # Extract parameters
    params = event.get("parameters", [])
    email = None
    message = None

    for p in params:
        if p["name"].lower() == "email":
            email = p["value"]
        if p["name"].lower() == "message":
            message = p["value"]

    # Validate parameters
    if not email or not message:
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get("actionGroup"),
                "function": event.get("function"),
                "functionResponse": {
                    "output": {
                        "email_status": "Missing email or message parameter",
                        "message_sent": False
                    }
                }
            }
        }

    try:
        # Send email using SES
        ses.send_email(
            Source="jaswanthmatta344@gmail.com",  # YOUR VERIFIED SES EMAIL
            Destination={"ToAddresses": [email]},
            Message={
                "Subject": {"Data": "Your Requested Information"},
                "Body": {"Text": {"Data": message}}
            }
        )

        # Return SUCCESS
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get("actionGroup"),
                "function": event.get("function"),
                "functionResponse": {
                    "output": {
                        "email_status": f"Email sent successfully to {email}",
                        "message_sent": True
                    }
                }
            }
        }

    except Exception as e:
        # Return FAILURE
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": event.get("actionGroup"),
                "function": event.get("function"),
                "functionResponse": {
                    "output": {
                        "email_status": f"Failed to send email: {str(e)}",
                        "message_sent": False
                    }
                }
            }
        }
