import random
import json

def generate_sparse_vector(vocab_size=5000, max_tokens=10):
    return {
        str(random.randint(1, vocab_size)): round(random.uniform(0.1, 1.0), 3)
        for _ in range(random.randint(3, max_tokens))
    }

def vector_to_spring(vocab_size=5000,max_token=10):
    return {
        str(random.randint(1,vocab_size)):round(random.uniform(0.1,1.0),3)
        for _ in range(random.randint)
    }
def vector_to_string(vector_dict):
    return " ".join([])
titles = [
    "ancient ruins discovered",
    "new vaccine trial successful",
    "local team wins championship",
    "meteor shower lights up sky",
    "economic report shows growth",
    "rare bird spotted in city",
    "tech startup raises funding",
    "climate summit begins today",
    "artist opens new exhibit",
    "archaeologists find burial site"
]

docs = []
for i, title in enumerate(titles):
    doc = {
        "id": i,
        "title": title,
        "sparse_vector": generate_sparse_vector()
    }
    docs.append(doc)

# output the json
with open("mock_sparse_data.json", "w") as f:
    json.dump(docs, f, indent=2)

print(docs[:2])  # preview
