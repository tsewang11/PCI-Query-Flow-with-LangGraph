from langgraph.graph import StateGraph, END
from langchain.schema import BaseMessage
from typing import TypedDict

# LangChain memory and logic
from app.memory import get_memory
from app.segmentation import segment_customer

# Mistral via Ollama
from langchain_community.chat_models import ChatOllama

# Define the expected data structure for the graph state
class State(TypedDict):
    query: str
    context: str
    segment: str
    response: str

# Initialize memory and LLM
memory = get_memory()
llm = ChatOllama(model="mistral")  # You can use "mistral:instruct" if pulled

# ---- Node 1: Capture query and retrieve memory context ----
def capture_query_node(state: dict) -> dict:
    query = state["query"]
    memory.chat_memory.add_user_message(query)
    context = memory.load_memory_variables({}).get("history", "")
    
    print("DEBUG: Query =", query)
    print("DEBUG: Memory Context =", context)

    return {"query": query, "context": context}

# ---- Node 2: Segment customer ----
def segmentation_node(state: dict) -> dict:
    return segment_customer(state)

# ---- Node 3: Generate AI-powered suggestion using Mistral ----
def suggestion_node(state: dict) -> dict:
    query = state["query"]
    segment = state["segment"]
    context = state["context"]

    prompt = f"""You are a helpful sales assistant.

The user is categorized as: {segment}
Conversation so far: {context}
Latest user query: {query}

Based on this, suggest a relevant product, offer, or assistance.
Keep it natural, helpful, and short.
"""

    response = llm.invoke(prompt)
    memory.chat_memory.add_ai_message(response.content)

    return {"response": response.content}

# ---- Define the state graph ----
def get_graph():
    workflow = StateGraph(State)

    workflow.add_node("capture_query", capture_query_node)
    workflow.add_node("segment", segmentation_node)
    workflow.add_node("suggest", suggestion_node)

    workflow.set_entry_point("capture_query")
    workflow.add_edge("capture_query", "segment")
    workflow.add_edge("segment", "suggest")
    workflow.add_edge("suggest", END)

    graph = workflow.compile()
    return graph
