import json
import boto3
import os
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

def lambda_handler(event, context):
    try:
        # --- STEP 1: Parse Input Event ---
        query = None
        
        if 'Records' in event:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'S3 trigger not supported for query'})
            }
        elif 'body' in event:
            body = json.loads(event['body'])
            query = body.get('query')
        elif 'query' in event:
            query = event['query']
        elif 'question' in event:
            query = event['question']
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No query found in event'})
            }
        
        if not query:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Query is empty'})
            }
        
        # --- STEP 2: Get Environment Variables ---
        opensearch_endpoint = os.environ['OPENSEARCH_ENDPOINT']
        opensearch_index = os.environ['OPENSEARCH_INDEX']
        embed_model_id = os.environ['EMBED_MODEL_ID']
        gen_model_id = os.environ['GEN_MODEL_ID']
        bedrock_region = os.environ['BEDROCK_REGION']
        
        # --- STEP 3: Initialize AWS Services ---
        session = boto3.Session()
        credentials = session.get_credentials()
        awsauth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            'us-east-1',
            'aoss',
            session_token=credentials.token
        )
        
        opensearch_client = OpenSearch(
            hosts=[{'host': opensearch_endpoint, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            pool_maxsize=20
        )
        
        bedrock = boto3.client('bedrock-runtime', region_name=bedrock_region)
        
        # --- STEP 4: Generate Query Embedding ---
        embed_request = {
            "inputText": query,
            "dimensions": 1024,
            "normalize": True
        }
        
        embed_response = bedrock.invoke_model(
            modelId=embed_model_id,
            body=json.dumps(embed_request)
        )
        
        embed_output = json.loads(embed_response["body"].read())
        query_embedding = embed_output["embedding"]
        
        # --- STEP 5: Search OpenSearch ---
        search_query = {
            "size": 5,
            "query": {
                "knn": {
                    "vector_field": {    # ← CORRECT FIELD NAME
                        "vector": query_embedding,
                        "k": 5
                    }
                }
            },
            "_source": ["content", "source"]
        }
        
        search_response = opensearch_client.search(
            index=opensearch_index,
            body=search_query
        )
        
        retrieved_docs = []
        for hit in search_response['hits']['hits']:
            retrieved_docs.append({
                'content': hit['_source']['content'],
                'source': hit['_source'].get('source', 'Unknown'),
                'score': hit['_score']
            })
        
        # --- STEP 6: Generate Answer with Amazon Titan ---
        if retrieved_docs:
            context = "\n\n".join([doc['content'] for doc in retrieved_docs])
            prompt = f"""Based on the following context, answer the question: {query}

Context:
{context}

Answer:"""
        else:
            prompt = f"Answer the following question: {query}"
        
        llm_request = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 500,
                "temperature": 0.7,
                "topP": 0.9,
                "stopSequences": []
            }
        }
        
        llm_response = bedrock.invoke_model(
            modelId=gen_model_id,
            body=json.dumps(llm_request)
        )
        
        llm_output = json.loads(llm_response["body"].read())
        generated_answer = llm_output["results"][0]["outputText"]
        
        # --- STEP 7: Return Response ---
        return {
            'statusCode': 200,
            'body': json.dumps({
                'query': query,
                'retrieved_documents': [doc['content'] for doc in retrieved_docs],
                'generated_answer': generated_answer.strip(),
                'context_used': len(retrieved_docs) > 0,
                'num_docs_found': len(retrieved_docs)
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


