from app.rag.ingestion import load_text_documents
from app.rag.chunking import chunk_documents
from app.rag.embeddings import embed_text, embed_texts

from app.rag.retrieval import retrieve



#1 Load Documents

documents = load_text_documents(r"C:\Users\amans\Downloads\industrial-intelligence-copilot\data\raw")

#2 Chunk documents

chunks = chunk_documents(documents)

#3 Extract chunk text

texts = [
    chunk["text"]
    for chunk in chunks
]

#4 Generate embeddings

embeddings = embed_texts(texts)

#5. Create indexed chunks

indexed_chunks = []

for chunk, embedding in zip(chunks, embeddings):
    indexed_chunks.append(
        {
            **chunk,
            "embedding": embedding,
        }
    )

#6 User query

query = "How should maintenence activities be performed?"

#7 embed query

query_embedding = embed_text(query)

#8 Retrieve top results

results = retrieve(
    query_embedding,
    indexed_chunks,
    top_k=5,
)

#9 Display results

for rank, result in enumerate(results, start=1):
    print("=" * 70)
    print("RANK:", rank)
    print("CHUNK ID:", result["chunk_id"])
    print("SOURCE:", result["source"])
    print("SCORE:", round(result["score"], 4))

    print("\nTEXT:")
    print(result["text"])
