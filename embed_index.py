import os
import glob
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

ES_URL = "http://localhost:9200"
INDEX_NAME = "demo_index"

CHUNK_SIZE = 1
MODEL_NAME = "all-MiniLM-L6-v2"  # outputs 384-dim embeddings

# Chunking sentences
def chunk_sentences(text, chunk_size=1, overlap=0):
    sentences = sent_tokenize(text)
    chunks = []

    i = 0
    while i < len(sentences):
        chunk = sentences[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap if chunk_size - overlap > 0 else 1

    return chunks


# Connect to ElasticSearch
print("Connecting to ElasticSearch")
es = Elasticsearch(ES_URL)
print("Connected!")

# Check connection
if not es.ping():
    print("Elasticsearch is not running!")
    exit()

# Create index if it doesn't exist
print("Checking index")
if not es.indices.exists(index=INDEX_NAME):
    print("Index does not exist, creating...")
    es.indices.create(
        index=INDEX_NAME,
        body={
            "mappings": {
                "properties": {
                    "filename": {"type": "keyword"},
                    "chunk_number":{"type":"integer"},
                    "chunk_text": {"type": "text"},
                    "embedding": {"type": "dense_vector", "dims": 384}
                }
            }
        }   
    )
    print(f"Created index: {INDEX_NAME}")
else:
    print("Index already exists")

print("Loading embedding model")
# Load embedding model
model = SentenceTransformer(MODEL_NAME)
print("Model loaded")

# Get all text files in your docs folder
files = glob.glob("docs/*.txt")
print(f"Found {len(files)} files")

for filepath in files:
    print(f"Processing {filepath}...")
    filename = os.path.basename(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_sentences(
        text, 
        chunk_size=CHUNK_SIZE,
        overlap=0
    )
    print(f"Found {len(chunks)} chunks")

    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()

        doc = {
            "filename": filename,
            "chunk_number": i,
            "chunk_text": chunk,
            "embedding": embedding
        }

        es.index(index=INDEX_NAME, body=doc)

    print(f"Indexed file: {filename}")

print("All documents indexed!")
