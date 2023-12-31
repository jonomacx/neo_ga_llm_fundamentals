from keys import openkey
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph



llm = ChatOpenAI(
    openai_api_key=openkey
)

graph = Neo4jGraph(
    url="bolt://54.174.85.163:7687",
    username="neo4j",
    password="rejections-gyroscopes-street",
)

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.

Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
For movie titles that begin with "The", move "the" to the end, For example "The 39 Steps" becomes "39 Steps, The" or "The Matrix" becomes "Matrix, The".

If no data is returned, do not attempt to answer the question.
Only respond to questions that require you to construct a Cypher statement.
Do not include any explanations or apologies in your responses.


Examples:

Find movies and years:
MATCH (m:Movie) WHERE m.released > 1990  RETURN m LIMIT 5

Schema: {schema}
Question: {question}
"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"],
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    cypher_prompt=cypher_generation_prompt,
    verbose=True
)

cypher_chain.run("What year was the film The Matrix released?")