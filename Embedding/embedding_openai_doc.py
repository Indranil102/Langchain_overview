from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

document=["I am very Happy ",
          "I am alone",
          "I am very sad"]

result =embedding.embed_documents(document)

print(str(result))