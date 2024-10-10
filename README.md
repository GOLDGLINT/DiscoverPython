
# scpOS

Un site web permettant aux employés de voir le status de chaque SCP. Des fonctionnalités supplémentaires sont dans la roadmap ;).
## Auteurs

- [@GOLDGLINT](https://github.com/GOLDGLINT)
- [@BldNicolas](https://github.com/BldNicolas)


## Technos

**Frontend:**
- React

**Backend:** 
- Python
- FastAPI : Gère les appels API
- tortoise : ORM

**Design:**
- Figma
- Sketchbook
## Installation

Le projet est réaliser via Docker.

1. Installer Docker

2. Build les images et les lancer :

```bash
  docker-compose up --build
```

3. Pour dev :
3.1. Créer un environnement virtuel :
```bash
python -m venv scpOSVenv
```

3.2. Activer l'environnement virtuel :
- MacOS:
```bash
source scpOSVenv/bin/activate
```

- Windows :
```bash
scpOSVenv\Scripts\activate
```

3.3. Installer les dépendances :
```bash
pip install --no-cache-dir --upgrade -r requirements.txt
```
