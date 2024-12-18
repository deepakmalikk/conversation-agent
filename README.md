# conversation-agent with Contextual Memory

This project features an AI-powered **Query-Response Agent** that remembers previous user interactions and generates context-aware responses. Built using the **Gemini LLM** for natural language processing and **FAISS** for semantic search, the agent can recall related queries and provide accurate, meaningful answers over time. The agent stores conversation history in a JSON file, allowing it to maintain context and improve responses as more queries are added.

## Key Features
- **Contextual Memory**: The agent remembers past queries and responses to create more relevant and context-aware answers.
- **FAISS Integration**: Implements FAISS to store and retrieve related queries for better search results and context.
- **Dynamic Query Handling**: As new queries come in, the agent combines them with previous interactions to enhance its responses.
- **Gemini LLM for Response Generation**: The agent uses the Gemini LLM model to generate accurate and human-like responses based on past conversations.
- **Persistent History**: Conversation history is saved and loaded from a JSON file, making the agent capable of resuming conversations after a restart.

## Technologies Used
- **Python**
- **Gemini LLM** (for natural language processing)
- **FAISS** (for semantic search)
- **PydanticAI** (for building the agent framework)
- **JSON** (for conversation history storage)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/deepakmalikk/conversation-agent.git
    cd conversation-agent
    ```

2. Create a virtual environment and activate it:

    - **For macOS/Linux**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - **For Windows**:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Gemini API key:

    ```plaintext
    GEMINI_API_KEY=your-gemini-api-key
    ```

## Usage

1. Run the agent script:

    ```bash
    python main.py
    ```

2. To interact with the agent, you can call the `handle_query` method. For example:

    ```python
    agent = QueryAgent()
    response = agent.handle_query("What is the capital of France?")
    print(response)
    ```

## Deployment

You can deploy the agent to your preferred platform (e.g., **Heroku**, **AWS**, **Google Cloud**, etc.) by following standard deployment procedures for FastAPI applications.

### Example Deployment (Heroku)

1. Create a `Procfile`:

    ```plaintext
    web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
    ```

2. Push to Heroku:

    ```bash
    heroku create
    git push heroku master
    heroku open
    ```

## Contributing

If you'd like to contribute to this project, feel free to fork it and submit pull requests. Please ensure that your code follows the existing style and includes proper tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
