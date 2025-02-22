import { useNavigate } from 'react-router-dom'
import { useState } from 'react';
import axios from "axios";
import { useEffect } from 'react';
import './ChoseSalle.css';


export default function ChoseFiliere({setIdfiliere}) {
    const navigate=useNavigate();
    const [filieres,setFilieres] =useState([])

    const getFilieres = async () => {
        try {
            const response= await axios.get('http://localhost:8000/api/getfilieres')
            console.log("Données de la filieres :", filieres);

            setFilieres(response.data)
            console.log("serveur reponde avec succes")
        } catch (error) {
            console.log("recuperation des donnees echoue")
        }

    }

    const handleClick = async (idfiliere) => {
        setIdfiliere(idfiliere)
        console.log(idfiliere)
        navigate("/module")

    }

    useEffect(() => {
        getFilieres();
    }, []);
    

    return(
        <div className='sallecon'>
            {filieres && filieres.map( (filiere) => ( <div className='sal' key={filiere.idFiliere} onClick={() => handleClick(filiere.idFiliere)}>{filiere.nom}</div>))}
        </div>
    )
}