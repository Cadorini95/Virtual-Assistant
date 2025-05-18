# VirtualAssistant

VirtualAssistant é uma aplicação web desenvolvida com [Streamlit](https://streamlit.io/) que permite consultas inteligentes a um banco de dados utilizando um modelo da OpenAI. A interação entre o modelo de IA e o banco de dados é estruturada com o uso do [LangChain](https://python.langchain.com/), proporcionando maior flexibilidade e robustez na interpretação e execução das consultas em linguagem natural.

## Funcionalidades

- Interface web intuitiva para interação com o usuário.
- Consulta ao banco de dados via linguagem natural, interpretada por modelo OpenAI.
- Configuração de variáveis sensíveis através de arquivo `.env`.
- Pronto para execução em containers Docker, facilitando o deploy e a portabilidade.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web em Python.
- **OpenAI API**: Processamento de linguagem natural para interpretar e responder consultas.
- **Docker & Docker Compose**: Gerenciamento de containers para ambiente isolado e replicável.
- **Python**: Linguagem principal do projeto.

## Como Executar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/VirtualAssistant.git
   cd VirtualAssistant
   ```

2. **Configure o arquivo `.env`** com as variáveis necessárias (exemplo: chaves de API, credenciais do banco de dados).  
   Exemplo de conteúdo para o arquivo `.env`:

   ```env
   OPENAI_API_KEY=sua-chave-openai-aqui
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=nome_do_banco
   ```

3. **Construa e execute os containers**:
   **Para rodar localmente (fora do Docker):**

```bash
poetry install
poetry run streamlit run virtualassistant/app.py
```

**Para rodar via Docker Compose:**

```bash
docker compose up --build
```

4. **Organização da pasta `virtualassistant/`**:

   ```
   virtualassistant/
   ├── app.py            # Interface principal da aplicação Streamlit
   ├── main.py           # Ponto de entrada do projeto
   ├── settings.py       # Configurações do schema do banco de dados
   ├── db_conn.py        # Módulo de conexão e operações com o banco de dados
   └── query_builder.py  # Construção e execução de queries a partir de linguagem natural
   ```

## Estrutura dos Arquivos

- `virtualassistant/`: Diretório contendo o código-fonte principal da aplicação.
- `docker-compose.yml`: Orquestração dos serviços Docker.
- `Dockerfile`: Instruções para build da imagem Docker.
- `pyproject.toml`: Configuração e dependências do projeto Python.
- `README.md`: Documentação do projeto.
- `.env`: Arquivo de variáveis de ambiente (não versionado no repositório).

## Observações

- Certifique-se de possuir uma chave de API válida da OpenAI.
- O arquivo `.env` **não** deve ser compartilhado publicamente.

## Licença

Este projeto está sob a licença MIT.
