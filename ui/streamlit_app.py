


import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.workflow import get_graph
from app.memory import get_memory




# Initialize
graph = get_graph()
memory = get_memory()

st.set_page_config(page_title="PCI Query Flow", layout="centered")

st.title("🧠 PCI Query Flow with LangGraph")
st.markdown("Ask something like:\n- _I want to buy a phone_\n- _Any discount available?_")

# Display chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input field
query = st.chat_input("Type your query here...")

if query:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Run through graph
    result = graph.invoke({"query": query})
    response = result.get("response")

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
