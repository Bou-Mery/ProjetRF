import { useState, useEffect } from "react";
import axios from "axios";
import "./AddProf.css";

export default function AddProf() {
  const [professeurs, setProfesseurs] = useState([]);
  const [data, setData] = useState({
    cin: "CIN",
    username: "",
    password: ""
  });

  const getProfesseurs = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/getprof");
      setProfesseurs(response.data);
    } catch (error) {
      console.log("Erreur lors de la récupération des données");
    }
  };

  function handleChange(e) {
    setData({
      ...data,
      [e.target.name]: e.target.value
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/addprofc",
        data
      );
      console.log(response.data);
      // Réinitialiser le formulaire après la soumission réussie si nécessaire
      setData({
        cin: "CIN",
        username: "",
        password: ""
      });
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    getProfesseurs();
  }, []);

  return (
    <div className="content-container">
      <div className="header">
        <h2 className="div">Ajouter un compte professeur</h2>
      </div>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <div className="inputs">
          <div className="con">
            <select onChange={handleChange} name="cin" className="infop">
              <option>Professeur</option>
              {professeurs &&
                professeurs.map((prof) => (
                  <option key={prof.id} value={prof.cin}>
                    {prof.nom} {prof.prenom}
                  </option>
                ))}
            </select>
          </div>
          <div className="con">
            <p className="info input-field">{data.cin}</p>
          </div>
          <div className="con">
            <input
              type="text"
              value={data.username}
              onChange={handleChange}
              name="username"
              placeholder="Email@exemple.com"
              className="info input-field"
            />
            <input
              type="text"
              value={data.password}
              onChange={handleChange}
              name="password"
              placeholder="Mot de passe "
              className="info input-field"
            />
          </div>
        </div>
        <div className="img">
          <div className="btn">
            <button type="submit" className="btn-primary">
              Ajouter
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}