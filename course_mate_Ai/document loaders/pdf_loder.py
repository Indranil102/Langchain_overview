from langchain_community.document_loaders import PyPDFLoader

#load the text file
data=PyPDFLoader("GRU.pdf")
docs=data.load()

print(len(docs)) 