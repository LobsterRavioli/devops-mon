# Dockerfile

# Usa una immagine di base con Python e Django già configurati
FROM python:3.12

# Imposta le variabili d'ambiente necessarie per Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=pokedex_app.settings

# Crea una directory per il codice sorgente Django
RUN mkdir /code
WORKDIR /code

# Copia il file requirements.txt e installa le dipendenze
RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install Django

# Copia il resto del codice del progetto nella directory /code/ del container
COPY . /code/



# Esponi la porta 8000 per il server Django (se necessario)
EXPOSE 8000

# Comando di default per avviare il server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


