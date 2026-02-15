from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm= ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
    
)

result=llm.invoke("Give me the story of the valentine day")

print(result.content)