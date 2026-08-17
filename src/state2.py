from asyncio import graph
from typing import TypedDict
from langgraph.graph import END, START, StateGraph

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
    return {
        "search_result": ["결과1", "결과2", "결과3"],
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
