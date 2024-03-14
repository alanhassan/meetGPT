import streamlit as st

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.OpenAI()

st.header('Bem-vindo ao MeetGPT 🎙️')
tab_gravar, tab_selecao = st.tabs(['Gravar Reunião', 'Ver transcrições salvas'])