# retrieval/rerank.py

from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, docs, top_k=5, score_threshold=0.3):
    """
    docs = [{"text": ..., "score": ...}]
    """

    if not docs:
        return []

    pairs = [(query, d["text"]) for d in docs]
    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    filtered = [
        doc["text"]
        for doc, score in ranked
        if score > score_threshold
    ]

    return filtered[:top_k]