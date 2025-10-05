from dotenv import load_dotenv
load_dotenv()
from prompts import *
from states import *
from langchain_groq import ChatGroq

llm = ChatGroq(model ="openai/gpt-oss-120b")

user_prompt = ""

prompt = planner_prompt(user_prompt)

res = llm.with_structured_output(Plan).invoke("Who is the current peime minister of India. only provide the name")
print(res.content)