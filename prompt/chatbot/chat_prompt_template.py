from langchain_core.prompts import ChatPromptTemplate



chatTemplate= ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant "),
    ("human", "Explain the topic {question}"),
])

prompt= chatTemplate.invoke({
    "domain":"AI",
    "question":"deep learning?"})

print(prompt)