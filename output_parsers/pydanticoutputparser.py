from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# HuggingFace endpoint
endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    task="text-generation",
)

model = ChatHuggingFace(llm=endpoint)

# Define schema
class PersonFacts(BaseModel):
    fact_1: str = Field(description="A fact about the person")
    fact_2: str = Field(description="Another fact about the person")
    fact_3: str = Field(description="Another fact about the person")

# Parser
parser = PydanticOutputParser(pydantic_object=PersonFacts)

# Prompt
template = PromptTemplate(
    template="""
Give me three facts about a fictional person.

{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

prompt = template.invoke({})

# Generate response
result = model.invoke(prompt)

# Parse result
final_result = parser.parse(result.content)

print(final_result)