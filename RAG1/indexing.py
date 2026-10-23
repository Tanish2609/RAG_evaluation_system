from file_reader import extract_paragraphs
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)

vector_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("../pdfs/Penguins_ACL.pdf")
vector_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")
