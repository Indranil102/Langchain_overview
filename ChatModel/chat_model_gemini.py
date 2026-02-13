
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm= ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.3)


result=llm.invoke("the prime miniser of India ?")

print(result.text)