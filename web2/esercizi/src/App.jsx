
import React from 'react';
import Saluto from './Saluto';
import CardUtente from './CardUtente';
import MenuRistorante from './MenuRistorante';

function App() {
  const persona=  {
      nome: "ugo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    }
  const persone = [
    {
      nome: "ugo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Pippo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Gino",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
  ];


  return (
    <div className="App">
      <Saluto></Saluto>
      <MenuRistorante></MenuRistorante>
      <h1>Lista Utenti</h1>
      
      <CardUtente
        nome="Roberto"
        email="rob@rob.it"
        imgUrl="https://placehold.co/600x400/png"
      ></CardUtente>
      
      <CardUtente {...persona}></CardUtente>

      <div className="row">
        {persone.map((p) => {
          return (
            <div className="col">
              <CardUtente {...p}></CardUtente>
            </div>
          );
        })}
        
      </div>
    </div>
    
  );
}

export default App;
