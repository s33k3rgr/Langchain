from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="You are an expert in social media content strategy."),
    HumanMessage(content="Give a short tip to create engaging posts on Instagram")
]

response = llm.invoke(messages)

print(response.content)
