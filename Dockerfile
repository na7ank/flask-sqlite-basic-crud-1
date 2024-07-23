# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o container
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o diretório da aplicação para o container
COPY app/ app/

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app/app.py

# Exponha a porta que o Flask usará
EXPOSE 8501

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8501"]
