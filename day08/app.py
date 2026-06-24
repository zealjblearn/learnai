import chromadb
from pprint import pprint

print(chromadb)

client = chromadb.PersistentClient("./chroma_db")
collection = client.get_or_create_collection("documents_notes")
print(collection)

# collection.add(documents=[
#         "Sachin Tendulkar is one of the greatest cricketers.",
#         "Virat Kohli is a modern cricket legend.",
#         "Python is a programming language."
#     ],
#     ids=["1","2","3"])

print(collection.count())

# result = collection.query(query_texts="Sachin")

# result = collection.query(query_texts="Sachin", n_results=1)
# pprint(result)

result = collection.query(query_texts="Who is the best cricket player", n_results=3)
pprint(result)