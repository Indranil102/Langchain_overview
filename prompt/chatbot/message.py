from langchain_core.messages import ChatMessage, HumanMessage, SystemMessage, AIMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini",)
#input thhat i sent to llm 
messages=[
    SystemMessage(content="You are a helpful assistant "),
    HumanMessage(content="tell me about the India"),
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)