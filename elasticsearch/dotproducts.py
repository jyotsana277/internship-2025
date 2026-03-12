from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

res = es.search(index="my-sparse-index", size=10)

def dot_product(v1, v2):
    return sum(v1[k] * v2.get(k, 0) for k in v1)

query_vector = {'0': 3.5, '3': 1.0}

for hit in res["hits"]["hits"]:
    doc = hit["_source"]
    vec = doc.get("my_sparse_vector") or doc.get("sparse_vector")
    if vec:
        score = dot_product(query_vector, vec)
        print(f"Doc: {doc} → Score: {score}")
