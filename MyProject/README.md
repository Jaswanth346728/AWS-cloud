# Smart Service AI Assistant  
### Built with Amazon Bedrock • Knowledge Base • OpenSearch Serverless • Lambda • SES

This project is an intelligent **AI-driven service assistant** designed to understand natural language requests and execute real-world actions using a fully serverless AWS architecture. It can find food deals, restaurant offers, shopping discounts, electronic product suggestions, and send results directly to the user’s email.

The system integrates a **Bedrock Knowledge Base** connected to **OpenSearch Serverless**, enabling fast retrieval of unstructured text through vector embeddings. The agent produces clean, human-like responses using Generative AI, without citations or technical metadata.

When a user requests, “send this to my email,” the **Bedrock Agent** triggers an action group function (`sendEmail`) that invokes an **AWS Lambda** backend. Lambda formats the message and delivers it securely using **Amazon SES**.

---

##  Key Features
- **Natural Language Understanding** using Amazon Bedrock  
- **RAG-powered Knowledge Base** with OpenSearch Serverless  
- **Custom Action Group Execution** through Bedrock Agents  
- **Serverless Backend** using AWS Lambda  
- **Automated Email Delivery** via Amazon SES  
- **Clean, citation-free AI responses**  
- **Vector Search & Retrieval** for unstructured deal and offer data  
- **End-to-end automated workflow**

---

##  What This Project Demonstrates
- Building **agentic AI systems** using Bedrock Agents  
- Integrating **Knowledge Base + Vector Search** for retrieval  
- Executing business logic with **Lambda Action Groups**  
- Sending dynamic content using **Amazon SES**  
- Structuring and retrieving unstructured data using RAG  
- Combining Generative AI with serverless services for real applications  

---

##  Technologies Used
- **Amazon Bedrock (Agents + Knowledge Bases)**  
- **Amazon OpenSearch Serverless**  
- **Amazon Lambda**  
- **Amazon SES**  
- **Amazon S3**  
- **Python (Lambda backend)**  

---

##  Project Summary  
This AI Assistant is capable of:

- Finding **food offers**, discounts, and restaurant deals  
- Recommending **shopping and clothing offers**  
- Suggesting **electronic items** based on user queries  
- Sending all results directly to user email via SES  
- Retrieving info from a Knowledge Base using **RAG**  
- Generating natural, user-friendly responses  
- Working as a **plug-and-play AI Agent** for any application  

With additional **fine-tuning** or expanded **RAG datasets**, this AI assistant can be integrated into any web or mobile application to provide smarter, more personalized customer interactions.

---

##  Real-World Use Cases
- Food delivery apps  
- Shopping & deal finder apps  
- Customer support AI  
- E-commerce recommendation engines  
- Personal assistant tools  
- Email-based notification systems  

---

##  Final Notes  
This project showcases the power of combining **Generative AI**, **RAG**, and **AWS Serverless** to build a fully automated, intelligent digital assistant that can retrieve information, summarize it naturally, and perform real-world actions for users.

