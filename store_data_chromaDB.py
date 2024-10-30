import json
import os
import chromadb
import chromadb.utils
import chromadb.utils.embedding_functions
import chromadb.utils.embedding_functions.google_embedding_function
import pandas as pd
import uuid
from dotenv import load_dotenv

load_dotenv()

with open('master_data.json', 'r') as file:
    data = json.load(file)
df = pd.DataFrame(data['substitutes'])
embed_fn = chromadb.utils.embedding_functions.google_embedding_function.GoogleGenerativeAiEmbeddingFunction(api_key=os.environ['GEMINI_API_KEY'])
client = chromadb.PersistentClient(".chromadb")
collection_name = "substitutes_collection_try6"
collection = client.get_or_create_collection(collection_name, embedding_function=embed_fn)

if not collection.count():
    for _,row in df.iterrows():
        documents = [
            #str(row),
            str(row['item'])
            # str(row['substitute']),
            # str(row['category']),
            # str(row['similarity_score']),
            # str(row['culinary_use']),
            # str(row['store']),
            # str(row['dietary_constraints'])
        ]
        collection.add(
            documents = documents,
            metadatas= {#"item": row["item"],
                        "substitute": row["substitute"],
                        "category": str(row['category']),
                        "similarity_score":str(row['similarity_score']),
                        "culinary_use":str(row['culinary_use']),
                        "store":str(row['store']),
                        "dietary_constraints":str(row['category'])},
            ids = [str(uuid.uuid4()) for _ in range(len(documents))]
        )

# new_data = url_content_json()
# for items in new_data['Food Prices in Bonn'].items():
#     #print(items)
#     metadatas={"prices": items}
