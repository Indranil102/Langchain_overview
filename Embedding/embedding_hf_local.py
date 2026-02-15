from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

embedding= HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text="I am very much happy today"

result= embedding.embed_query(text)

print(result)