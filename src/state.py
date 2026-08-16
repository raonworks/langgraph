from operator import add
from typing import TypedDict


class BasicState(TypedDict):
    current_step: str
    user_id: str

state: BasicState = {"current_step": "시작", "user_id": "12345678"}

result = add([1,2], [3,4])
print(result)