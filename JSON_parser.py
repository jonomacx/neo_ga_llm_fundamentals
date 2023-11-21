from connect import llm
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser
from langchain.output_parsers.json import SimpleJsonOutputParser


template = PromptTemplate.from_template("""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Always output JSON.

Tell me about the following fruit: {fruit}
""")


llm_chain = LLMChain(
    llm=llm,
    prompt=template,
#    output_parser=StrOutputParser()
    output_parser=SimpleJsonOutputParser()
)


response = llm_chain.run(fruit="apple")

print(response)
