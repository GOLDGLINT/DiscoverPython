# Utiliser une image Node.js comme base
FROM node:18

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package.json ./
COPY package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier le code source
COPY . .

# Construire l'application React
RUN npm run build

# Exposer le port 3000 pour le frontend
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["npm", "start"]