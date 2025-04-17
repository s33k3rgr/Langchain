from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

response = llm.invoke("What is the capital of France?")

print(response.content)
