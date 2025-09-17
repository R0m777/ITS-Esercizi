import React from 'react';
import piatti from './piatti';

function MenuRistorante() {
  return (
    <div>
      <h2>Menu del Ristorante</h2>
        {
          piatti.map((p,index)=>{
            return (<p key={p.id}>{p.nome} €{p.prezzo}</p>)
          })
        }
      
    </div>
  );
}

export default MenuRistorante;
