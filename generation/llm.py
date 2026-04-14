'''import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(query, context_docs):
    context = "\n\n".join(context_docs)

    prompt = f"""
You are an expert AI assistant.

Answer the question ONLY using the provided context.
If the answer is present, explain clearly.
DO NOT say "I don't know" if partial info is available.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:1b",   # ← changed from llama3
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
'''
'''
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(query, context_docs):
    context = "\n\n".join(context_docs)

    prompt = f"""
You are a highly accurate AI assistant.

STRICT RULES:
1. Answer ONLY from the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not clearly present in the context, say: "I don't know based on the provided context."
4. Do NOT guess or hallucinate.
5. Keep the answer concise and directly relevant to the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3:latest",   # 🔥 upgraded model
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,      # 🔥 reduces hallucination
                "top_p": 0.9,
                "num_predict": 300
            }
        }
    )

    return response.json()["response"]
'''
'''
RAGAS Results:

{'answer_relevancy': 0.7104, 'faithfulness': 0.8591, 'context_precision': 0.8667, 'context_recall': 0.9778}'''


# generation/llm.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, context_docs):
    context = "\n\n".join(context_docs)

    prompt = f"""You are a highly accurate AI assistant.

STRICT RULES:
1. Answer ONLY from the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not clearly present in the context, say: "I don't know based on the provided context."
4. Do NOT guess or hallucinate.
5. Keep the answer concise and directly relevant to the question.

Context:
{context}

Question:
{query}

Answer:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].message.content

'''
RAGAS Results:

{'answer_relevancy': 0.7029, 'faithfulness': 0.8211, 'context_precision': 0.8667, 'context_recall': 0.9444}'''