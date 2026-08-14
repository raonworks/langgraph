import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import Field, BaseModel

#os.environ['GOOGLE_API_KEY'] = "AIzaSyATcuvokUIUHuwVM6SGra6A5doyCf_Xrjo"
#llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0)
llm = ChatOllama(model="llama3:8b", base_url="http://172.16.0.130:11434", temperature=1)

# llm_answer = llm.invoke("오늘은 기분 나쁜 그놈을 또 보고 말았네, 나의 기분을 1줄로 응원해줘. 대답은 반드시 한국어로 해줘")
# llm_answer = llm.invoke("기분 좋은 시를 하나 만들어줘. 대답은 한국어로 해")

class ExamParser(BaseModel):
    answer: str = Field(description="the answer of the question")
    question_rank: str = Field(description="rank of the question, low is 1, high 5")

parser = JsonOutputParser(pydantic_object = ExamParser)

prompt = PromptTemplate(
    template="너는 한국사람이고 모든 대답은 한국어로만 할 수 있어.\n answer 필드는 반드시 5줄 이상이어야 하고, 줄바꿈은 \\n으로 표현해. \n {format_instructions} \n, Question: {query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

llm_answer = chain.invoke({"query": "시를 하나 써줘"})

print("--- reply ---")
print(llm_answer)
