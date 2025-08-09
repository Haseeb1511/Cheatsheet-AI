import streamlit as st
from chatbot.backend import app,retrieve_all_thread
from langchain_core.messages import HumanMessage
import uuid
#pip install langgraph-checkpoint-sqlite



#===============================================Session state==========================================================================

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

if "chat_thread" not in st.session_state:
    st.session_state["chat_thread"] = retrieve_all_thread()

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_titles" not in st.session_state:
    st.session_state["thread_titles"] = {}

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#================================================User Input=============================================================================
user_input = st.chat_input("Ask Anything")
CONFIG = {"configurable":{"thread_id":st.session_state["thread_id"]}}
#=================================================Utility Function=============================================================================
def add_thread(thread_id):
    if thread_id not in st.session_state["chat_thread"]:
        st.session_state["chat_thread"].append(thread_id)

def reset_chat():
    thread_id = str(uuid.uuid4())
    st.session_state["thread_id"] = thread_id
    add_thread(thread_id)
    st.session_state["message_history"] = []

def load_conversation(thread_id):
    state = app.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get("messages", [])

def set_thread_title(thread_id, first_message):
    preview = first_message.strip().split("\n")[0][:30]  # first line, max 30 chars
    st.session_state["thread_titles"][thread_id] = preview or "New Chat"



#=====================================================Sidebar==================================================================
add_thread(st.session_state["thread_id"])

st.sidebar.title("ChatBot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")
for thread_id in st.session_state["chat_thread"][::-1]:
    title = st.session_state["thread_titles"].get(thread_id, "New Chat")
    if st.sidebar.button(title, key=f"btn_{thread_id}"):
        st.session_state["thread_id"] = thread_id
        messages = load_conversation(thread_id)
        temp_messages = []
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = "user"
            else:
                role= "assistant"
            temp_messages.append({"role":role,"content":msg.content})
        
        st.session_state["message_history"] = temp_messages


#==================================================Main==================================================================================


if user_input:
    if not st.session_state["message_history"]:
        set_thread_title(st.session_state["thread_id"], user_input)

    with st.chat_message("user"):
        st.markdown(user_input)
        st.session_state["message_history"].append({"role":"user","content":user_input})


    with st.chat_message("assistant"):

        collected_chunk = []
        def stream_generator():
            for message_chunk,meta_data in app.stream(
            {"messages":[HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode="messages"):
                text_pieces = message_chunk.content
                collected_chunk.append(text_pieces)
                yield text_pieces

        st.write_stream(stream_generator())
        ai_response = "".join(collected_chunk)
        st.session_state["message_history"].append({"role":"assistant","content":ai_response})



