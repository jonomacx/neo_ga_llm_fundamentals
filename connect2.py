from connect import llm
import sys

#question = sys.argv[1]
#response = llm(question)
response = llm("how many days are in the week?")
print(response)

