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
![Image](https://github.com/user-attachments/assets/c2ac436d-75cc-4aaa-a1b7-7c95126f158c)

✅ **Sélection de la salle d'examen**
![Image](https://github.com/user-attachments/assets/4c76b334-82b6-428d-8ac0-914540640d8b)

✅ **Détection et enregistrement des étudiants par reconnaissance faciale**
![Image](https://github.com/user-attachments/assets/54fea7a6-ee24-42f1-9ef3-cb96e955a791)

✅ **Affichage en temps réel des présences enregistrées**
![Image](https://github.com/user-attachments/assets/0200d2ff-42f3-46a3-9c4d-5f364f485c94)



### 🌍 Interface Web (Admin)
✅ **Connexion sécurisée**

![Image](https://github.com/user-attachments/assets/70a6270c-f524-4072-90d0-0ccc7047aab5)


✅ **Dashboard**
![Image](https://github.com/user-attachments/assets/a3af0091-86d0-406b-bf83-e0ccfa86cdbd)



✅ **Gestion des enseignants** (Ajout, modification, suppression)
![Image](https://github.com/user-attachments/assets/c5ee1691-7567-4cac-abb1-b0eb75666e60)



✅ **Gestion des salles et des examens**
![Image](https://github.com/user-attachments/assets/126273be-9654-4097-806e-b7aa18473152)


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

- BOUKHRAIS Meryem ([GitHub Profile](https://github.com/Bou-Mery
- SAKHR Niama
- BALLOUK Mohamed
