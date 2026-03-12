from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

res = es.search(index="my-sparse-index", size=10)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
