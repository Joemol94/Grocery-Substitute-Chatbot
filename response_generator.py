#from llm_initialize import llm_conn
from langchain_core.prompts import PromptTemplate
import chromadb
#from web_scraping import url_content_json

# client = chromadb.PersistentClient()
# collection_name = "substitutes_collection_try4"
# collection = client.get_collection(collection_name)

# # Example query
# sample_user_query = "what is the substitute item for cumin powder in german stores?"
# results = collection.query(query_texts=[sample_user_query], n_results=1)
# item_name = results['documents']
# item_details = results['metadatas']
# url_price_data = url_content_json()


def substitute_response_generator():
    prompt_extract = PromptTemplate.from_template(
    """
    ### You work as a grocery recommendation expert. I will provide you details regarding the item name, relevant item info and some scraped price details.
    1. {sample_user_query}
    2. {item_name}
    3. {item_details}
    4. {url_price_data}
    ### Instruction:
    Provide a brief summary of the user queried item name, its substitue available in german supermarket, its similarity score and other details.
    Mostly the price data will not be relevant to the item queried, in that case, provide a sensible price value.
    If the user queried item is not available in the shared data, provide a relevant substitute and other details.
    DONOT MENTION data is not available, just mention approximately.
    DONOT REPEAT Information.
    DONOT MENTION a wage answer like supermarket or organic store. Mention a valid german store like Lidl,aldi, penny.
    ### Output:
    Respond like for your query item, the substitute available in german supermarket is xx and all important details are yy. The price detail is approximately zz and available in stores abc. 
    Give the response in points. Also Highlight the substitute as it is main part of the response.
    """
)
    return prompt_extract

# llm = llm_conn()
# lang_chain = substitute_response_generator() | llm
# res = lang_chain.invoke(input={'sample_user_query':sample_user_query,'item_name':item_name,'item_details':item_details,'url_price_data':url_price_data})
# print(res.content)




