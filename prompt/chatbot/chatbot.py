from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini",)


chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input== 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("Bot:", result.content)
    
print("Chat history:", chat_history)