from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini",)

#schema
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, either positive or negative"]
    
    
structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""The haradware is great, but the software is bloated. There is many pre-installed apps. that i can't remove. Also the ui look outdated comapred to other brands. Helping for the software update to fix this.  """)


print(result)