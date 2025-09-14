import os
from dotenv import load_dotenv
load_dotenv()

# Langsmith Trcaking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']= 'true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI Assistsnt that gives accurate answers to everything."),
        ("user", "Question:{question}")

    ]
)

# Streamlit framework

st.title("Chat with Chatbot")
input_text = st.text_input("Plaease Enter your question?")

llm = Ollama(model = "gemma3:latest")

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


