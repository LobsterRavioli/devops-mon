#!/bin/bash

# Ferma e rimuove tutti i container esistenti
docker-compose down

# Costruisce le immagini Docker
docker-compose build

# Avvia i container in background
docker-compose up -d

# Attende alcuni secondi per assicurarsi che il database sia pronto
sleep 10

# Esegue le migrazioni e popola il database
docker-compose exec web python manage.py migrate
docker-compose exec web python populate_db.py

# Riavvia i container per applicare tutte le modifiche
docker-compose restart
