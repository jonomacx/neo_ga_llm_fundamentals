from keys import openkey

from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import RetrievalQA

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.neo4j_vector import Neo4jVector


OPENAI_API_KEY = openkey

chat_llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

embedding_provider = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://54.174.85.163:7687",
    username="neo4j",
    password="rejections-gyroscopes-street",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

retrievalQA = RetrievalQA.from_llm(
    llm=chat_llm,
    retriever=movie_plot_vector.as_retriever(),
    verbose=True,
    return_source_documents=True
    #output_parser=SimpleJsonOutputParser()
)

r = retrievalQA("A mission to the moon goes wrong")
print(r)
#parser = SimpleJsonOutputParser()
#parser.invoke(r)