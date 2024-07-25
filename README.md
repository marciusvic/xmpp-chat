## Como rodar no Windows
1. Instale o Python 3
2. Instale o Ejjaberd no Docker Desktop `docker pull ejabberd/ecs` 
3. Desabilite o TLS nas configuracoes do Ejabberd:
- `docker exec -it ejabberd /bin/sh`
- `cd conf`
- `vi ejabberd.yml`
- Sete `starttls_required: false`
- `ejabberdctl restart`
4. Entre na venv e instale as dependências `pip install -r requirements.txt`
5. Rode o arquivo `chat.py` com o comando `python chat.py`