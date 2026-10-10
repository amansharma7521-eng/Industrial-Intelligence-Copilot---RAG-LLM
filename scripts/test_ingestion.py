from app.rag.ingestion import load_text_documents


documents = load_text_documents("data/raw")

for document in documents:
    print("=" * 60)
    print("DOCUMENT:", document["source"])
    print(document["text"][:300])