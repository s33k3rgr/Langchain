from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4")

chat_history = []

system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

#chat loop
while True:
    #get user input
    query = input("You: ")
    if query.lower() == "exit":
        break

    #add user message to chat history
    chat_history.append(HumanMessage(content=query))

    #get response from model
    result = model.invoke(chat_history)
    response = result.content

    #add AI message to chat history
    chat_history.append(AIMessage(content=response))

    #print response
    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)

