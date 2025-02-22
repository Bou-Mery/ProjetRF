import { useNavigate } from 'react-router-dom'
import { useState } from 'react';
import axios from "axios";
import { useEffect } from 'react';
import './ChoseSalle.css';

export default function ChoseSalle({setIdsalle}) {
    const navigate=useNavigate();
    const [salles,setSalles] =useState([])
  const data = { prompt: 'Votre donnée ici' };

    const getSalles = async () => {
        try {
            const response= await axios.get('http://localhost:8000/api/getsalle')
            console.log("Données de la salle :", salles);

            setSalles(response.data)
            console.log("serveur reponde avec succes")
        } catch (error) {
            console.log("recuperation des donnees echoue")
        }

    }

    const handleClick = async (idsall) => {
        setIdsalle(idsall)
        console.log(idsall)
        navigate("/filiere")

    }

    useEffect(() => {
        getSalles();
    }, []);
    

    return(
        <div className='sallecon'>
            {salles && salles.map( (sall) => ( <div className='sal' key={sall.idSalle} onClick={() => handleClick(sall.idSalle)}>{sall.nomSalle}</div>))}
        </div>
    )
}