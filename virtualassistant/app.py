import os
import streamlit as st
#from virtualassistant import settings, query_builder
from settings import *
from query_builder import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def app():
    st.header("Assistente virtual", divider=True)
    st.markdown("####  Consulte rapidamente os dados operacionais disponíveis")
    st.markdown("###### O objetivo deste assistente é fornecer respostas rápidas e precisas com base nos dados disponíveis no banco de dados.")

    if 'mensagens' not in st.session_state:
        st.session_state['mensagens'] = []

    def enviar_mensagem():
        user_input = st.session_state["input_usuario"]
        if user_input:
            st.session_state['mensagens'].append(HumanMessage(content=user_input))
            resposta = get_chat_model(user_input)
            st.session_state['mensagens'].append(AIMessage(content=resposta))
            st.session_state["input_usuario"] = ""  # Limpa o campo de texto

    # Exibe o histórico do chat
    st.markdown("#### Histórico do Chat")
    for mensagem in st.session_state['mensagens']:
        if isinstance(mensagem, HumanMessage):
            with st.chat_message("Usuário"):
                st.write(mensagem.content)
        elif isinstance(mensagem, AIMessage):
            with st.chat_message("Assistente"):
                st.write(mensagem.content)
        elif isinstance(mensagem, SystemMessage):
            with st.chat_message("Sistema"):
                st.write(mensagem.content)

    # Entrada do usuário com controle de estado e on_change
    st.text_input(
        "Digite sua mensagem para continuar a conversa:",
        key="input_usuario",
        on_change=enviar_mensagem
    )