from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
propmt = PromptTemplate(
    template="Generate five interesting facts about {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
    
)

parser= StrOutputParser()

chain= propmt | model | parser 

result=chain.invoke({'topic':'Python programming'})
print(result)