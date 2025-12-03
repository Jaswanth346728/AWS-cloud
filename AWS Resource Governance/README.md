#  AWS Resource Governance — Enforcing Compliance With AWS Config

This project demonstrates how AWS Config can be used to monitor, evaluate, and enforce compliance across AWS resources.  
The goal is to ensure that S3 buckets and other resources follow best practices such as encryption, tagging, and versioning.

All evaluations were validated in the AWS Config dashboard, and all configured rules reached a **Compliant** state.

---

##  What I Implemented

### **1. Enabled AWS Config**
- Set up AWS Config in the region  
- Selected an S3 bucket to store configuration snapshots  
- Used the default service-linked role for AWS Config  
- Confirmed that the configuration recorder and delivery channel were active

---

### **2. Applied Managed AWS Config Rules**

####  S3 Default Encryption
Rule: **`s3-default-encryption-kms`**  
- Ensures all S3 buckets use KMS encryption  
- Helps enforce data protection standards

####  Required Tags  
Rule: **`required-tags`**  
- Verifies that resources include mandatory tags  
- Helps maintain resource ownership, cost tracking, and governance

####  S3 Bucket Versioning  
Rule: **`s3-bucket-versioning-enabled`**  
- Ensures versioning is turned on for S3 buckets  
- Helps protect against unintended overwrites or deletions

---

### **3. Compliance Validation**
- Evaluated resources using AWS Config  
- Verified rule status in the **Rules** section  
- Monitored compliance metrics in the **Dashboard**  
- Ensured all rules reached “**Compliant**” status  
- Enabled versioning on the required bucket to pass validation  
- Confirmed clean compliance in both:
  - Rule list  
  - Dashboard overview  

---

##  AWS Services Used
- **AWS Config**  
- **Amazon S3**  
- **AWS IAM**  
- **AWS Management Console**

---

##  Key Learnings
- How AWS Config continuously monitors configurations  
- Setting up and customizing managed Config rules  
- Enforcing encryption, versioning, and tagging standards  
- Interpreting compliance results via the Config dashboard  
- Improving cloud governance and operational consistency  

---

