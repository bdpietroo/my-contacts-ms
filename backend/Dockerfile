# Usa uma imagem oficial do Python como base.
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia o arquivo de dependências para o contêiner.
COPY requirements.txt requirements.txt

# Instala as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do código da sua aplicação para o contêiner.
COPY . .

# Expõe a porta que o Gunicorn (nosso servidor de produção) usará.
EXPOSE 8080

# O comando para iniciar a aplicação quando o contêiner for executado.
# Usamos Gunicorn, um servidor WSGI robusto para produção.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]