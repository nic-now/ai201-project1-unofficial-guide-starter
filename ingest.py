"""
ingest.py
Loads documents from documents/, cleans them, splits into chunks,
and prints 5 random chunks for inspection.
Run after fetch_docs.py.
"""

import os
import re
import random
from transformers import AutoTokenizer

DOCS_DIR = "documents"
CHUNK_SIZE = 250   # tokens — must stay under all-MiniLM-L6-v2's 256-token limit
OVERLAP = 50       # tokens of overlap between consecutive chunks
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Using the actual model tokenizer keeps token counts accurate
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def load_documents(docs_dir):
    docs = []
    for filename in sorted(os.listdir(docs_dir)):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(docs_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        docs.append({"source": filename, "text": text})
    print(f"Loaded {len(docs)} documents from {docs_dir}/")
    return docs


def clean_text(text):
    # Decode leftover HTML entities
    text = (text
        .replace("&amp;", "&")
        .replace("&nbsp;", " ")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&#39;", "'")
        .replace("&quot;", '"')
    )
    # Collapse 3+ blank lines into a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(text, source):
    """
    Splits text into overlapping token-based chunks.
    Returns a list of dicts: {text, source}
    """
    # encode without special tokens so we count only real content tokens
    token_ids = tokenizer.encode(text, add_special_tokens=False)
    chunks = []
    start = 0
    while start < len(token_ids):
        end = min(start + CHUNK_SIZE, len(token_ids))
        chunk_str = tokenizer.decode(token_ids[start:end], skip_special_tokens=True).strip()
        if chunk_str:  # skip empty chunks
            chunks.append({"text": chunk_str, "source": source})
        if end == len(token_ids):
            break
        start += CHUNK_SIZE - OVERLAP
    return chunks


def main():
    docs = load_documents(DOCS_DIR)
    if not docs:
        print("No .txt files found in documents/. Run fetch_docs.py first.")
        return []

    all_chunks = []
    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned, doc["source"])
        all_chunks.extend(chunks)
        print(f"  {doc['source']}: {len(chunks)} chunks")

    total = len(all_chunks)
    print(f"\nTotal chunks: {total}")
    if total < 50:
        print("  Warning: fewer than 50 chunks — chunks may be too large or documents are short.")
    elif total > 2000:
        print("  Warning: more than 2000 chunks — chunks may be too small.")
    else:
        print("  Chunk count looks healthy (50–2000 range).")

    # Inspect 5 random chunks — read these and ask: does each make sense on its own?
    print("\n--- 5 RANDOM CHUNKS FOR INSPECTION ---")
    for i, chunk in enumerate(random.sample(all_chunks, min(5, total)), 1):
        print(f"\n[Chunk {i} | source: {chunk['source']}]")
        print(chunk["text"])

    return all_chunks


if __name__ == "__main__":
    main()
