
from llama_index import VectorStoreIndex,SimpleDirectoryReader
documents=SimpleDirectoryReader("data").load_data()

print(documents)