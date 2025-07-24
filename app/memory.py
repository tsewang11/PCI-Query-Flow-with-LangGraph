from langchain.memory import ConversationBufferMemory

# Returns a reusable memory object
def get_memory():
    return ConversationBufferMemory(return_messages=True)
