from keys import openkey
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.neo4j_vector import Neo4jVector

embedding_provider = OpenAIEmbeddings(openai_api_key=openkey)

documents = ["Text to be indexed"]

new_vector = Neo4jVector.from_documents(
    documents,
    embedding_provider,
    url="bolt://localhost:7687",
    username="neo4j",
    password="pleaseletmein",
    index_name="myVectorIndex",
    node_label="Chunk",
    text_node_property="text",
    embedding_node_property="embedding",
    create_id_index=True,
)