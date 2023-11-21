from connect import llm
import sys

question = sys.argv[1]

response = llm(question)

print(response)

