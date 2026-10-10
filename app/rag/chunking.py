def chunk_documents(documents: list[dict]) -> list[dict]:
    chunks = []

    for document in documents:
        paragraphs = [
            paragraph.strip()
            for paragraph in document["text"].split("\n\n")
            if paragraph.strip()
        ]

        for index, paragraph in enumerate(paragraphs):
            chunks.append(
                {
                    "chunk_id": f"{document['document_id']}_{index:03d}",
                    "document_id": document["document_id"],
                    "source": document["source"],
                    "text": paragraph,
                }
            )

    return chunks