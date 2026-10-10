# Industrial Intelligence Copilot

## Objective

Build an industrial-scale AI system while learning RAG and LLM
engineering through implementation.

The system will eventually support:

- Document RAG
- Hybrid retrieval
- Reranking
- Query transformation
- RAG evaluation
- SQL + RAG
- Agentic RAG
- Multimodal RAG
- GraphRAG
- Production deployment

## Learning methodology

Build → Understand → Break → Improve → Measure

For every major component we should understand:

1. Why it exists
2. How it works
3. How the code implements it
4. Data flow
5. Failure modes
6. Evaluation methodology

## Current Stage

Stage 1 — Basic RAG

## Current Stage

Stage 1 — Basic RAG

## Completed

- Project structure created
- Initial industrial dataset created
- Text document ingestion implemented
- Baseline paragraph-based chunking implemented
- Chunk output inspected
- Local embedding model integrated
- Basic semantic similarity experiment completed
- In-memory semantic retriever implemented
- Five manual retrieval queries tested
- Initial retrieval failure analysis completed

## Current Pipeline

Documents
→ Ingestion
→ Baseline Chunking
→ Local Embeddings
→ In-Memory Semantic Retrieval
→ Retrieval Evaluation

## Current Chunking Baseline

The current chunker uses paragraph boundaries.

Known limitations:

- Section headings can become standalone chunks.
- Document titles can become standalone chunks.
- Dates can become standalone chunks.
- Semantic relationships between adjacent paragraphs are not explicitly preserved.
- Chunk size is not token-aware.
- No overlap is currently used.
- Document and section context are not automatically attached to every chunk.

These limitations will be evaluated and improved later rather than prematurely optimized.

## Current Retrieval Baseline

The current retriever:

- Embeds the user query using the same local embedding model as the chunks.
- Computes cosine similarity between the query embedding and every chunk embedding.
- Sorts chunks by similarity score in descending order.
- Returns the top-K chunks.
- Preserves chunk text, chunk ID, document ID, source, embedding, and similarity score.

Current retrieval approach:

- Dense semantic retrieval only
- In-memory search
- Brute-force comparison against every chunk
- No vector database
- No BM25 or keyword retrieval
- No reranking
- No metadata filtering
- No query transformation

## Initial Retrieval Findings

The manual experiments revealed:

1. Section headings can rank highly even when they do not contain the answer.
2. A document title can rank highly because it identifies the correct document but does not provide the required information.
3. Related evidence may be retrieved even when it does not directly answer the query.
4. Dense retrieval can miss an important chunk, as observed in the lubrication-problem query.
5. Similarity scores are not probabilities or confidence values.
6. Dense semantic similarity does not guarantee factual or operational relevance.

## Baseline Evaluation

Initial manual evaluation used five queries.

Observed approximate results:

- Recall@1: 40%
- Recall@3: 60%
- Recall@5: 80%

Important limitations:

- The dataset contains only five queries.
- The corpus contains only sixteen chunks.
- Relevance judgments are preliminary.
- Some questions require multiple evidence chunks.
- These numbers are educational baseline measurements, not production performance claims.

## Current Goal

Create a formal retrieval evaluation dataset and automate:

- Recall@1
- Recall@3
- Recall@5

The evaluation should compare retrieved chunk IDs against manually defined relevant chunk IDs.

## Next Task

Build:

- `evaluation/dataset/retrieval_questions.json`
- `scripts/evaluate_retrieval.py`

Then inspect the automated evaluation results before changing chunking or retrieval methods.