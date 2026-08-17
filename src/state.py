from operator import add
from typing import Annotated, TypedDict
from langgraph.graph import START, END, StateGraph


class BasicState(TypedDict):
    current_step: str
    user_id: str
    response: str
    messages: Annotated[list[str], add]

state: BasicState = {"current_step": "시작", "user_id": "12345678", "messages": []}

def node1(state):
    return {"current_step": "node1 실행됨", "messages": ["안녕하세요, node1에서 메시지를 추가했습니다."]}

def node2(state):
    return {"user_id": "87654321", "messages": ["node2에서 새로운 메시지를 추가했습니다."]}

def node3(state: BasicState) -> dict:
    response = f"'{state['user_id']}'에 대한 답변입니다."
    return {"response": response, "messages": [f"User: {state['user_id']}", f"ai: {response}"]}

graph = StateGraph(BasicState)
graph.add_node("step1", node1)
graph.add_node("step2", node2)
graph.add_node("step3", node3)

graph.add_edge(START, "step1")
graph.add_edge("step1", "step2")
graph.add_edge("step2", "step3")
graph.add_edge("step3", END)

app = graph.compile()
result = app.invoke({"current_step": "", "user_id": "12345678", "response": "", "messages": []})

print(result)
