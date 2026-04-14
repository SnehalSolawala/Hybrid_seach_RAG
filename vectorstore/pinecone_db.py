# vectorstore/pinecone_db.py
import os
from pinecone import Pinecone, ServerlessSpec
from embeddings.dense import get_dense_embeddings
from embeddings.sparse import get_sparse_vector

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "hybrid-rag"

def init_index(force_recreate: bool = False):
    """
    Initializes a Pinecone index that supports hybrid (sparse+dense) search.
    The index MUST use metric='dotproduct' for sparse values to work.

    Set force_recreate=True to delete and rebuild if the index already exists
    with a wrong configuration (e.g., cosine metric).
    """
    existing = pc.list_indexes().names()

    if force_recreate and index_name in existing:
        print(f"[init_index] Deleting existing index '{index_name}' for recreation...")
        pc.delete_index(index_name)
        existing = []

    if index_name not in existing:
        print(f"[init_index] Creating index '{index_name}' with dotproduct metric...")
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="dotproduct",   # ← REQUIRED for sparse+dense hybrid search
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    else:
        print(f"[init_index] Using existing index '{index_name}'.")

    return pc.Index(index_name)


def upsert_data(index, chunks):
    dense_vectors = get_dense_embeddings(chunks)

    vectors = []
    for i, chunk in enumerate(chunks):
        vectors.append({
            "id": f"doc-{i}",
            "values": dense_vectors[i].tolist(),
            "sparse_values": get_sparse_vector(chunk),
            "metadata": {"text": chunk}
        })

    index.upsert(vectors=vectors)
    print(f"[upsert_data] Upserted {len(vectors)} vectors.")