from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
from langchain.chat_models import init_chat_model
from langchain_ollama import ChatOllama
from typing import TypedDict

load_dotenv()

gemma4 = ChatOllama(model="qwen3-coder:8b", base_url="http://server.raonworks.com:11434", temperature=1)


class MyState(TypedDict):
    message: str

def say_hello(state):
     return {"message": "hi, langgraph!!!"}

graph = StateGraph(MyState)
graph.add_node("hello", say_hello)
graph.add_edge(START, "hello")
graph.add_edge("hello", END)

app = graph.compile()
result = app.invoke({"message": ""})
print(result)
