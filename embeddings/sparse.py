# embeddings/sparse.py
from rank_bm25 import BM25Okapi
from collections import Counter

bm25 = None
vocab = None

def build_bm25(corpus):
    global bm25, vocab

    tokenized_corpus = [doc.split() for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)

    # Build a stable vocabulary: token → unique integer index
    all_tokens = sorted(set(token for doc in tokenized_corpus for token in doc))
    vocab = {token: idx for idx, token in enumerate(all_tokens)}

def get_sparse_vector(text: str) -> dict:
    """
    Returns a Pinecone-compatible sparse vector using vocab indices
    and BM25 IDF scores as weights.
    """
    global bm25, vocab

    if bm25 is None or vocab is None:
        raise ValueError("BM25 not initialized. Call build_bm25(corpus) first.")

    token_counts = Counter(text.split())
    indices = []
    values = []

    for token, tf in token_counts.items():
        if token in vocab and token in bm25.idf:
            idf = bm25.idf[token]
            if idf > 0:
                indices.append(vocab[token])
                values.append(float(tf * idf))  # simple TF-IDF weight

    # Pinecone requires at least one entry
    if not indices:
        return {"indices": [0], "values": [0.0]}

    return {"indices": indices, "values": values}