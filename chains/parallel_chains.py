from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
from langchain_core.runnables import RunnableParallel

model1= ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3

)
model2= ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.3)

prompt1= PromptTemplate(
    template="generate short and simple notes deom te folloeinh text \n {text}",
    input_variables=["text"]
)
prompt2= PromptTemplate(
    template="generate a 5 short question answer from the following text./n{text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="""
Merge the provided notes and quiz into a single document.

Notes:
{notes}

Quiz:
{quiz}
""",
    input_variables=["notes", "quiz"]
)

parser= StrOutputParser()

# develop chain into 2 part look at the img in notes

parallel_chain= RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})


merge_chain= prompt3 | model2 | parser

chain= parallel_chain | merge_chain


text= """The solar system is a collection of celestial bodies that orbit around the Sun. It consists of eight planets, including Earth, as well as dwarf planets, moons, asteroids, and comets. The planets are divided into two categories: the inner rocky planets (Mercury, Venus, Earth, Mars) and the outer gas giants (Jupiter, Saturn, Uranus, Neptune). The solar system also contains the asteroid belt between Mars and Jupiter, which is home to numerous rocky objects. The Sun is the central star of the solar system and provides the necessary energy for life on Earth. The solar system formed about 4.6 billion years ago from a giant cloud of gas and dust."""
result=chain.invoke({'text':text})


print(result)