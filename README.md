## Praticando CRUD:

Criando um CRUD com interface usando flask e SQLite.
Praticando Jinja2 (Mecanismo de template usado pelo Flask).

https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application

## Estrutura:

```
python-sqlite-flask/
├── app/
│   ├── database/
│   │   ├── database.db
│   │   ├── init_db.py
│   │   └── schema.sql
│   ├── templates/
│   │   ├── base.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── index.html
│   ├── static/
│   │   └── styles.css
│   └── app.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```
- static e templates: Diretórios para arquivos estáticos e templates Jinja2, respectivamente.
- ``app.py``: O arquivo principal do seu aplicativo Flask.
- instance: Diretório onde seu arquivo de banco de dados app.db estará localizado.
- ``.dockerignore``: Arquivo para listar os arquivos e diretórios que não devem ser incluídos na imagem Docker.
- ``.gitignore``: Arquivo para listar os arquivos e diretórios que não devem ser incluídos no controle de versão.
- ``Dockerfile``: Arquivo de configuração para criar a imagem Docker.