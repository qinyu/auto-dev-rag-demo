import os
from typing import List

from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from pydantic import BaseModel

vectorstore = PineconeVectorStore(index_name="cmb-rag-demo",
                                  embedding=(OpenAIEmbeddings(
                                      api_key=os.environ["OPENAI_API_KEY"],
                                      base_url="https://api.aiproxy.io/v1"
                                  )))

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

groq = ChatGroq(model_name="llama3-8b-8192")

openai = ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"],
                    base_url="https://api.aiproxy.io/v1")


def format_docs(docs):
    """
    Format the documents for the RAG prompt
    :param docs:
    :return:
    """
    features = []
    for doc in docs:
        meta = doc.metadata
        steps = "".join(f"  {step}\n" for step in meta['steps'] if len(step.strip()) > 0)
        features.append(f"Feature: {meta['feature']}\n{steps}")
    return "---\n".join(features)


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


@app.post("/domainQuery")
def query_domain_api(body: Messages):
    return query_domain(body.messages[0].content)


def query_domain(query):
    custom_rag_prompt = PromptTemplate.from_template("""从下面上下文的 feature 中提取和最后的问题有关的事实。最多用5句话来概括事实，每一句话尽可能保持精炼。
    请不要增加额外的信息，只提取和问题有关的事实。如果无法提取到相关事实，请回答案。
    
    上下文：
    {features}

    问题: {question}

    事实:""")
    rag_chain = (
            {"features": retriever | format_docs, "question": RunnablePassthrough()}
            | custom_rag_prompt
            | openai
            | StrOutputParser()
    )
    return rag_chain.invoke(query)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001)
