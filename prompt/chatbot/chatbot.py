from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 
from langchain_core.messages import ChatMessage, HumanMessage, SystemMessage, AIMessage

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini",)


chat_history = [ SystemMessage(content="You are a helpful assistant") ]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input== 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Bot:", result.content)
    
print("Chat history:", chat_history)