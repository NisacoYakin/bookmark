#!/bin/bash
# scripts/backup_db.sh
# Sauvegarde la base PostgreSQL pour l'environnement actif

ENV=${ENV:-dev}  # default dev
DB_URL_VAR="DATABASE_URL_$(echo $ENV | tr '[:lower:]' '[:upper:]')"
DB_URL=$(eval echo "\$$DB_URL_VAR")

if [ -z "$DB_URL" ]; then
    echo "[ERROR] La variable $DB_URL_VAR n'est pas définie."
    exit 1
fi

# Extraire info depuis URL (user:password@host:port/db)
PGUSER=$(echo $DB_URL | sed -n 's/postgresql:\/\/\([^:]*\):.*/\1/p')
PGHOST=$(echo $DB_URL | sed -n 's/postgresql:\/\/[^:]*:[^@]*@\(.*\):.*/\1/p')
PGPORT=$(echo $DB_URL | sed -n 's/.*:\([0-9]*\)\/.*/\1/p')
PGDATABASE=$(echo $DB_URL | sed -n 's/.*\/\([a-zA-Z0-9_]*\).*/\1/p')
PGPASSWORD=$(echo $DB_URL | sed -n 's/postgresql:\/\/[^:]*:\([^@]*\)@.*/\1/p')

export PGPASSWORD

# Nom du fichier backup
BACKUP_FILE="backup_${ENV}_$(date +%Y%m%d%H%M%S).sql"

echo "[BACKUP] Sauvegarde de $PGDATABASE dans $BACKUP_FILE"
pg_dump -h $PGHOST -U $PGUSER -p $PGPORT -F c -b -v -f $BACKUP_FILE $PGDATABASE
echo "[BACKUP] Terminé."
