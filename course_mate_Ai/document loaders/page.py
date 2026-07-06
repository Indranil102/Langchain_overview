from langchain_community.document_loaders import WebBaseLoader

#load the text file
data=WebBaseLoader("https://www.apple.com/in/macbook-air/")
docs=data.load()

print(docs) 