from sentence_transformers import CrossEncoder
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI  # or any HuggingFace, Cohere, etc.

# Load a cross-encoder model fine-tuned for relevance
re_ranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Assume you already have FAISS vectorstore built with your docs
vectorstore = FAISS.load_local("your_faiss_index", embedding_model)

retriever = vectorstore.as_retriever(search_kwargs={"k": 20})  # fetch top 20 for re-ranking


def cross_encoder_rerank(query, docs, top_n=5):
    passages = [doc.page_content for doc in docs]
    pairs = [[query, passage] for passage in passages]
    
    scores = re_ranker.predict(pairs)
    # Sort docs based on score
    ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
    return [doc for score, doc in ranked[:top_n]]


llm = OpenAI(temperature=0)

# Wrap in a function to insert re-ranking before generation
def custom_retrieval_qa_chain(query):
    initial_docs = retriever.get_relevant_documents(query)
    reranked_docs = cross_encoder_rerank(query, initial_docs)
    
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain.run(input_documents=reranked_docs, query=query)

response = custom_retrieval_qa_chain("What is quantum computing?")
print(response)
