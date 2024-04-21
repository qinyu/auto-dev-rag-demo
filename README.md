# 运行语义化搜索服务

## 1. 环境准备
### 1.1 安装 requirements.txt 中的依赖
```shell
pip install -r requirements.txt`
```
### 1.2 设置环境变量(API_KEY)

```shell
export PINECONE_API_KEY=<your Pinecone API key available at app.pinecone.io>
export OPENAI_API_KEY=<your OpenAI API key, available at platform.openai.com/api-keys>```
````

## 2. 运行服务
```shell
python ./rag_api.py
```

## 3. 发送请求
打开服务的文档链接：http://127.0.0.1:8000/docs, 点击`Try it out`按钮，输入请求参数，点击`Execute`按钮，查看返回结果。