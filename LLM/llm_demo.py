import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create the LLM instance using OpenRouter endpoint 
llm = ChatOpenAI(
    model="gpt-4o-mini",  
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE")
)

# Run a test query
result = llm.invoke("Tell me 5 Indian state name with their capital city.")
print(result.text)
