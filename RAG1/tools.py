from .indexing import vector_store
from langchain.tools import tool

last_retreieved_context = []


@tool
def collecting_info(query : str) -> str:
    """
    Search the PDF knowledge base and return relevant information
    for the users question
    """

    global last_retreieved_context

    docs = vector_store.similarity_search(query , k=3)

    last_retreieved_context = [doc.page_content for doc in docs]

    return "\n\n".join(last_retreieved_context)


