#  Data Ingestion Methods - Real-Time Streaming Pipeline on AWS

This project implements a complete real-time data ingestion and analytics pipeline using several AWS services, including **Amazon Kinesis Data Firehose**, **AWS Lambda**, **Amazon S3**, **AWS Glue**, and **Amazon Athena**.  
The goal of the project is to demonstrate how clickstream data can be ingested, transformed, stored, and queried at scale using fully managed AWS data services.

---


##  What I Implemented

### **1. Real-Time Ingestion With Amazon Data Firehose**
- Created a Kinesis Data Firehose delivery stream  
- Configured IAM roles for Firehose to access S3 and Lambda  
- Set appropriate buffering and delivery settings  
- Integrated Firehose with downstream services  

---

### **2. Clickstream Data Storage in Amazon S3**
- Delivered ingested events into an Amazon S3 bucket  
- Organized storage with prefixes for easier processing  
- Verified that Firehose delivery was working in real time  

---

### **3. Data Transformation Using AWS Lambda**
- Built a Lambda function to preprocess incoming events  
- Connected Lambda as a transformation step within Firehose  
- Ensured transformed data was delivered correctly to S3  
- Added DynamoDB integration to store processed analytics results  

---

### **4. Data Cataloging With AWS Glue**
- Configured a Glue Crawler to map S3 data  
- Automatically generated a table schema  
- Prepared the data for SQL-based analytics  

---

### **5. Interactive Querying With Amazon Athena**
- Connected Athena to the Glue Data Catalog  
- Wrote SQL queries to analyze ingested clickstream data  
- Validated transformation accuracy and data organization  

---

##  AWS Services Used

- Amazon Kinesis Data Firehose  
- AWS Lambda  
- Amazon S3  
- AWS Glue  
- Amazon Athena  
- Amazon DynamoDB  
- AWS IAM  

---

##  Key Learnings

- Designing and deploying real-time ingestion pipelines  
- Transforming streaming data using Lambda functions  
- Building data lakes with S3 + Glue + Athena  
- Managing buffering, delivery frequency, and transformation steps  
- Storing analytical insights in DynamoDB  
- Understanding how AWS services connect in end-to-end data workflows  

---

