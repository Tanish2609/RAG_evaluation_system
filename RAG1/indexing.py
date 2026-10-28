from dotenv import load_dotenv
from file_reader import extract_paragraphs
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("../pdfs/Penguins_ACL.pdf")
vector_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")
