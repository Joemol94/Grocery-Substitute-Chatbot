import os

from llama_index.llms.groq import Groq
from llama_index.llms.gemini import Gemini
from llama_index.core.settings import Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.embeddings.gemini import GeminiEmbedding
from web_scraping import url_content_json
from dotenv import load_dotenv
import chromadb

load_dotenv()

db = chromadb.PersistentClient(".chromadb")
price_details = url_content_json()

Settings.llm = Gemini(api_key=os.environ['GEMINI_API_KEY'], model="models/gemini-1.5-flash")
# Settings.llm = Groq(model="llama-3.1-70b-versatile", api_key=os.environ['GROQ_API_KEY'])
Settings.embed_model = GeminiEmbedding(model_name="models/text-embedding-004", api_key=os.environ['GEMINI_API_KEY'])
collection = db.get_collection("substitutes_collection_try6")
store = ChromaVectorStore(chroma_collection=collection)
# context = StorageContext(vector_stores=store)
index = VectorStoreIndex.from_vector_store(store)

system_prompt = """
### You work as a grocery recommendation expert. I will provide you details regarding the item name, relevant item info and some scraped price details.
    1. User Query
    2. Context (if any)
    ### Instructions:
    1. Always Make the chat conversational.
    2. Only use the use the context if it's relevant to the user query otherwise feel to address the user quer based on your knowledge.
    3. The context will be only be provided if there is any.
    4. The following were applicable if and only if the user's query is related to an item
            a) Provide a brief summary of the user queried item name, its substitute available in german supermarket, its similarity score and other details.
            b) Mostly the price data will not be relevant to the item queried, in that case, provide a sensible price value.
            c) If the user queried item is not available in the shared data, provide a relevant substitute and other details based on you knowledge.
            d) DONOT MENTION data is not available, handle the situation like a pro.
            e) DONOT MENTION a vague answer like supermarket or organic store. Mention a valid german store like Lidl, aldi, penny.
            f) Have a natural conversation.
            g) Try to Respond like for your query item, the substitute available in german supermarket is xx and all important details are yy. The price detail is approximately zz and available in stores abc. Give the response in points. Also Highlight the substitute as it is main part of the response. Else you can have a natural conversation.
"""

base_prompt = """
    ----------Context---------
    Item name: {item_name}
    Additional info about the item: {item_details}
    Price data: {url_price_data}

    
    ---------User query--------
    {sample_user_query}
"""
messages = [ChatMessage(role=MessageRole.SYSTEM, content=system_prompt)]
retriever_engine = index.as_retriever(top_k=1)

print("You can start chatting now...")

while True:
    query = input("Q: ")
    if query == 'quit':
        break
    # print(f"Q: {query}")
    llm_prompt = base_prompt.replace("{sample_user_query}", query, 1)
    context = retriever_engine.retrieve(query)
    if len(context) > 0:
        con = context[0]
    llm_prompt = llm_prompt.replace("{item_name}", con.text if len(context) > 0 else "null", 1)
    llm_prompt = llm_prompt.replace("{item_details}", str(con.metadata) if len(context) > 0 else "null", 1)
    llm_prompt = llm_prompt.replace("{url_price_data}", str(price_details) if len(context) > 0 else "null", 1)
    messages.append(ChatMessage(role=MessageRole.USER, content=llm_prompt))
    res = Settings.llm.chat(messages=messages)
    print(f"A: {str(res)}\n")
    messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=str(res)))
