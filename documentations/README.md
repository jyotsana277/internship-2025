# RAG Search Demo

A mini semantic search engine over AI/ML topic documents, demonstrating the difference between **keyword search** and **vector (semantic) search** using Elasticsearch and sentence embeddings.

---

## What It Does

This project indexes a collection of short educational documents about AI topics and lets you search through them in two ways:

- **Sparse search** — traditional keyword/BM25 matching
- **Dense search** — semantic vector search using sentence embeddings

---

## Project Structure

```
demo/
├── docs/               # Knowledge base (.txt files)
│   ├── rag.txt
│   ├── nlp.txt
│   ├── nlu.txt
│   ├── nlg.txt
│   ├── ml.txt
│   ├── dl.txt
│   ├── es.txt
│   ├── vecdb.txt
│   ├── chatbot.txt
│   └── convAI.txt
│
├── embed_index.py      # Chunks + embeds docs and indexes them into Elasticsearch
├── sparse_demo.py      # Keyword search (BM25)
├── dense_demo.py       # Semantic search (cosine similarity)
├── hybrid.py           # (Coming soon) Combined sparse + dense search
├── mockchunker.py      # Utility to test sentence chunking logic
└── requirements.txt    # Python dependencies
```

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Elasticsearch

Make sure Elasticsearch is running locally on port `9200`. You can use Docker:

```bash
docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.x
```

### 3. Index the documents

Run this once to chunk, embed, and upload all docs to Elasticsearch:

```bash
python embed_index.py
```

This will:
- Split each `.txt` file in `docs/` into sentence-level chunks
- Generate 384-dimensional embeddings using `all-MiniLM-L6-v2`
- Store both the text and embeddings in an index called `demo_index`

---

## Running the Search Demos

### Keyword Search (Sparse)

```bash
python sparse_demo.py
```

Uses Elasticsearch's built-in BM25 `match` query. Good for exact keyword matches.

### Semantic Search (Dense)

```bash
python dense_demo.py
```

Encodes your query into a vector and retrieves the most semantically similar chunks using cosine similarity — finds relevant results even when exact words don't match.

---

## Models Used

| Model | Dimensions | Used For |
|---|---|---|
| `all-MiniLM-L6-v2` | 384 | Generating embeddings for documents and queries |

---

## Topics Covered in the Knowledge Base

- Retrieval-Augmented Generation (RAG)
- Natural Language Processing (NLP)
- Natural Language Understanding (NLU)
- Natural Language Generation (NLG)
- Machine Learning (ML)
- Deep Learning (DL)
- Elasticsearch
- Vector Databases
- Chatbots
- Conversational AI