from langgraph.graph import StateGraph,START,END
from typing import Annotated,TypedDict
from langchain_core.messages import BaseMessage,SystemMessage,HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import sqlite3

class AgentState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

llm = llm = ChatOpenAI(model="gpt-4.1-nano",temperature=0)

def chatbot(state:AgentState):
    query = state['messages']
    model = llm.invoke(query)
    return{"messages":[model]}

graph = StateGraph(AgentState)

conn = sqlite3.connect(database="chat.db",check_same_thread=False)
memory = SqliteSaver(conn=conn)

graph.add_node("chatbot",chatbot)
graph.add_edge(START,"chatbot")
graph.add_edge("chatbot",END)
app = graph.compile(checkpointer=memory)

# config = {"configurable":{"thread_id":"1"}}

# for message_chunk,meta_data in app.stream(
#     {"messages":[HumanMessage(content="write a essay on allama iqbal in 500 word")]},
#     config=config,
#     stream_mode="messages"
#                     ): # it will return generator object
#     if message_chunk.content:
#         print(message_chunk.content,end=" ",flush=True)


def retrieve_all_thread():
    all_thread = set()
    for checkpoint in memory.list(None):
        all_thread.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_thread)