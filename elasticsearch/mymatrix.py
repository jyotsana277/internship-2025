import numpy as np
from scipy.sparse import coo_matrix

data = []
rows = []
cols = []

with open("mockdata.mtx") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 3:
            continue
        i, j, v = parts
        rows.append(int(i))
        cols.append(int(j))
        data.append(float(v))

shape = (max(rows)+1, max(cols)+1)
A = coo_matrix((data, (rows, cols)), shape=shape)

for i in range(A.shape[0]):
    row = A.getrow(i)

    # get indices and values for nonzero entries
    indices = row.indices
    values = row.data

    # convert to dict with string keys for JSON
    sparse_vector = {
        str(idx): float(val) for idx, val in zip(indices, values)
    }

    # build document
    doc = {
        "row_id": i,
        "sparse_vector": sparse_vector
    }

    print(doc)
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://localhost:9200")

actions = []

for i in range(A.shape[0]):
    row = A.getrow(i)
    indices = row.indices
    values = row.data

    sparse_vector = {
        str(idx): float(val) for idx, val in zip(indices, values)
    }

    doc = {
        "row_id": i,
        "sparse_vector": sparse_vector
    }

    action = {
        "_index": "my-sparse-index",
        "_id": i,
        "_source": doc
    }

    actions.append(action)

helpers.bulk(es, actions)

print("Upload complete!")

