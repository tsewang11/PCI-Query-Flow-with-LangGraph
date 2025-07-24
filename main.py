from app.workflow import get_graph

if __name__ == "__main__":
    graph = get_graph()
    
    print("Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        result = graph.invoke({"query": query})
        print("Bot:", result.get("response"))
