from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

def llm_conn():
    llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    groq_api_key = os.getenv('GROQ_API_KEY')
    )
    print('initiated')
    return llm