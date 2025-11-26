# Serverless Single-Page Application on AWS

This project demonstrates how I deployed a serverless single-page application using Amazon S3, Amazon API Gateway, AWS Lambda, and DynamoDB. The frontend is hosted on S3, and the backend is built using Lambda functions connected through API Gateway. CloudWatch Logs were used to troubleshoot and fix backend permission issues.

## What I Did

### 1. S3 Static Website Hosting
- Created an S3 bucket and enabled static website hosting.
- Enabled public access and uploaded the frontend files.

### 2. API Gateway Endpoints
- Built a GET `/vehicles` endpoint to return all vehicle records.
- Built a GET `/vehicle/{id}` endpoint to return details for a specific vehicle.
- Integrated both endpoints with Lambda using Lambda Proxy Integration.

### 3. Lambda + DynamoDB Integration
- `find_all_vehicles` Lambda function performs a DynamoDB Scan.
- `find_vehicle` Lambda function performs a GetItem by ID.
- Returned JSON responses to the frontend.

### 4. CloudWatch Troubleshooting
- Initial API calls failed.
- CloudWatch Logs showed `AccessDeniedException` for DynamoDB.
- Updated the Lambda execution role with required DynamoDB permissions (`Scan` and `GetItem`).
- API responses worked successfully after permissions were corrected.

## Architecture Summary
S3 (Frontend)
→ API Gateway
→ Lambda Functions
→ DynamoDB (vehicles table)
→ CloudWatch Logs for monitoring and debugging

## Skills Demonstrated
- S3 static hosting  
- API Gateway REST API design  
- Lambda function development  
- DynamoDB data access patterns  
- IAM role and permission debugging  
- CloudWatch-based troubleshooting  
- Serverless application design  

## Why This Project Matters
This project reflects a common serverless architecture used in real production environments. It shows hands-on experience in building APIs, connecting serverless components, fixing IAM issues, and deploying cloud applications on AWS.
