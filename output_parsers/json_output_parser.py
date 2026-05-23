from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

endpoints= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    task="text-generation",
)
parser= JsonOutputParser()
model= ChatHuggingFace(llm=endpoints)
# 1 st prompt -> detailed report
template1= PromptTemplate(
    template='Give me the name, age and city of a ficitonal pereson \n {format_instructions}',
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain= template1| model| parser
final_result=chain.invoke({})
print(final_result)
print(type(final_result))
# 2nd prompt -> summary of the report


