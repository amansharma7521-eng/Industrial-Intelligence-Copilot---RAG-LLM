import numpy as np

from app.rag.embeddings import embed_texts

texts = [
    "The bearing temperature should normally remain below 80°C.",
    "What is the normal temperature limit for the bearing?",
    "The compressor should undergo emergency shutdown when pressure exceeds 85 bar.",
]

embeddings = embed_texts(texts)

def cosine_similarity(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a)*np.linalg.norm(b)
    )
# to get all the embedding similarity relation between the three statements in text
n=len(texts)

for i in range(n - 1):
    for j in range(i + 1, n):
        score = cosine_similarity(embeddings[i], embeddings[j])

        print()
        print(f"Text{i + 1}  ↔  Text{j + 1}")
        print(f"Similarity: {score:.4f}")