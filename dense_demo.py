from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

ES_URL = "http://localhost:9200"
INDEX_NAME = "demo_index"
MODEL_NAME = "all-MiniLM-L6-v2"

# connect to elasticsearch
es = Elasticsearch(ES_URL)
if not es.ping():
    print("ElasticSearch is not running!")
    exit()

# load the embedding model
model = SentenceTransformer(MODEL_NAME)

# get query from user
user_query = input("Enter your query: ")

# generate embedding
query_vector = model.encode(user_query).tolist()

# define the search query
query_body = {
    "size": 5,
    "query": {
        "script_score": {
            "query": {
                "match_all": {}
            },
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",  # +1.0 to avoid negative scores
                "params": {
                    "query_vector": query_vector
                }
            }
        }
    }
}

# perform the search
response = es.search(index=INDEX_NAME, body=query_body)

# print results
print("\nTop Results:\n")
for hit in response["hits"]["hits"]:
    print(f"[Score: {hit['_score']:.4f}] {hit['_source']['chunk_text'][:200]}...\n")
