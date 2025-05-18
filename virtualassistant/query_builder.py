## Importar as bibliotecas necessárias
import settings
from   settings import *
from   dotenv import load_dotenv
from   db_conn  import get_conn_string
from   sqlalchemy import create_engine,text
import pandas as pd


from langchain.prompts import PromptTemplate
from langchain_openai  import ChatOpenAI    ## PADRÃO DE RESPOSTA --> AI MESSAGE 
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_community.utilities import SQLDatabase
from pydantic import BaseModel, Field       ## BIBLIOTECA PARA CRIAÇÃO DE CLASSES E VALIDAÇÃO DE DADOS

## Inicializando modelo OPENAI
def build_openai_model():
    """
    Função para inicializar o modelo OpenAI com as credenciais do ambiente.
    """
    load_dotenv()  ## Carregar as variáveis de ambiente do arquivo .env
    return ChatOpenAI(model="gpt-3.5-turbo")

def build_sql_json_chain(user_input, schema_info=settings.SCHEMA_INFO):
    parser = StrOutputParser(name="query_element_builder")  ## CRIAÇÃO DO OUTPUT PARSER
    #instructions = parser.get_format_instructions()
    template_contexto = PromptTemplate.from_template("Você é um assistente que gera queries SQL para o banco de dados SQL Server."
                                                     "Um usuário fez o seguinte questionamento: {user_input}.\n" 
                                                     "Baseado nas estrutura do banco de dados, você deve estrutura uma query eficiente e com a sintaxe correta"
                                                     "baseada nas informações disponíveis para o banco de dados: {schema_info}.\n" 
                                                     "Preciso que apenas a query seja retornada, sem explicações ou comentários adicionais." 
                                                     )
    #template_formato = PromptTemplate.from_template("Formato da resposta: {formato}", partial_variables={"formato": instructions})
    template_final   = (template_contexto)
    chain   =  template_final | build_openai_model() | parser  
    return chain.invoke({"schema_info": schema_info, 'user_input': user_input})
    
def get_sql_data(user_input):
    sql_query = build_sql_json_chain(user_input)
    engine = create_engine(get_conn_string(), fast_executemany=True)
    with engine.connect() as conn:
        result = pd.read_sql(text(sql_query), conn)
        conn.close()
    return result   

def get_chat_model(user_input):
    result = get_sql_data(user_input)  ## Executa a query SQL e retorna o resultado
    parser = StrOutputParser(name="query_processor")  ## CRIAÇÃO DO OUTPUT PARSER
    template_contexto = PromptTemplate.from_template("Você receberá como entrada o resultado de uma query SQL em formato de uma tabela: {result}."
                                                     "A resposta descritivo sobre o resultado da query, e abaixo esse resultado em formato de tabela." 
                                                     )
    template_final   = (template_contexto)
    chain  =  template_final | build_openai_model() | parser
    return chain.invoke({"result": result})
    

