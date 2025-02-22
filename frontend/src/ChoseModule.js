import { useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import axios from "axios";
import './ChoseSalle.css';

export default function ChoseModule({ setIdmodule ,idfil }) {
  const navigate = useNavigate();
  const [modules, setModules] = useState([]);

  const getModules = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/getmodules', {
        params: {
          idfil: idfil // Envoyer idfil comme paramètre dans la requête
        }
      });

      setModules(response.data);
      console.log("Données des modules :", modules);
      console.log("Serveur répond avec succès");
    } catch (error) {
      console.log("Récupération des données échouée");
    }
  }

  const handleClick = (idmodul) => {
    setIdmodule(idmodul);
    navigate('/etudiant')
  }

  useEffect(() => {
    getModules();
  }, []);

  return (
    <div className='sallecon'>
      {modules.map(module => (
        <div className='sal' key={module.id} onClick={() => handleClick(module.id)}>
          <span>{module.nomModule}</span>
        </div>
      ))}
    </div>
  );
}