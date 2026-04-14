using ollama = llama3:latest
{'answer_relevancy': 0.7104, 'faithfulness': 0.8591, 'context_precision': 0.8667, 'context_recall': 0.9778}

using openAI : gpt-3.5-turbo
RAGAS Results:

{'answer_relevancy': 0.7029, 'faithfulness': 0.8211, 'context_precision': 0.8667, 'context_recall': 0.9444}


# 📚 Hybrid Search RAG (Retrieval Augmented Generation)

## 🚀 Overview

This project implements a **Hybrid Search-based Retrieval Augmented Generation (RAG) system**, combining both **dense (vector-based semantic search)** and **sparse (BM25 keyword search)** techniques to improve retrieval quality for Large Language Model (LLM) responses.

Instead of relying only on embeddings, this system enhances accuracy by combining:
- Semantic understanding (Vector Search)
- Keyword matching (BM25)
- Hybrid ranking fusion

This makes the system more reliable for:
- Domain-specific Q&A
- Technical documentation
- Keyword-heavy queries
- Enterprise search applications

---

## 🧠 Why Hybrid Search?

Traditional RAG systems use only vector search, which has limitations:

| Method | Strength | Weakness |
|--------|----------|----------|
| Dense (Vector Search) | Understands meaning and context | Misses exact keywords |
| Sparse (BM25 Search) | Strong keyword matching | Weak semantic understanding |

### ✅ Hybrid Search Advantage

This project combines both approaches to achieve:
- Better retrieval accuracy
- Higher recall + precision
- More robust LLM context generation

---

## 🏗️ System Architecture
User Query
│
▼
Query Processing
│
├── Dense Retrieval (Embeddings / Vector DB)
├── Sparse Retrieval (BM25 / Keyword Search)
│
▼
Hybrid Fusion (RRF / Weighted Scoring)
│
▼
Top-K Relevant Documents
│
▼
LLM (OpenAI / Ollama / Local Model)
│
▼
Final Answer Generation



---

## ⚙️ Features

- 🔍 Hybrid Search (Dense + Sparse retrieval)
- ⚡ Improved document recall and ranking
- 🧠 Semantic + keyword-based query handling
- 🤖 LLM-powered response generation
- 📄 Works with custom documents (PDF, text, etc.)
- 🔧 Modular and scalable architecture

---

## 🧰 Tech Stack

- Python
- LangChain
- FAISS / ChromaDB (Vector Database)
- BM25 (Keyword Search)
- OpenAI / Ollama / LLM APIs

---

## 📁 Project Structure
Hybrid_seach_RAG/




---

## 🔄 How It Works

### 1. Document Ingestion
Documents are loaded from the `data/` folder and split into chunks.

### 2. Embedding Generation
Chunks are converted into vector embeddings and stored in a vector database.

### 3. Sparse Indexing
A BM25 index is created for keyword-based retrieval.

### 4. Query Processing
User query is processed in two ways:
- Dense retrieval (semantic similarity)
- Sparse retrieval (keyword matching)

### 5. Hybrid Fusion
Results are merged using:
- Reciprocal Rank Fusion (RRF)
or
- Weighted ranking system

### 6. Context Selection
Top relevant chunks are selected.

### 7. LLM Generation
The selected context is passed to an LLM to generate a final grounded response.

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/SnehalSolawala/Hybrid_seach_RAG
cd Hybrid_seach_RAG
```
### 2.Create virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate'
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set environment variables
   OPENAI_API_KEY=your_api_key
  PINECONE_API_KEY= PINECONE_API


before run write your query in main.py file:
example:
query = "what are the selection criteria for LLM"


### 5. Run the application
```bash
python main.py
```


