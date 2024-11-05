# German Grocery Substitute Finder

This project is a conversational AI chatbot that helps users find German grocery substitutes for Indian ingredients. The chatbot uses a combination of machine learning and language processing models to provide accurate, culturally relevant grocery suggestions available in German supermarkets. The application leverages LangChain, ChromaDB, and a large language model (LLM) for contextual understanding and response generation, alongside web scraping for real-time price data.

## Features

- **Substitute Finder**: Finds German substitutes for Indian grocery items.
- **Contextual Response**: Uses a language model to provide detailed and conversational responses.
- **Real-Time Price Data**: Integrates live price data.
- **Interactive UI**: Built using Streamlit for easy access and interactivity.

## Tech Stack

- **LangChain**: For prompt management and response generation.
- **ChromaDB**: Manages and retrieves grocery item embeddings for similarity-based recommendations.
- **LLM**: Provides conversational responses and understanding of ingredient contexts.
- **Streamlit**: Creates the web interface for user interaction.
- **Web Scraping**: Scrapes live price data from German food price websites for accurate price approximations.

## Requirements

- Python
- Streamlit
- ChromaDB
- LangChain and LangChain Community Libraries
- Environment variables for API keys (e.g., `GEMINI_API_KEY`)
- Other dependencies as listed in `requirements.txt`

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/german-grocery-substitute-finder.git
   cd german-grocery-substitute-finder
   ```

2. **Install Dependencies**:
   Install the necessary libraries via `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file and add your API keys (e.g., `GEMINI_API_KEY`) for connecting to language models.
   
4. **Initialize ChromaDB Collection**:
   Ensure that the `substitutes_collection` in ChromaDB is populated with necessary grocery data before running the app.

## Project Structure

- **app.py**: Main Streamlit app where users interact with the chatbot.
- **app_bot.py**: Contains the chatbot logic, vector store index, and the LLM connection setup. Uses a system prompt to guide the chatbot responses.
- **web_scraping.py**: Responsible for web scraping and cleaning price data from price website. Converts the scraped data into a JSON format.
- **llm_initialize.py**: For initializing the LLM connection.
- **response_generator.py**: Methods for generating responses based on the user query.

## Usage

1. **Run the App**:
   Start the Streamlit app with:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the Chatbot**:
   - Enter the name of an Indian ingredient in the input box.
   - The chatbot will provide a German grocery substitute, along with contextual price data if available.
   - If no exact substitute is found, the chatbot will use its knowledge base to provide a suitable alternative.

## Prompt Structure

The bot is guided by structured prompts to ensure responses are relevant and conversational. Key sections in `app_bot.py`:

- **System Prompt**: Sets rules for making responses conversational, accurate, and to avoid vague answers.
- **Base Prompt**: Structured template for presenting context and user queries, helping the LLM generate informative answers.

## Notes

- This app is tailored to provide recommendations based on a mix of scraped price data and the LLM's internal knowledge.
