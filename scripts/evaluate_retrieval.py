import json

from app.rag.ingestion import load_text_documents
from app.rag.chunking import chunk_documents
from app.rag.embeddings import embed_texts,embed_text
from app.rag.retrieval import retrieve

from pathlib import Path

base_dir = Path(r"C:\Users\amans\Downloads\industrial-intelligence-copilot")

paths = {
    "raw_data": base_dir/"data"/"raw",
    "evaluation_file": base_dir/"evaluation"/"retrieval_questions.json",
    "output_dir": base_dir/"output",
}

def build_indexed_chunks():
    """
    Load documents, create, generate embeddings,
    and attach each embedding to its corresponding chunk.
    """

    documents = load_text_documents(str(paths["raw_data"]))

    chunks = chunk_documents(documents)

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embed_texts(texts)

    indexed_chunks = []

    for chunk, embedding in zip(chunks, embeddings):
        indexed_chunks.append(
            {
                **chunk,
                "embedding": embedding
            }
        )

    return indexed_chunks


def load_evaluation_dataset(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_query(query_record, indexed_chunks):
    query = query_record["query"]
    relevant_chunks = set(query_record["relevant_chunks"])

    query_embedding = embed_text(query)

    retrieved_results = retrieve(
        query_embedding=query_embedding,
        indexed_chunks=indexed_chunks,
        top_k=5
    )

    retrieved_chunk_ids = [
        result["chunk_id"]
        for result in retrieved_results
    ]

    metrics = {}

    for k in [1, 3, 5]:

        top_k_ids = set(
            retrieved_chunk_ids[:k]
        )


        relevant_retrieved = (
            top_k_ids.intersection(relevant_chunks)
        )

        # Hit Rate@k:
        # Did we retrieve at least one relevant chunk?

        hit = bool(relevant_retrieved)

        metrics[f"hit_rate_at_{k}"] = int(hit)

        # Recall@K:
        # What fraction of all relevant chunks
        # were retrieved within the top k?

        recall = (
            len(relevant_retrieved)
            / len(relevant_chunks)
        )

        metrics[f"recall_at_{k}"] = recall


    return {
        "query": query,
        "relevant_chunks": list(relevant_chunks),
        "retrieved_chunk_ids": retrieved_chunk_ids,
        "metrics": metrics
    }


def calculate_average_metrics(results):
    number_of_queries = len(results)
    averages = {}

    for metric_name in [
        "recall_at_1",
        "recall_at_3",
        "recall_at_5"
    ]:
        total = sum(
            result["metrics"][metric_name]
            for result in results
        )
        averages[metric_name] = total / number_of_queries

    return averages


def main():
    indexed_chunks = build_indexed_chunks()
    evaluation_dataset = load_evaluation_dataset(str(paths["evaluation_file"]))

    results = []

    for query_record in evaluation_dataset:
        result = evaluate_query(
            query_record=query_record,
            indexed_chunks=indexed_chunks
        )
        results.append(result)

    for index, result in enumerate(results, start=1):
        print("=" * 80)
        print("QUERY", index)
        print(result["query"])

        print("\nRetrieved chunks:")
        for rank, chunk_id in enumerate(result["retrieved_chunk_ids"], start=1):
            print(f"{rank}. {chunk_id}")

        print("\nMetrics:")
        print(result["metrics"])

    averages = calculate_average_metrics(results)

    print("=" * 80)
    print("AVERAGE METRICS")

    for metric_name, value in averages.items():
        print(f"{metric_name}:{value:2%}")


if __name__ == "__main__":
    main()