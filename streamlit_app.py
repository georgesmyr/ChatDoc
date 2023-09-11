import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

# Set OpenAI API key
openai.api_key = st.secrets.openai_key
st.header("Chat with the docs.")


