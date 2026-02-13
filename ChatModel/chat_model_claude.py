from unittest import result
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm= ChatAnthropic(
    model="claude-2",
    temperature=0.3,)

result=llm.invoke("How many planet in the solor system?")

print(result.content)