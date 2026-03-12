import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

def chunk_sentences(text, chunk_size=1, overlap=0):
    sentences = sent_tokenize(text)
    chunks = []

    i = 0
    while i < len(sentences):
        chunk = sentences[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap

    return chunks

# read a file to test it on
with open("docs/rag.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_sentences(text)

# print to check
for i, chunk in enumerate(chunks):
    print(f"--- chunk {i+1} ---")
    print(chunk)
    print()
