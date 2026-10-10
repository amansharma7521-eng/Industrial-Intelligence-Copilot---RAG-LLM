from pathlib import Path


def load_text_documents(directory: str) -> list[dict]:
    documents = []

    for file_path in Path(directory).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "document_id": file_path.stem,
                "source": file_path.name,
                "text": text,
            }
        )

    return documents