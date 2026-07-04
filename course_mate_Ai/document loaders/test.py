from langchain_community.document_loaders import TextLoader

#load the text file
data=TextLoader("notes.txt")
docs=data.load()

print(docs) 