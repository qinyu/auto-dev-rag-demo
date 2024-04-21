from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os
from langchain_core.documents import Document


# parse file content like this:
# """
# Feature: 新建博客
#   作为一位博客作者
#   我想在InnoRev网站上新建博客
#   以便于我可以发布我的文章
#
#   Scenario: 新建博客成功
#     Given 用户已经登录，并且填写了正确的博客信息
#     When  用户点击“新建博客”按钮
#     Then 系统创建一个新的博客，并返回博客的id
#
#   Scenario: 新建博客成功
#     Given 用户已经登录，并且填写了正确的博客信息
#     When  用户点击“新建博客”按钮
#     Then 系统创建一个新的博客，并返回博客的id
# """
# return a tuple like this:
# ("新建博客\n 作为一位博客作者\n  我想在InnoRev网站上新建博客\n  以便于我可以发布我的文章",
# , [{"scenario":"新建博客成功", "steps":["Given 用户已经登录，并且填写了正确的博客信息", "When  用户点击“新建博客”按钮", "Then 系统创建一个新的博客，并返回博客的id"]},
# }..])

def parse_feature_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        feature = ''
        scenarios = []
        scenario = None
        steps = []
        for line in lines:
            line = line.strip()
            if line.startswith('Feature:'):
                feature = line.split(":")[-1].strip()
            elif line.startswith('Scenario:'):
                if scenario:
                    scenarios.append({'scenario': scenario, 'steps': steps})
                scenario = line.split(":")[-1].strip()
                steps = []
            else:
                steps.append(line)
        if scenario:
            scenarios.append({'scenario': scenario, 'steps': steps})
        return feature, scenarios


# loop all files which name ends with '.feature' in 'features' folder
def load_docs():
    _docs = []
    for _, _, files in os.walk('features'):
        for file in files:
            if file.endswith('.feature'):
                print(file)
                file_path = os.path.join('features', file)
                feat, scenarios = parse_feature_file(file_path)
                for _s in scenarios:
                    _docs.append(Document(_s['scenario'],
                                          metadata={'feature': feat,
                                                    'source': file_path,
                                                    'steps': _s['steps']}))
    return _docs


if __name__ == '__main__':
    docs = load_docs()
    print(docs)
    if '-y' in os.sys.argv:
        vectorstore = PineconeVectorStore(index_name="cmb-rag-demo",
                                          embedding=(OpenAIEmbeddings(
                                              api_key=os.environ["OPENAI_API_KEY"],
                                              base_url="https://api.aiproxy.io/v1"
                                          )))
        vectorstore.delete(delete_all=True)
        vectorstore.add_documents(documents=docs)
