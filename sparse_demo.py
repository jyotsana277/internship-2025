from elasticsearch import Elasticsearch

ES_URL = "http://localhost:9200"
INDEX_NAME = "demo_index"

es = Elasticsearch(ES_URL)

while True:
    query_text = input("Enter your search query (or type 'exit' to quit): ").strip()
    
    if query_text.lower() == "exit":
        print("Demo Terminated.")
        break

    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "match": {
                    "chunk_text": query_text
                }
            }
        }
    )

    hits = response["hits"]["hits"]
    
    print(f"\nFound {len(hits)} results:\n")

    for hit in hits:
        score = hit["_score"]
        filename = hit["_source"]["filename"]
        chunk_text = hit["_source"]["chunk_text"]

        print(f"Score: {score:.2f}")
        print(f"File: {filename}")
        print(f"Chunk: {chunk_text}")
        print("-" * 50)

    print()
