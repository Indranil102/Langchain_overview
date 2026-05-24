from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1= PromptTemplate(
    template="Generate a detailed report on {topic}.",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Generate a 5 bullet points summary of the report on./n{text}",
    input_variables=["text"]
)

model= ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3

)
parser= StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({'topic':'summer season'})

print(result)

chain.get_graph().print_ascii()