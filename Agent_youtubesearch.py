from keys import openkey
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool, YouTubeSearchTool

youtube = YouTubeSearchTool()

#set the connection
llm = ChatOpenAI(
    openai_api_key=openkey
)

#set context of prompt
prompt = PromptTemplate(
    template="""
    You are a movie expert. You find movies from a genre or plot.

    ChatHistory:{chat_history}
    Question:{input}
    """,
    input_variables=["chat_history", "input"]
    )

#create a conversation history which holds context of previous questions in chat
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

#create a chain
chat_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

#create a tool that uses the chain
tools = [
    Tool.from_function(
        name="YouTubeSearchTool",
        description="For when you need a link to a movie trailer. The question will be a string. Return a link to a YouTube video.",
        func=youtube.run,
        return_direct=True
    ),
    Tool.from_function(
        name="ChatOpenAI",
        description="For when you need to chat about movies. The question will be a string. Return a string.",
        func=chat_chain.run,
        return_direct=True
    )
]

#initialize an agent to use the tool
#ReAct - Reasoning and Acting Agent Type
agent = initialize_agent(
    tools, llm, memory=memory,
    max_iterations=3,  #maximum number of iterations to run the LLM for. This is useful in preventing the LLM from running for too long or entering an infinite loop.
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True, #the agent will print out the LLM output and the tool output.
    handle_parsing_errors=True, # the agent will handle parsing errors and return a message to the user.
)

while True:
    q = input(">")
    print(agent.run(q))