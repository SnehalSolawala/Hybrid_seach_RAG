# embeddings/dense.py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")

def get_dense_embeddings(texts):
    return model.encode(texts)