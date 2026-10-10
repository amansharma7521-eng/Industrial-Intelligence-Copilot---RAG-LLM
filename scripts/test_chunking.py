from app.rag.ingestion import load_text_documents
from app.rag.chunking import chunk_documents


documents = load_text_documents("data/raw")

chunks = chunk_documents(documents)

for chunk in chunks:
    print("=" * 60)
    print("CHUNK ID:", chunk["chunk_id"])
    print("SOURCE:", chunk["source"])
    print("TEXT:")
    print(chunk["text"])