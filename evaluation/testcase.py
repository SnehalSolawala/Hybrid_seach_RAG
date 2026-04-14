# evaluation/test_cases.py
"""
Test cases generated from: Generative AI and LLMs For Dummies (Snowflake Special Edition)
                            by David Baum, Wiley 2024

How to use:
    from evaluation.test_cases import TEST_CASES, get_questions, get_ground_truths
    from evaluation.metrics import build_test_dataset, run_evaluation

    test_data = build_test_dataset(
        questions    = get_questions(),
        ground_truths= get_ground_truths(),
        pipeline_fn  = run_pipeline,
        index        = index
    )
    results = run_evaluation(test_data)

Difficulty levels:
    easy   — answer is stated almost word-for-word in the PDF (tests basic retrieval)
    medium — answer requires combining 2-3 sentences from the PDF
    hard   — answer requires reasoning across multiple sections / chapters
"""

TEST_CASES = [

    # -----------------------------------------------------------------------
    # CHAPTER 1 — Introducing Gen AI and the Role of Data
    # -----------------------------------------------------------------------
    {
        "id": "ch1_easy_01",
        "difficulty": "easy",
        "chapter": 1,
        "topic": "Gen AI definition",
        "question": "What is generative AI?",
        "ground_truth": (
            "Generative AI is a type of artificial intelligence that uses neural networks "
            "and deep learning algorithms to identify patterns within existing data as a "
            "basis for generating original content such as text, images, audio, and video."
        ),
    },
    {
        "id": "ch1_easy_03",
        "difficulty": "easy",
        "chapter": 1,
        "topic": "GPU role",
        "question": "Why are GPUs important for AI model training?",
        "ground_truth": (
            "GPUs have a large number of cores that can process multiple tasks "
            "simultaneously. This parallel processing capability accelerates training "
            "and inference times, making them much faster than CPUs for the "
            "computationally intensive matrix operations involved in machine learning."
        ),
    },

    # -----------------------------------------------------------------------
    # CHAPTER 2 — Understanding Large Language Models
    # -----------------------------------------------------------------------
    {
        "id": "ch2_easy_01",
        "difficulty": "easy",
        "chapter": 2,
        "topic": "LLM definition",
        "question": "What are large language models (LLMs)?",
        "ground_truth": (
            "Large language models are advanced AI systems designed to understand the "
            "intricacies of human language and generate intelligent, creative responses "
            "when queried. They are trained on enormous data sets typically measured in "
            "petabytes, using deep learning techniques to excel at understanding and "
            "generating text similar to human-produced content."
        ),
    },
    {
        "id": "ch2_hard_01",
        "difficulty": "hard",
        "chapter": 2,
        "topic": "Data governance",
        "question": "How should enterprises enforce data governance when using LLMs?",
        "ground_truth": (
            "Enterprises should use a cloud data platform that brings processing to the "
            "data rather than taking data to the processing engine. This allows control "
            "over user access to corporate data sources and enforcement of security and "
            "governance policies. Running the model as a service within the cloud data "
            "platform ensures that data, prompts, and completions are not shared with "
            "unauthorized users. The platform should extend governance to all data types: "
            "structured, semistructured, and unstructured."
        ),
    },

    # -----------------------------------------------------------------------
    # CHAPTER 3 — LLM App Project Lifecycle
    # -----------------------------------------------------------------------
    {
        "id": "ch3_easy_01",
        "difficulty": "easy",
        "chapter": 3,
        "topic": "Selection criteria",
        "question": "What are the selection criteria for choosing the right LLM for a project?",
        "ground_truth": (
            "When selecting the right LLM, consider: task alignment (choose an LLM "
            "that aligns to the task, such as GPT for conversational apps or BioBERT "
            "for biomedical research), training data (whether it matches the domain), "
            "model size and complexity (larger models give higher-quality outputs but "
            "need more compute), adapting and tuning (whether the LLM can be "
            "contextualized with prompts or fine-tuning), and ecosystem and support "
            "(availability of resources, tools, and community support)."
        ),
    },
    {
        "id": "ch3_medium_01",
        "difficulty": "medium",
        "chapter": 3,
        "topic": "Small vs large LLMs",
        "question": "What is the tradeoff between small and large language models?",
        "ground_truth": (
            "Smaller LLMs have fewer parameters, consume less compute resources, and "
            "are faster to fine-tune and deploy — they are well suited for running "
            "specific tasks cost-effectively. Larger LLMs with typically 10 billion or "
            "more parameters can learn more nuanced language patterns and provide more "
            "accurate outputs for a wider range of scenarios, but require more resources "
            "to train and adapt. The choice is a cost-performance tradeoff depending "
            "on the use cases that need to be supported."
        ),
    },
    {
        "id": "ch3_medium_02",
        "difficulty": "medium",
        "chapter": 3,
        "topic": "Fine-tuning",
        "question": "What are the three basic steps to fine-tune a language model?",
        "ground_truth": (
            "The three basic steps to fine-tune an LLM are: first, select the pretrained "
            "LLM most relevant to the use case; second, identify data sets related to the "
            "use case to refine the LLM by teaching the model using a training data set "
            "that includes example prompts and the data the model needs to answer them "
            "(the model weights are adjusted during this step); and third, evaluate the "
            "fine-tuned LLM to verify results meet requirements, adjusting learning rate "
            "and batch size as needed."
        ),
    },
    {
        "id": "ch3_hard_02",
        "difficulty": "hard",
        "chapter": 3,
        "topic": "Vector database role",
        "question": "Why is a vector database important for RAG applications?",
        "ground_truth": (
            "A vector database enables efficient storage, retrieval, and manipulation "
            "of vector embeddings. By assigning a unique key to each vector, it allows "
            "quick and direct access to content at a discrete level. In RAG applications, "
            "rapid retrieval and matching of vectors allow the model to discover "
            "semantically related text — for example, finding a product similar to one a "
            "customer previously searched for. This is more efficient than exact matching "
            "because data is identified based on similarity metrics like distance "
            "between vectors."
        ),
    },

    # -----------------------------------------------------------------------
    # CHAPTER 4 — Bringing LLM Apps into Production
    # -----------------------------------------------------------------------
    {
        "id": "ch4_easy_02",
        "difficulty": "easy",
        "chapter": 4,
        "topic": "Latency",
        "question": "What is latency in the context of LLMs and how can it be reduced?",
        "ground_truth": (
            "Latency refers to the time it takes an LLM to make predictions once it "
            "receives input data. To reduce latency, strategies include using smaller "
            "models, optimizing models for inference, using efficient hardware and "
            "software, and keeping the processing close to the data. This last strategy "
            "also reduces the amount of data transferred between compute resources "
            "and the storage layer, improving performance while reducing costs and "
            "data security risks."
        ),
    },
    {
        "id": "ch4_medium_02",
        "difficulty": "medium",
        "chapter": 4,
        "topic": "LLMOps",
        "question": "What is LLMOps and what does an orchestration library do?",
        "ground_truth": (
            "LLMOps stands for LLM operations — a set of developer tools and frameworks "
            "for building AI-powered applications. An orchestration library simplifies "
            "access to external data sources and connects to APIs within other "
            "applications. It enables chaining together different prompts to create "
            "complex applications, connecting to external data sources like databases "
            "and APIs, and scaling to multiple LLMs for different specialized tasks."
        ),
    },
    {
        "id": "ch4_hard_01",
        "difficulty": "hard",
        "chapter": 4,
        "topic": "Chunking and context window",
        "question": "Why is chunking necessary in RAG systems and how does it relate to the context window?",
        "ground_truth": (
            "Many text sources are too long to fit into the limited context window of an "
            "LLM, which typically holds only a few thousand tokens. In RAG systems, "
            "external data sources are divided into chunks that each fit within the "
            "context window. These chunks are then chained together so the model can "
            "process the information. Packages like LangChain can handle this chunking "
            "and chaining automatically."
        ),
    },

    # -----------------------------------------------------------------------
    # CHAPTER 5 — Security and Ethical Considerations
    # -----------------------------------------------------------------------
    {
        "id": "ch5_medium_01",
        "difficulty": "medium",
        "chapter": 5,
        "topic": "Data privacy concerns",
        "question": "What are the three main data privacy concerns when using gen AI applications?",
        "ground_truth": (
            "The three main data privacy concerns are: unintentional disclosure of "
            "sensitive information (gen AI apps can generate outputs containing sensitive "
            "customer data even when not explicitly prompted), misuse of generated data "
            "(gen AI can create synthetic data indistinguishable from real data that "
            "could be used for identity theft or deep fakes), and compliance violations "
            "(data privacy regulations like GDPR and CCPA impose strict requirements "
            "on how businesses collect and use personal data, including data used to "
            "train gen AI models)."
        ),
    },
    {
        "id": "ch5_hard_01",
        "difficulty": "hard",
        "chapter": 5,
        "topic": "Open-source risks",
        "question": "What are the risks of using open-source LLMs and tools for building gen AI apps?",
        "ground_truth": (
            "Open-source LLMs like Llama 2, BERT, and Falcon can come with risks from "
            "their training data sets, which are often not publicly accessible. "
            "Other open-source tools such as orchestration frameworks and vector "
            "databases may be vulnerable if not regularly updated and patched — "
            "malicious entities can exploit these vulnerabilities without proper "
            "security measures. Open-source offerings may also exhibit inconsistent "
            "quality due to their nature as byproducts of many community contributions. "
            "Organizations should consider cost, performance, and compliance risks "
            "based on their specific needs and risk tolerance."
        ),
    },

    # -----------------------------------------------------------------------
    # CHAPTER 6 — Five Steps to Generative AI
    # -----------------------------------------------------------------------
    {
        "id": "ch6_easy_01",
        "difficulty": "easy",
        "chapter": 6,
        "topic": "Five steps",
        "question": "What are the five steps to generative AI outlined in the book?",
        "ground_truth": (
            "The five steps to generative AI are: (1) Identify Business Problems — "
            "rank potential projects by business impact, data readiness, and executive "
            "sponsorship; (2) Select a Data Platform — standardize on a scalable, "
            "governed cloud data platform; (3) Build a Data Foundation — consolidate "
            "data, remove silos, and establish data governance procedures; (4) Create "
            "a Culture of Collaboration — enable all stakeholders to access data sets "
            "simultaneously and educate users on prompt engineering; (5) Measure, "
            "Learn, Celebrate — start small, identify metrics, validate progress, "
            "and democratize gen AI capabilities."
        ),
    },

    # -----------------------------------------------------------------------
    # CROSS-CHAPTER / HARD REASONING
    # -----------------------------------------------------------------------
    {
        "id": "cross_hard_01",
        "difficulty": "hard",
        "chapter": "3+4",
        "topic": "RAG pipeline full flow",
        "question": "How does a RAG system work end-to-end from ingestion to answer generation?",
        "ground_truth": (
            "A RAG system works as follows: first, documents are loaded and split into "
            "chunks that fit within the LLM's context window. These chunks are converted "
            "into vector embeddings and stored in a vector database. At query time, the "
            "user's question is also converted into a vector and used to retrieve the "
            "most semantically similar chunks from the database. These retrieved chunks "
            "are then injected into the prompt as context, and the LLM generates an "
            "answer grounded in that retrieved information rather than relying solely "
            "on its pretrained knowledge."
        ),
    },
]


# ---------------------------------------------------------------------------
# Convenience helpers
# ---------------------------------------------------------------------------

def get_questions(difficulty: str | None = None, chapter: int | None = None) -> list[str]:
    """
    Returns a list of questions, optionally filtered by difficulty or chapter.

    Args:
        difficulty : 'easy', 'medium', or 'hard'  (None = all)
        chapter    : chapter number (None = all)
    """
    cases = TEST_CASES
    if difficulty:
        cases = [c for c in cases if c["difficulty"] == difficulty]
    if chapter:
        cases = [c for c in cases if str(c["chapter"]) == str(chapter)]
    return [c["question"] for c in cases]


def get_ground_truths(difficulty: str | None = None, chapter: int | None = None) -> list[str]:
    """
    Returns a list of ground truth answers matching the same filters as get_questions().
    Always call get_questions() and get_ground_truths() with the same filters.
    """
    cases = TEST_CASES
    if difficulty:
        cases = [c for c in cases if c["difficulty"] == difficulty]
    if chapter:
        cases = [c for c in cases if str(c["chapter"]) == str(chapter)]
    return [c["ground_truth"] for c in cases]


def get_by_topic(topic_keyword: str) -> list[dict]:
    """Returns test cases whose topic contains the keyword (case-insensitive)."""
    kw = topic_keyword.lower()
    return [c for c in TEST_CASES if kw in c["topic"].lower()]


def summary():
    """Prints a summary of the test set."""
    from collections import Counter
    difficulties = Counter(c["difficulty"] for c in TEST_CASES)
    chapters     = Counter(str(c["chapter"]) for c in TEST_CASES)
    print(f"\nTotal test cases : {len(TEST_CASES)}")
    print(f"By difficulty    : {dict(difficulties)}")
    print(f"By chapter       : {dict(sorted(chapters.items()))}")
    print()


# ---------------------------------------------------------------------------
# Quick usage example (run this file directly to see the summary)
# ---------------------------------------------------------------------------
"""
if __name__ == "__main__":
    summary()

    print("Sample easy question:")
    print(" Q:", get_questions(difficulty="easy")[0])
    print(" A:", get_ground_truths(difficulty="easy")[0])

    print("\nSample hard question:")
    print(" Q:", get_questions(difficulty="hard")[0])
    print(" A:", get_ground_truths(difficulty="hard")[0])
"""