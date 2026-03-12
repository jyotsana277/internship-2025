from elasticsearch import Elasticsearch, helpers
import json

# connect to elasticsearch
es = Elasticsearch("http://localhost:9200")

# read your json file
with open("mock_sparse_data.json", "r") as f:
    docs = json.load(f)

# prepare bulk actions
actions = []
for doc in docs:
    action = {
        "_index": "my-sparse-index",
        "_id": doc["id"],
        "_source": {
            "text": doc["title"],
            "my_sparse_vector": doc["sparse_vector"]
        }
    }
    actions.append(action)


# bulk upload
helpers.bulk(es, actions)

print("Uploaded all docs from file!")
