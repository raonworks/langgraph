from asyncio import graph
from typing import TypedDict
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

llm = ChatOllama(model="qwen3-coder:30b", base_url="http://localhost:11434", temperature=1)

prompt = PromptTemplate(
    template="너는 한국사람이고 모든 대답은 한국어로만 할 수 있어.\n, Question: {query}",
    input_variables=["query"],
)

class InputState(TypedDict):
    input: str

class OutputState(TypedDict):
    answer: str

class OverallState(InputState, OutputState):
    intermediate_data: str
    search_result: list[str]

class PrivateState(OverallState):
    API_KEY: str

# node 정의
def search_node(state: InputState) -> PrivateState:
    chain = prompt | llm
    result = chain.invoke({"query": state["input"]})

    return {
        "search_result": [result.content],
        "intermediate_data": f"{state['input']}에 대한 검색",
        "API_KEY": "sk-22112233445566"
    }

def answer_node(state: PrivateState) -> OutputState:
    print(state["API_KEY"])
    return {
        "answer": f"검색결과: '{state['input']}'에 대한 답변입니다. {state['search_result']}",
    }

graph = StateGraph(OverallState)

graph.add_node("search", search_node)
graph.add_node("answer", answer_node)

graph.add_edge(START, "search")
graph.add_edge("search", "answer")
graph.add_edge("answer", END)
app = graph.compile()

result = app.invoke({"input": "이별"})

print(result)
