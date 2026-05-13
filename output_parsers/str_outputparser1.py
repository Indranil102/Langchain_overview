from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

endpoints= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    task="text-generation",
)

model= ChatHuggingFace(llm=endpoints)
# 1 st prompt -> detailed report
template1= PromptTemplate(
    template='Write a details report on{topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary of the report
template2= PromptTemplate(
    template='Write a 5 line summary of the report on./n{text}',
    input_variables=['text']
)

parser= StrOutputParser()
chain= template1| model| parser | template2 | model| parser 

result=chain.invoke({'topic':'Solar system'})
print(result)