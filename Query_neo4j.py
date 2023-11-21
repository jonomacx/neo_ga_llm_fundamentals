from langchain.graphs import Neo4jGraph

#graph = Neo4jGraph(
#    url="bolt://3.93.219.226:7687",
#    username="neo4j",
#    password="ticks-sex-fields"
#)

graph = Neo4jGraph(
    url="bolt://51.255.39.248:7687",
    username="neo4j",
    password="4oeNj0n0!e"
)


r = graph.query("MATCH (n:Role) RETURN n LIMIT 25")
print(r)

graph.refresh_schema()   #the object loads the database schema into memory - this enables Langchain to access the schema information without having to query the database.
print(graph.schema)