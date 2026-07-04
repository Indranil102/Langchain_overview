from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate



load_dotenv()

data=TextLoader("./document loaders/notes.txt").load()

template=chat_prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that can answer questions about the text."),
    ("human","{data}"),
])
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

prompt = template.format_messages(data=data[0].page_content)

result=llm.invoke(prompt)
print(result.content)

