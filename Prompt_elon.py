from langchain.prompts import PromptTemplate
from connect import llm
import sys

template = PromptTemplate(template="""
You are an Elon Musk impersonator..
Your role is to assist your customer with their rocket ship and planetary needs.
Respond using an American accent.

Tell me about the following planet: {planet}
""", input_variables=["planet"])

prompt = sys.argv[1]
response = llm(template.format(planet=prompt))

print(response)
