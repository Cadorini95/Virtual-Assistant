import os
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd
import pyodbc

load_dotenv()

# Ensure the pyodbc dependency is installed and available
# CONFIGURAÇÃO DE CONEXÃO COM O BANCO DE DADOS (USANDO VARIÁVEIS DE AMBIENTE)
SQL_SERVER = os.getenv('SERVER')
DATABASE   = os.getenv('DATABASE')
USERNAME   = os.getenv('USERNAME')
PASSWORD   = os.getenv('PASSWORD')

def get_conn_string():
    DRIVER = 'ODBC Driver 17 for SQL Server'
    params = urllib.parse.quote_plus(
        f"DRIVER={DRIVER};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        f"Connection Timeout=30;"
    )
    return f"mssql+pyodbc:///?odbc_connect={params}"
