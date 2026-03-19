# Architecture Technique de l'Application Bookmark

## 1. Aperçu

- **Backend** : Flask + SQLAlchemy
- **Frontend** : HTML + CSS + JS (consommation API)
- **Base de données** : PostgreSQL (Neon.tech)
- **Environnements** : dev, staging, prod (DSP ENV)
- **Extensions Flask** : SQLAlchemy, Migrate, Marshmallow
- **Version Control** : GitHub
- **Mobile DevOps** : Termux + PRoot Ubuntu + tmux

## 2. Arborescence finale
bookmark/ ├── app/ │   ├── init.py │   ├── config.py │   ├── database.py │   ├── models.py │   ├── routes.py │   └── extensions.py ├── frontend/ │   ├── index.html │   ├── css/ │   └── js/ ├── scripts/ │   ├── seed_db.py │   └── backup_db.sh ├── tests/ ├── migrations/ ├── run.py ├── requirements.txt └── docs/

## 3. Flux DSP ENV

1. `.env.dev`, `.env.staging`, `.env.prod` contiennent `DATABASE_URL`.  
2. `Config` charge dynamiquement la DB selon `ENV`.  
3. CRUD via `routes.py` consomme la base correspondante.  

## 4. Monitoring et DevOps

- Termux : shell + tmux  
- CI/CD scripts : tests, push GitHub  
- Backup automatique via `backup_db.sh`


