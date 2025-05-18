# Esquema do banco de dados
SCHEMA_INFO = """
    Estrutura do banco de dados:
    Tabela: PLANTS
        - plant_id (INTEGER)    : ID único da planta
        - plant_name (NVARCHAR) : Nome da planta
        - manager (NVARCHAR)    : Nome do gerente
        - region (NVARCHAR)     : Região da planta

    Tabela: PLANT_CONSUMPTION
        - plant_id (INTEGER) : ID da planta (chave estrangeira para PLANTS)
        - datetime (DATETIME): Data e hora do registro
        - consumption (FLOAT): Consumo registrado
    """