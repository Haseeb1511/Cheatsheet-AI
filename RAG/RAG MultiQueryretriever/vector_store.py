from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

#--------------------------------------pdf load--------------------------------------------------
path= "data/law.pdf"
def got_loader(path):
    loader = PyPDFLoader(path)
    return loader.load()
doc_loader = got_loader(path)


def text_splitter(doc):
    splitter = RecursiveCharacterTextSplitter(chunk_size=900,chunk_overlap=100)
    return splitter.split_documents(doc)
got_chunks = text_splitter(doc_loader)
print("chunks created")


path_to_vs = "./faiss/law"
def model():
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
embedding_model = model()
vector_store = FAISS.from_documents(documents=got_chunks,
                                    embedding = embedding_model)
vector_store.save_local(path_to_vs)
                                