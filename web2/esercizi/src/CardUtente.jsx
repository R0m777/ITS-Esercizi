import React from 'react';

function CardUtente(props) {
  return (
    <div className="card-utente" style={{ border: '1px solid #ccc', padding: '1rem', margin: '1rem', width: '250px' }}>
      <img src={props.imgUrl} alt="Avatar utente" style={{ width: '100%', height: 'auto', borderRadius: '50%' }} />
      <h2>{props.nome}</h2>
      <p>{props.email}</p>
    </div>
  );
}

export default CardUtente;
