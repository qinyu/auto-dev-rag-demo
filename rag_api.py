import os

from fastapi import FastAPI
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

vectorstore = PineconeVectorStore(index_name="cmb-rag-demo",
                                  embedding=(OpenAIEmbeddings(
                                      api_key=os.environ["OPENAI_API_KEY"],
                                      base_url="https://api.aiproxy.io/v1"
                                  )))

app = FastAPI(title="CMB RAG Demo", description="Demo for CMB RAG", version="0.1.0")


@app.get("/scenarios")
def read_item(query: str, k: int = 3):
    return vectorstore.similarity_search(query, k=k)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001)
