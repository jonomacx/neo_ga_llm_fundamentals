from langchain.prompts import PromptTemplate
from connect import llm
import sys

template = PromptTemplate(template="""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Tell me about the following fruit: {fruit}
""", input_variables=["fruit"])

prompt = sys.argv[1]
response = llm(template.format(fruit=prompt))

print(response)
