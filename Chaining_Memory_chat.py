from keys import openkey
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferMemory

chat_llm = ChatOpenAI(
    openai_api_key=openkey
)

prompt = PromptTemplate(template="""You are a surfer dude, having a conversation about the surf conditions on the beach.
Respond using surfer slang.
Chat History: {chat_history}
Context: {context}
Question: {question}
""", input_variables=["chat_history", "context", "question"])

memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", return_messages=True)

#create the chain
chat_chain = LLMChain(llm=chat_llm, prompt=prompt, memory=memory, verbose=True)

current_weather = """
    {
        "surf": [
            {"beach": "Fistral", "conditions": "6ft waves and offshore winds"},
            {"beach": "Polzeath", "conditions": "Flat and calm"},
            {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"}
        ]
    }"""


#and then start asking questions with context
#response = chat_chain.run(
#    context=current_weather,
#    question="I am at Watergate Bay. What is the surf like?"
#)
#print(response)

#response = chat_chain.run(context=current_weather, question="Where I am?")
#print(response)


while True:
    question = input(">")
    response = chat_chain.run(context=current_weather, question=question)
    print(response)