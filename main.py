import streamlit as st
import os

from utils.query_utils import load_db, query_chatbot
from utils.db_utils import add_data_to_db, data_to_db, add_uploaded_files_to_db, uploaded_files_to_db
from utils.streamlit_utils import cleanup_uploaded_files, db_error_check,rescan_projects, write_uploaded_files_to_disk, build_func, update_func,title_func, intro_func, chat_func , eval_func , query_func

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
# from langchain_community.retrievers import BM25Retriever
# from nltk.tokenize import word_tokenize
# from langchain.retrievers import EnsembleRetriever


#model = OllamaLLM(model="deepseek-r1:14b")

if "available_projects" not in st.session_state:
    rescan_projects(st.session_state)

title_func()

if "available_projects" not in st.session_state:
    st.session_state["available_projects"] = []
if "db_project" not in st.session_state:
    st.session_state["db_project"] = None
if "db_type" not in st.session_state:
    st.session_state["db_type"] = "Build new"

page_names_to_funcs = {
    "-": intro_func,
    "Build": build_func,
    "Update": update_func,
    "Evaluate": eval_func,
    # "Finetune": finetune_func,
     "Chat": chat_func
}
page_name = st.sidebar.selectbox("Choose a function", page_names_to_funcs.keys())
page_names_to_funcs[page_name]()