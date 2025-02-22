import React from 'react';

const Compte = () => {
  const handleButtonClick = () => {
    // Handle button click logic
  };

  return (
    <div>
      <h2>Compte Component</h2>
      <button onClick={handleButtonClick}>Button 1</button>
      <button onClick={handleButtonClick}>Button 2</button>
    </div>
  );
};

export default Compte;