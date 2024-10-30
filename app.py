import streamlit as st
from llm_initialize import llm_conn
from response_generator import substitute_response_generator
import chromadb
from web_scraping import url_content_json

# Initialize components at startup
@st.cache_resource
def initialize_components():
    # Initialize LLM
    llm = llm_conn()
    # Initialize ChromaDB
    client = chromadb.PersistentClient()
    collection = client.get_collection("substitutes_collection_try4")
    # Get price data
    price_data = url_content_json()
    # Create prompt template
    prompt_template = substitute_response_generator()
    
    return llm, collection, price_data, prompt_template

# Initialize components
llm, collection, price_data, prompt_template = initialize_components()

# Streamlit UI
st.title("German Grocery Substitute Finder")
st.write("Enter an ingredient to find its substitute in German stores")

# User input
user_query = st.text_input("What ingredient are you looking for?")

if user_query:
    # Get results from ChromaDB
    results = collection.query(query_texts=[user_query], n_results=1)
    item_name = results['documents']
    item_details = results['metadatas']
    
    # Create chain and get response
    lang_chain = prompt_template | llm
    with st.spinner('Finding substitutes...'):
        res = lang_chain.invoke({
            'sample_user_query': user_query,
            'item_name': item_name,
            'item_details': item_details,
            'url_price_data': price_data
        })
        
    # Display results
    st.write(res.content)