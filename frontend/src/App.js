import React, { useState } from 'react';
import './App.css';
import Topbar from './Topbar';
import Sidebar from './Sidebar';
import Content from './content';
import AddProf from './AddProf';
import Salle from './Salle';
import Home from './Home';
import {Routes,Route,BrowserRouter} from 'react-router-dom';

import Compte from './compte'; // Import the Compte component
import ChoseSalle from './ChoseSalle';
import ChoseFiliere from './ChoseFiliere';
import ChoseModule from './ChoseModule';


const App = () => {
  const [activeItem, setActiveItem] = useState(null);

  const handleSidebarItemClick = (index) => {
    setActiveItem(index);
  };
  const [idsalle, setIdsalle] = useState();
  function putIdsalle(id) {
    setIdsalle(id);
  }
  const [idmodule, setIdModule] = useState();
  function putIdModule(id) {
    setIdModule(id);
  }
  const [idfil, setIdfil] = useState();
  function putIdfiliere(id) {
    setIdfil(id);
  }

  return (
    <div className="app">
      <BrowserRouter>
      <Topbar  />
      <div className="main">
        <Sidebar activeItem={activeItem} onSidebarItemClick={handleSidebarItemClick} />
        <Routes>
            <Route index    element={ <Home />} />
            <Route path="/addp"    element={<AddProf />} />
            <Route path="/sal"   element={<ChoseSalle setIdsalle={putIdsalle}/>} />

            <Route path="/module" element={<ChoseModule setIdmodule={putIdModule} idfil={idfil} idmod={idmodule}/>} />
            <Route path="/filiere" element={<ChoseFiliere setIdfiliere={putIdfiliere}  />} /> 
        <Route path="/etudiant"  element={<Salle idmod={idmodule} idSal={idsalle} idfil={idfil} />} />


        </Routes>
      </div>
      </BrowserRouter>
    </div>
  );
};

export default App;
