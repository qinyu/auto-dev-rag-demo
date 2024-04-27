import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

vectorstore = PineconeVectorStore(index_name="cmb-rag-demo",
                                  embedding=(OpenAIEmbeddings(
                                      api_key=os.environ["OPENAI_API_KEY"],
                                      base_url="https://api.aiproxy.io/v1"
                                  )))

app = FastAPI(title="CMB RAG Demo", description="Demo for CMB RAG", version="0.1.0")

class Message(BaseModel):
    role: str
    content: str


class Messages(BaseModel):
    messages: List[Message]


# @app.post("/api/agent/api-market", response_class=PlainTextResponse)
# def mock_market(messages: Messages):
#     return """

@app.post("/scenarios")
def read_item(body: Messages):
    return vectorstore.similarity_search(query=body.messages[0].content, k=3)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001)
