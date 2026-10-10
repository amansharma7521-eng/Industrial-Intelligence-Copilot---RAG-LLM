from app.rag.embeddings import embed_text
import test_embeddings

text = "The bearing temperature should normally remain below 80°C"

embedding = embed_text(text)

print("Embedding dimension:", len(embedding))
print("First 10 values:", embedding[:10])