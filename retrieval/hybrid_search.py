# retrieval/hybrid_search.py

from embeddings.dense import get_dense_embeddings
from embeddings.sparse import get_sparse_vector


def hybrid_search(index, query, top_k=20, alpha=0.7):
    """
    alpha = weight for dense (semantic)
    (1 - alpha) = weight for sparse (keyword/BM25)
    """

    dense_vec = get_dense_embeddings([query])[0]
    sparse_vec = get_sparse_vector(query)

    results = index.query(
        vector=(dense_vec * alpha).tolist(),
        sparse_vector={
            "indices": sparse_vec["indices"],
            "values": [v * (1 - alpha) for v in sparse_vec["values"]],
        },
        top_k=top_k,
        include_metadata=True,
        include_values=False
    )

    docs = []
    for match in results["matches"]:
        text = match["metadata"]["text"]
        score = match["score"]

        docs.append({
            "text": text,
            "score": score
        })

    return docs