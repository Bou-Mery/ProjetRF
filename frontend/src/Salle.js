import { useState, useEffect } from "react";
import './Salle.css';
import axios from "axios";

export default function Salle({ idmod, idSal, idfil }) {
  const [data, setData] = useState({
    dateExamen: "",
    heureDeb: "",
    heureFin: "",
    idSalle: idSal,
    cneEtudiant: "",
    idModule: idmod,
  });

  const [etudiants, setEtudiants] = useState([]);

  const getAllStudents = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/etudiants', {
        params: {
          idfil: idfil // Envoyer idfil comme paramètre dans la requête
        }
      });
      setEtudiants(response.data);
    } catch (error) {
      console.log("Récupération des données échouée");
    }
  }

  function handleChange(e) {
    setData({
      ...data,
      [e.target.name]: e.target.value
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/enrg', data);
      console.log(response.data);
      setData({
        dateExamen: "",
        heureDeb: "",
        heureFin: "",
        idSalle: idSal,
        cneEtudiant: "",
        idModule: idmod,
      });
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    getAllStudents();
  }, []);

  return (
    <div className="container2">
      <div className="content-container2">
        <div className="header2">
          <h2>Ajouter un étudiant</h2>
        </div>
        <form onSubmit={handleSubmit} encType="multipart/form-data">
          <div className="inputs2">
            
            <div className="con2">
              <input
                type="text"
                value={data.dateExamen}
                onChange={handleChange}
                name="dateExamen"
                placeholder="Date"
                className="input-field"
              />
              <input
                type="text"
                value={data.heureDeb}
                onChange={handleChange}
                name="heureDeb"
                placeholder="Heure Debut d'Examen"
                className="input-field"
              />
            </div>
            <div className="con2">
              <input
                type="text"
                value={data.heureFin}
                onChange={handleChange}
                name="heureFin"
                placeholder="Heure Fin d'Examen"
                className="input-field"
              />
              <select onChange={handleChange} name="cneEtudiant" className="input-field">
                <option>Etudiants</option>
                {etudiants && etudiants.map((etudiant) => (
                  <option key={etudiant.id} value={etudiant.cne}>{etudiant.nom}</option>
                ))}
              </select>
            </div>
          </div>
          <div className="img2">
            <div className="btn2">
              <button type="submit">Ajouter</button>
            </div>
            <input type="file" name="image" onChange={handleChange} />
          </div>
        </form>
      </div>
    </div>
  );
}