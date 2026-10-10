import numpy as np

def cosine_similarity(a,b):
    a=np.array(a)
    b=np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

def retrieve(
        query_embedding,
        indexed_chunks,
        top_k=3
):
    results = []

    for chunk in indexed_chunks:

        score = cosine_similarity(
            query_embedding,
            chunk["embedding"]
           )

        results.append(
            {
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "source": chunk["source"],
                "text": chunk["text"],
                "score": score,
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse =True
    )

    return results[:top_k]