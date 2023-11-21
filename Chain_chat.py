from keys import openkey
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import sys

chat_llm = ChatOpenAI(
    openai_api_key=openkey
)

#System - System messages instruct the LLM on how to act on human messages
instructions = SystemMessage(content="""
You are a surfer dude, having a conversation about the surf conditions on the beach.
Respond using surfer slang.
""")
prompt = sys.argv[1]
question = HumanMessage(content=prompt)

response = chat_llm([
    instructions,
    question
] )


#AI - Responses from the AI are called AI Responses
print(response)
print(response.content)
