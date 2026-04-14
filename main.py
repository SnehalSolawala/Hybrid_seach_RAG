from dotenv import load_dotenv
import os

# Load environment variables from .env FIRST before any other imports
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("OPENAI_API_KEY not found. Please set it in your .env file.")

from ingestion.loader import load_pdf
from ingestion.chunking import chunk_text

from embeddings.dense import get_dense_embeddings
from embeddings.sparse import get_sparse_vector

from vectorstore.pinecone_db import init_index, upsert_data

from embeddings.sparse import build_bm25

from retrieval.hybrid_search import hybrid_search
from retrieval.reranker import rerank

from generation.llm import generate_answer

from evaluation.testcase import get_questions, get_ground_truths

from evaluation.metrics import build_ragas_dataset, run_ragas_evaluation


def run_pipeline(query, index):
    docs = hybrid_search(index, query)
    top_docs = rerank(query, docs)

    # remove duplicates
    top_docs = list(dict.fromkeys(top_docs))

    if not top_docs:
        return {
            "answer": "No relevant context found.",
            "sources": []
        }

    answer = generate_answer(query, top_docs)

    return {
        "answer": answer,
        "sources": top_docs
    }


if __name__ == "__main__":
    # Step 1: Load data
    text = load_pdf("data/GenAI_pdf.pdf")

    if not text:
        raise ValueError("PDF text extraction failed or file is empty")

    # Step 2: Chunk
    chunks = chunk_text(text)
    build_bm25(chunks)

    # Step 3: Init Pinecone
    index = init_index(force_recreate=True)

    # Step 4: Store
    upsert_data(index, chunks)

    # Step 5: Query
    query = "what are the selection criteria for LLM"

    result = run_pipeline(query, index)

    print("\nAnswer:\n", result["answer"])
    print("\nSources:\n", result["sources"])

    # -------------------------------
    # Step 6: Run Evaluation
    # -------------------------------
    print("\nRunning RAGAS evaluation...\n")

    questions = get_questions()
    ground_truths = get_ground_truths()

    ragas_data = build_ragas_dataset(
        questions=questions,
        ground_truths=ground_truths,
        pipeline_fn=run_pipeline,
        index=index
    )

    results = run_ragas_evaluation(ragas_data)

    print("\nRAGAS Results:\n")
    print(results)
"""
from ingestion.loader import load_pdf
from ingestion.chunking import chunk_text

from vectorstore.pinecone_db import init_index, upsert_data
from embeddings.sparse import build_bm25

from retrieval.hybrid_search import hybrid_search
from retrieval.reranker import rerank
from generation.llm import generate_answer

from evaluation.metrics import build_test_dataset, run_evaluation
from evaluation.testcase import summary


# ---------------------------
# PIPELINE
# ---------------------------

def run_pipeline(query, index):
    docs = hybrid_search(index, query)
    top_docs = rerank(query, docs)

    top_docs = list(dict.fromkeys(top_docs))  # remove duplicates

    answer = generate_answer(query, top_docs)

    return {
        "answer": answer,
        "sources": top_docs
    }


# ---------------------------
# MAIN
# ---------------------------

if __name__ == "__main__":

    print("\nLoading dataset summary...")
    summary()

    # Step 1: Load PDF
    text = load_pdf("data/GenAI_pdf.pdf")

    if not text:
        raise ValueError("PDF text extraction failed")

    # Step 2: Chunk
    chunks = chunk_text(text)

    # Step 3: BM25 index
    build_bm25(chunks)

    # Step 4: Vector DB
    index = init_index(force_recreate=True)
    upsert_data(index, chunks)

    # ---------------------------
    # EVALUATION
    # ---------------------------
    print("\nRunning evaluation...\n")

    test_results = build_test_dataset(run_pipeline, index)

    report = run_evaluation(test_results)

    # Print sample results
    print("\nSample result:")
    print(report["details"][0])"""