# AWS Content Delivery Network (CDN) Lab

This project demonstrates how to decrease application latency by deploying a global Content Delivery Network (CDN) using Amazon CloudFront. The lab involves configuring CloudFront with two different origins—an Amazon EC2 instance and an Amazon S3 static website—to understand how CDN caching improves performance for users across multiple geographic locations.

---

## Objectives
- Deploy a CloudFront distribution to deliver content with low latency.
- Configure an EC2 instance as the origin for a CloudFront distribution.
- Configure an Amazon S3 static website as the origin for a CloudFront distribution.
- Reconfigure CloudFront to switch between origins.
- Validate latency improvement achieved through edge locations.

---

## Architecture Overview
CloudFront delivers cached content to global users from the nearest edge location. In this lab, two architectures were implemented:

1. **CloudFront → EC2 Origin**
2. **CloudFront → S3 Static Website Origin**

This setup demonstrates how CloudFront reduces load on the origin and improves response time.

---

## Steps Performed

### 1. Configure CloudFront with EC2 as the Origin
- Launched an EC2 instance running a basic web server.
- Retrieved the public DNS endpoint of the EC2 instance.
- Created a CloudFront distribution and set the EC2 public DNS as the origin.
- Validated content delivery through the CloudFront distribution domain.

### 2. Configure CloudFront with S3 Static Website as the Origin
- Created an S3 bucket for static hosting.
- Enabled “Static Website Hosting” and uploaded `index.html`.
- Obtained the S3 website endpoint.
- Updated the CloudFront distribution to replace the EC2 origin with the S3 website endpoint.
- Set `index.html` as the default root object.
- Verified content delivery and edge caching through the CloudFront domain.

---

## Key Learnings
- CloudFront reduces latency by serving cached content from edge locations.
- Switching origins in CloudFront allows seamless migration from compute-based hosting (EC2) to serverless hosting (S3).
- S3 as an origin provides cost efficiency and scalability.
- Understanding how CDN caching works is essential for building high-performance web applications.

---

## Technologies Used
- Amazon CloudFront
- Amazon EC2
- Amazon S3 (Static Website Hosting)
- AWS Global Edge Network

---

## Outcome
Successfully deployed and tested a global content delivery network using CloudFront. Verified that CloudFront fetches content from the nearest edge location and provides faster delivery compared to accessing the origin directly. Gained practical experience in configuring CloudFront distributions with multiple origins and optimizing content delivery performance.

