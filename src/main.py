import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

#os.environ['GOOGLE_API_KEY'] = "AIzaSyATcuvokUIUHuwVM6SGra6A5doyCf_Xrjo"
#llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0)
llm = ChatOllama(model="llama3:8b", base_url="http://172.16.0.130:11434", temperature=1)

# llm_answer = llm.invoke("오늘은 기분 나쁜 그놈을 또 보고 말았네, 나의 기분을 1줄로 응원해줘. 대답은 반드시 한국어로 해줘")
# llm_answer = llm.invoke("기분 좋은 시를 하나 만들어줘. 대답은 한국어로 해")

prompt = PromptTemplate(
    template="너는 한국사람이고 모든 대답은 한국어로만 할 수 있어, {query}",
    input_variables=["query"]
)

chain = prompt | llm

llm_answer = chain.invoke({"query": "blue는 칼라코드가 어떻게되지?"})

print("--- reply ---")
print(llm_answer.content)
