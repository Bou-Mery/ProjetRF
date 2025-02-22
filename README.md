# 🎓 Système de Gestion des Présences par Reconnaissance Faciale

## 📌 Description du Projet
Ce projet vise à automatiser la gestion des présences lors des examens académiques en utilisant la **reconnaissance faciale**. Il comprend :
- Une **application desktop** pour l'enregistrement des présences en temps réel.
- Une **interface web** pour la gestion des étudiants, des salles et des enseignants.

---

## 🛠️ Technologies Utilisées

### 🚀 Backend
- **PHP & Laravel** : Développement des API REST et gestion de la logique métier.
- **MySQL** : Base de données relationnelle pour stocker les informations des utilisateurs et des examens.
- **Python & OpenCV** : Traitement et détection faciale en temps réel.
- **Face_Recognition** : Identification et comparaison des visages.

### 🎨 Frontend
- **React.js** : Développement d'une interface utilisateur dynamique et réactive.
- **CSS & Bootstrap** : Amélioration de l’expérience utilisateur avec un design moderne.

### 🖥️ Application Desktop
- **Python (Tkinter & PyQt)** : Interface graphique pour l'enregistrement des présences.
- **OpenCV & PIL** : Capture et traitement des images en temps réel.
- **MySQL Connector** : Communication entre la base de données et l'application.

---

## 📷 Interfaces et Fonctionnalités

### 🖥️ Application Desktop
✅ **Authentification des enseignants**

✅ **Sélection de la salle d'examen**
✅ **Détection et enregistrement des étudiants par reconnaissance faciale**
✅ **Affichage en temps réel des présences enregistrées**

### 🌍 Interface Web (Admin)
✅ **Connexion sécurisée**
✅ **Gestion des enseignants** (Ajout, modification, suppression)
✅ **Gestion des étudiants** (Ajout, modification, suppression)
✅ **Gestion des salles et des examens**
✅ **Visualisation des présences**

---

## ⚡ Installation et Exécution
### 🖥️ Prérequis
- **WampServer** (ou XAMPP) pour exécuter le backend PHP/MySQL.
- **Python 3.x** avec OpenCV et les bibliothèques nécessaires.
- **Node.js** pour exécuter l'interface web React.js.

### 🚀 Installation
```bash
# Cloner le projet
git clone git remote add origin https://github.com/Bou-Mery/ProjetRF.git
cd ProjetRF

# Installer les dépendances du backend
cd backend
composer install

# Installer les dépendances du frontend
cd ../frontend
npm install
```

### ▶️ Exécution
```bash
# Lancer le serveur backend
php artisan serve

# Lancer l’application React
npm run dev

# Exécuter le script Python
python assemblage.py
```

---

## 👥 Contributeurs


📌 **Contactez-nous pour toute amélioration ou contribution !** 😊
- BOUKHRAIS Meryem ([GitHub Profile](https://github.com/Bou-Mery
- SAKHR Niama
- BALLOUK Mohamed
