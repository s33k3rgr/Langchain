from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)


# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the chain using RunnableSequence
chain = RunnableSequence(first = format_prompt,  middle = [invoke_model], last = parse_output)
# or we can use the pipe operator
# chain = format_prompt | invoke_model | parse_output

# run the chain
result = chain.invoke({"animal": "cat", "count": 2})

print(result)
