from keys import openkey
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.neo4j_vector import Neo4jVector

embedding_provider = OpenAIEmbeddings(openai_api_key=openkey)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://52.90.176.41:7687",
    username="neo4j",
    password="age-speeches-gross",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

r = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.",k=1) #k = number of docs to be returned
print(r)