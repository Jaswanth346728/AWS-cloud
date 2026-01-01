# Production-Style GenAI API — Latency-First Engineering on AWS

This project focuses on **measuring, understanding, and reducing latency** in a serverless Generative AI API built on AWS.  
Rather than treating latency as a side effect, the system is designed and evaluated using a **latency-first engineering mindset**, with particular emphasis on **p50, p95, and p99 behavior**.

The work intentionally avoids overengineering and instead demonstrates how **measured observations** can guide effective optimization decisions in real-world cloud systems.

---

## Architecture Overview

The architecture is intentionally minimal to isolate latency behavior and avoid confounding variables.

Client → API Gateway → AWS Lambda → Amazon Bedrock → Lambda → Client


### Services Used
- **Amazon API Gateway** – Public HTTP endpoint
- **AWS Lambda (Python)** – Request orchestration and timing instrumentation
- **Amazon Bedrock** – Foundation model inference
- **Amazon CloudWatch** – Logs, metrics, dashboards, and latency analysis

No databases, queues, caching layers, or orchestration services were introduced to keep the experiment controlled and interpretable.

---

## Problem Statement

Initial testing revealed **high tail latency (p95 / p99)** even at low request volume.  
The core questions this project aimed to answer were:

- Where does latency actually originate in a serverless GenAI system?
- Is latency dominated by cold starts, runtime overhead, or model inference?
- Can meaningful improvements be achieved **without adding infrastructure**?

---

## Measurement Strategy

Latency was measured directly inside the Lambda function using precise timestamps:

- **Bedrock inference time**
- **Total Lambda execution time**
- **Cold start (Init Duration) vs warm execution**

Requests were generated using repeated API calls to observe latency distribution rather than relying on single measurements.

CloudWatch Logs and Dashboards were used to validate:
- Median latency (p50)
- Tail latency (p95 / p99)
- Cold start impact on extreme outliers

---

## Key Finding: Inference Dominance

Analysis showed that:

- Model inference accounted for **~95–99% of total Lambda execution time**
- Non-inference overhead (runtime initialization, JSON parsing, logging) was negligible
- Optimizing Lambda memory or code paths would not materially reduce latency

**Conclusion:**  
Latency optimization had to target **foundation model inference**, not infrastructure.

---

## Optimization Performed

A single, controlled change was introduced:

- **Baseline model:** Claude 3 Haiku  
- **Optimized model:** Amazon Nova Lite  

All other variables were kept constant:
- Same prompt
- Same Lambda configuration
- Same API Gateway endpoint
- Same request pattern

This ensured the comparison reflected **inference behavior only**.

---

## Results

After switching to Amazon Nova Lite:

- **p95 latency reduced by approximately 50%**
- Median latency improved significantly
- Tail latency distribution tightened
- Lambda billed duration decreased
- Per-request cost dropped as a consequence of faster execution

Cold start overhead remained, but its overall impact on end-to-end latency was reduced due to faster inference.

---

## Reliability and Failure Implications

Reducing execution time improved system reliability by:

- Increasing margin before API Gateway and Lambda timeouts
- Lowering risk of tail-latency amplification under burst traffic
- Reducing the likelihood of retries and cascading slowdowns

No synthetic fault injection was performed; instead, reliability improvements were achieved by **shrinking the latency surface area**.

---

## Scope and Limitations

This project intentionally did **not** include:

- Retries or backoff logic
- Caching layers
- Asynchronous processing
- Load testing at high concurrency

The goal was to demonstrate **measured latency optimization**, not to build a full production platform.

---

## Key Takeaway

Latency problems cannot be solved by assumptions.

By instrumenting real execution paths, identifying the dominant bottleneck, and applying a minimal optimization, the system achieved meaningful improvements in **latency, cost, and reliability** without architectural complexity.
