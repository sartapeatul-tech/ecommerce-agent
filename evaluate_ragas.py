import os
import sys
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ecommerce-agent-v2"

sys.path.append(os.path.dirname(__file__))

from app.graph.build_graph import build_graph
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

def run_evaluation():
    # Sample data for evaluation
    questions = [
        "What are some good wireless headphones under 100?",
        "Recommend a coffee maker with timer."
    ]
    answers = []
    contexts = []

    graph = build_graph()

    for query in questions:
        state = {
            "query": query,
            "products": [],
            "constraints": {},
            "filtered_products": [],
            "review_analysis": [],
            "ranked_products": [],
            "final_output": ""
        }
        result = graph.invoke(state)
        answers.append(result["final_output"])
        # For simplicity, use the query as context (in real RAG, this would be retrieved docs)
        contexts.append([query])

    # Sample ground truths
    ground_truths = [
        "Wireless headphones under 100 include options like the Wireless Headphones model.",
        "A coffee maker with timer is the Coffee Maker model."
    ]

    # Create dataset
    data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truths": ground_truths
    }
    dataset = Dataset.from_dict(data)

    # Evaluate
    result = evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy]
    )

    print("RAGAS Evaluation Results:")
    print(result)

if __name__ == "__main__":
    run_evaluation()