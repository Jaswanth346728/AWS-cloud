# Analyzing Network Traffic with VPC Flow Logs & Network ACLs  
*A practical AWS security project for detecting and blocking suspicious IP traffic*

---

##  Overview

This project demonstrates how to analyze network traffic in an Amazon VPC using **VPC Flow Logs**, identify suspicious public IP addresses, and block them using **Network ACLs (NACLs)**.  
The workflow mirrors real-world security operations used by Cloud Engineers and Security Analysts to protect workloads from unauthorized inbound traffic.

Through this implementation, I learned how to:

- Capture VPC and Subnet network traffic using Flow Logs  
- Store and analyze log data in Amazon S3  
- Identify external public IP addresses communicating with EC2 instances  
- Block specific malicious or unknown IPs with Network ACLs  
- Validate block actions through **REJECT** entries in subnet Flow Logs  

---

##  What I Built (Step-by-Step)

### 1. Created an Amazon S3 Bucket  
Configured an S3 bucket to store all VPC and subnet flow log files.

---

### 2. Enabled VPC Flow Logs (Accepted Traffic Only)  
- Opened the VPC console  
- Created a **VPC-level Flow Log**  
- Selected **ACCEPT** traffic  
- Set S3 as the destination  

This allowed monitoring of all traffic that successfully reached the EC2 instance.

---

### 3. Analyzed S3 Logs to Identify Public IPs  
Downloaded the flow log file from S3 and analyzed the entries.  
From the logs, I identified a suspicious external IP:

###  Suspicious IP Identified
54.210.225.137

This IP was unexpectedly connecting to the instance.

---

### 4. Blocked the IP Using a Network ACL  
Added an inbound **DENY rule** in the NACL:

54.210.225.137/32

- `/32` blocks exactly one IP  
- Applied at the subnet level  
- Prevents unwanted traffic before it reaches the instance  

---

### 5. Created Subnet Flow Logs (Rejected Traffic)  
To validate the rule:

- Created subnet-level Flow Logs  
- Set to record **REJECT** traffic  
- Sent logs to the same S3 bucket  

---

### 6. Verified the Block in Flow Logs  
Checked the new S3 log file and confirmed the IP was rejected:

54.210.225.137 ... REJECT OK


This confirmed that NACL blocking was working successfully.

---

##  Key Security Concepts Demonstrated

- VPC Flow Log analysis  
- Public vs private IP identification  
- Detecting unauthorized IP traffic  
- Network ACL deny rule configuration  
- Observing REJECT traffic in Flow Logs  
- Reducing unnecessary inbound traffic for cost efficiency  

---

##  AWS Services Used

- **Amazon VPC**  
- **Subnets**  
- **Network ACL**  
- **VPC Flow Logs**  
- **Amazon S3**  
- **EC2**

---


##  Summary

By creating flow logs, reviewing S3 log files, blocking the IP using a NACL, and verifying reject traffic at the subnet level, this project provided full end-to-end experience in **AWS networking, monitoring, and security operations**.


