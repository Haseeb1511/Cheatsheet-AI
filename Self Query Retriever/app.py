from langchain_community.document_loaders import PyPDFDirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


file = PyPDFDirectoryLoader(
    path="./data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
document = file.load()

chunks = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=50).split(document)


vector_store = FAISS.from_documents(embedding=embedding_model , documents=chunks)
vector_store.save_local()