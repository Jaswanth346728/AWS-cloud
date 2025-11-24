# Connecting Multiple VPCs Using VPC Peering 

In this project, I configured VPC Peering between three different VPCs to enable secure communication across isolated networks. This lab helped me understand how routing, CIDR blocks, and network permissions work together in AWS networking.

The goal was to allow the **Marketing VPC** and **Developer VPC** to securely access the **Finance VPC** by creating peering connections and updating routing rules.

---

## Overview

I worked with three VPCs:

- **Marketing VPC** – 10.10.0.0/16  
- **Finance VPC** – 172.31.0.0/16  
- **Developer VPC** – 192.168.0.0/20  

The task was to set up VPC peering and ensure each VPC could route traffic correctly to the Finance VPC.

---

## Steps I Completed

### **1. Created a VPC Peering Connection (Marketing → Finance)**
- Started a new peering request from **Marketing VPC** to **Finance VPC**.
- Logged into the **Finance VPC** side and **accepted** the peering request.
- Updated the **route tables** in both VPCs to include each other's CIDR ranges.

### **2. Updated Security Group Rules**
- Modified the **Finance VPC security group inbound rules** to allow traffic from the **Marketing VPC CIDR range**.
- This ensured that even if routing was correct, the traffic would not be blocked by SG rules.

### **3. Created Another Peering Connection (Developer → Finance)**
- Initiated and accepted a new peering request between **Developer VPC** and **Finance VPC**.
- Added routes in both VPC route tables to allow communication.
- Updated inbound rules in the Finance VPC to allow Developer VPC traffic.

### **4. Validated VPC-to-VPC Communication**
- Ensured that both Marketing and Developer servers could reach the Finance server through private IPs.
- Confirmed routing and security were correctly configured.

---

## Architecture Summary

The final setup included:

- **Two VPC Peering Connections**  
  - Marketing ↔ Finance  
  - Developer ↔ Finance  
- **Updated Route Tables** in all VPCs  
- **Correct Security Group & Inbound Rules**  
- **Fully working private communication** between VPCs  

This is the same pattern used in real AWS environments for connecting department-based VPCs, multi-account networks, and microservice communication.

---

## What I Learned

- How VPC Peering works internally  
- How to update route tables with CIDR blocks  
- How security groups and routing work together  
- How to design secure cross-VPC communication  
- How to validate networking paths in AWS  

---

## Technologies Used

- **Amazon VPC**
- **VPC Peering**
- **Route Tables**
- **Security Groups / NACLs**
- **EC2 Instances**
- **AWS Console**

---



