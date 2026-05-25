from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser
)

from langchain_core.runnables import (
    RunnableParallel,
    RunnableBranch,
    RunnableLambda
)

from pydantic import BaseModel, Field
from typing import Literal


# ---------------- MODELS ---------------- #

model1 = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


# ---------------- PARSERS ---------------- #

parser = StrOutputParser()


# ---------------- PYDANTIC SCHEMA ---------------- #

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative", "mixed"] = Field(
        description="The sentiment of the feedback text"
    )


parser2 = PydanticOutputParser(
    pydantic_object=Feedback
)


# ---------------- CLASSIFICATION PROMPT ---------------- #

prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback text.

Feedback:
{feedback}

{formatted_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "formatted_instructions": parser2.get_format_instructions()
    }
)


# ---------------- CLASSIFIER CHAIN ---------------- #

classifier_chain = prompt1 | model1 | parser2


# ---------------- RESPONSE PROMPTS ---------------- #

prompt2 = PromptTemplate(
    template="""
Write an appropriate professional response 
to the following positive feedback:

{feedback}
""",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="""
Write an empathetic and professional response 
to the following negative feedback:

{feedback}
""",
    input_variables=["feedback"]
)

prompt4 = PromptTemplate(
    template="""
Write a balanced response to the following mixed feedback:

{feedback}
""",
    input_variables=["feedback"]
)


# ---------------- BRANCH CHAIN ---------------- #

branch_chain = RunnableBranch(

    # POSITIVE
    (
        lambda x: x["sentiment"].sentiment == "positive",

        RunnableLambda(
            lambda x: {"feedback": x["feedback"]}
        )
        | prompt2
        | model1
        | parser
    ),

    # NEGATIVE
    (
        lambda x: x["sentiment"].sentiment == "negative",

        RunnableLambda(
            lambda x: {"feedback": x["feedback"]}
        )
        | prompt3
        | model1
        | parser
    ),

    # MIXED
    (
        lambda x: x["sentiment"].sentiment == "mixed",

        RunnableLambda(
            lambda x: {"feedback": x["feedback"]}
        )
        | prompt4
        | model1
        | parser
    ),

    # DEFAULT
    RunnableLambda(
        lambda x: "Could not classify sentiment"
    )
)


# ---------------- MAIN CHAIN ---------------- #

chain = RunnableParallel({

    # Preserve original feedback
    "feedback": RunnableLambda(
        lambda x: x["feedback"]
    ),

    # Generate sentiment classification
    "sentiment": classifier_chain

}) | branch_chain


# ---------------- INPUT ---------------- #

result = chain.invoke({
    "feedback": "I love the design of this phone, but the battery drains too quickly."
})


# ---------------- OUTPUT ---------------- #

print("\nFINAL RESPONSE:\n")
print(result)


# ---------------- GRAPH ---------------- #

print("\nCHAIN GRAPH:\n")

chain.get_graph().print_ascii()