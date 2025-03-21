# import os
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
# openai_api_key = os.environ["OPENAI_API_KEY"]

# from langchain_openai import ChatOpenAI

# chatModel = ChatOpenAI(model="gpt-3.5-turbo-0125")

# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_template("tell me a curious fact about {politician}")

# chain = prompt | chatModel | StrOutputParser()

# response = chain.invoke({"politician": "JFK"})

# print("\n----------\n")

# print("Result from invoking the chain:")

# print("\n----------\n")
# print(response)

# print("\n----------\n")


import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
GROQ_API_KEY = os.environ["groq_api_key"]
from langchain_groq import ChatGroq;
chatModel = ChatGroq(model_name="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template("tell me a curious fact about {politician}")

chain = prompt | chatModel | StrOutputParser()

response = chain.invoke({"politician": "JFK"})

print("\n----------\n")

print("Result from invoking the chain:")

print("\n----------\n")
print(response)

print("\n----------\n")