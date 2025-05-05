from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.prompts import PromptTemplate
load_dotenv()

prompt = PromptTemplate(
    template="""You are a highly accurate assistant.
        Use ONLY the given context to answer the user's question.
        If the context does not contain the information needed, simply reply:
        "I don't know based on the given context."
        CONTEXT:
        {context}
        QUESTION:
        {question}
        Your Answer:""",
input_variables=["context", "question"])

path_to_vs = "./faiss/law"
def model():
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
embedding_model = model()
vector_store = FAISS.load_local(folder_path=path_to_vs,embeddings=embedding_model,allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever(search_kwargs={"k":3})


parser = StrOutputParser()
model = ChatGroq(model ="gemma2-9b-it",max_tokens=300)

multi_query = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=model,
    include_original=True,
)

def context_text(docs):
    context_text ="\n\n".join(doc.page_content for doc in docs)
    return context_text


parallel_chain = RunnableParallel({
    "context":multi_query | RunnableLambda(context_text),
    "question":RunnablePassthrough()

})

chain = parallel_chain |prompt | model | parser
query = input("enter query:")
response = chain.invoke(query)
print(response)

#power of president in pakistan