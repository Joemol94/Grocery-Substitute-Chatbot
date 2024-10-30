
from langchain_community.document_loaders import WebBaseLoader
from llm_initialize import llm_conn
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

bonn_price_url = "https://www.numbeo.com/food-prices/in/Bonn"

def extract_url_content(bonn_price_url):
    loader = WebBaseLoader(web_paths=[bonn_price_url])
    page_data_raw = loader.load().pop().page_content
    return page_data_raw
#print(page_data_raw)

def preprocess_content(content):
    if content:  # Check if content is not None
        cleaned_content = ' '.join(content.split())
        return cleaned_content
    return None

def initail_prompt_json_extract():
    prompt_extract = PromptTemplate.from_template(
    """
    ### Below is the content of scraped info from a general site for general food prices or vegetable prices in germany.
    {page_data}
    ### Instruction:
    The scraped text is very messy.
    I want you to understand the content and map the product with the price and output the same as a JSON
    Please don't return python code only return the output as JSON. Also please return only valid JSON.
    ### Valid JSON (NO PREAMBLE) 

    """
)
    return prompt_extract

def json_content(cont):
    json_parser = JsonOutputParser()
    json_response = json_parser.parse(cont)
    json_response

def url_content_json():
    page_data_raw = extract_url_content(bonn_price_url)
    cleaned_data = preprocess_content(page_data_raw)
    #print(type(cleaned_data))
    llm = llm_conn()
    lang_chain = initail_prompt_json_extract() | llm
    res = lang_chain.invoke(input={'page_data':cleaned_data})
    #print(res.content)
    json_parser = JsonOutputParser()
    json_response = json_parser.parse(res.content)
    #print(json_response)
    return json_response

