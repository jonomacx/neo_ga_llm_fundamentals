from keys import openkey
from langchain.llms import OpenAI

llm = OpenAI(
openai_api_key=openkey,
#models need to use the completions models from here: https://platform.openai.com/docs/models/how-we-use-your-data
#model="gpt-4",
model="gpt-3.5-turbo-instruct",
#model="text-davinci-003",  
#model="text-embedding-ada-002",
temperature=0.2
)
