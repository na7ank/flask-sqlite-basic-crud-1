
## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" width="50" height="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" width="50" height="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width="50" height="40"/>Praticando CRUD com flask, sqlite e docker:
Criando um CRUD com interface usando flask e SQLite.
Praticando Jinja2 (Mecanismo de template usado pelo Flask).

![Imagem 1](/imgs/screen-1.PNG)

![Imagem 2](/imgs/screen-2.PNG)


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
│   │   ├── about.html
│   │   └── index.html
│   ├── static/
│   │   ├── scroll-bars-styles.css
│   │   └── styles.css
│   └── app.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

### Diretórios:
- ``python-sqlite-flask/`` : Diretório raíz do projeto.
- ``app/`` : O arquivo principal ``app.py`` do seu aplicativo flask.
- ``static/``: Diretório para arquivos estáticos como folhas de estilos ou imagens.
- ``templates/``: Diretório para htmls que serão renderizados dinamicamente pelo **Jinja2** durante funcionamento do app.
- ``database/``: Contém o banco de dados sqlite e arquivos para configurações iniciais da base.

### Templates:
- ``base.html``: html principal 'pai' que o app renderiza. Os outros blocos herdam essa estrutura.
- ``index.html``: Bloco com o layout dos posts recuperados do banco de dados.
- ``about.html``: Bloco com um texto explicativo.
- ``edit.html``: Bloco responsável por editar ou deletar dados.

### Arquivos de Configuração e outros:
- ``.dockerignore``: Arquivo para listar os arquivos e diretórios que não devem ser incluídos na imagem Docker.
- ``.gitignore``: Arquivo para listar os arquivos e diretórios que não devem ser incluídos no controle de versão.
- ``.gitattributes``: Arquivo selecionar qual linguagem o repositório considera para mostrar a % de linguagens utilizadas.
- ``Dockerfile``: Arquivo de configuração para criar a imagem Docker.
- ``requirements.txt``: Módulos requisitos python para rodar o projeto.
- ``schema.sql``: SQL com querys iniciais para criar uma tabela por exemplo.
- ``init_db.py``: Script para executar as querys em ``schema.sql``.

## Criando o Container:

### Construindo a imagem Docker
- ``docker build -t meu-app-flask .``

### Rodando o container
- ``docker run -p 8501:8501 meu-app-flask``
