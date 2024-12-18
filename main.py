from agent import QueryAgent

def main():
    agent = QueryAgent()

    while True:
        query = input("Enter your query: ")
        if query.lower() in {"exit", "quit"}:
            print("Exiting...")
            break

        response = agent.handle_query(query)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()