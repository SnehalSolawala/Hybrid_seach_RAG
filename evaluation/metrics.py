# evaluation/metrics.py
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness, context_precision, context_recall
from langchain_openai import ChatOpenAI
from ragas.run_config import RunConfig
from langchain_openai import OpenAIEmbeddings

def build_ragas_dataset(
    questions,
    ground_truths,
    pipeline_fn,
    index
):
    data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": []
    }

    for q, gt in zip(questions, ground_truths):
        result = pipeline_fn(q, index)

        data["question"].append(q)
        data["answer"].append(result["answer"])
        data["contexts"].append(result["sources"])  # list of chunks
        data["ground_truth"].append(gt)

    return Dataset.from_dict(data)

def run_ragas_evaluation(dataset):

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    config = RunConfig(max_workers=4, timeout=60)

    result = evaluate(
        dataset,
        metrics=[
            answer_relevancy,
            faithfulness,
            context_precision,
            context_recall
        ],
        llm=llm,
        embeddings=embeddings,
        run_config=config
    )

    return result