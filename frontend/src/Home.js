import React from 'react';
import './Home.css';

const Home = () => {
  return (
    <div className="container">
      <h1 class="h1H">Bienvenue sur notre site web</h1>
      <p class="pH">Notre site web est une plateforme qui offre une variété de services et fonctionnalités pour répondre à vos besoins.</p>
      <p class="pH">Voici quelques-unes des fonctionnalités principales de notre site :</p>
      <ul class="H">
        <li class ="liH">Fonctionnalité 1 : Description de la fonctionnalité ou du service offert.</li>
        <li class ="liH">Fonctionnalité 2 : Description de la fonctionnalité ou du service offert.</li>
        <li class ="liH" >Fonctionnalité 3 : Description de la fonctionnalité ou du service offert.</li>
        {/* Ajoutez d'autres fonctionnalités selon vos besoins */}
      </ul>
      <p>Nous sommes dédiés à offrir une expérience utilisateur exceptionnelle et à vous fournir les outils nécessaires pour atteindre vos objectifs.</p>
    </div>
  );
};

export default Home;