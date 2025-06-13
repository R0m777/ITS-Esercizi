import React from 'react'

const Component1 = (props) => {
  //console.log(props);
  


  const full_name=()=>{
    return props.nome+" "+props.cognome
  }
  
  return (
    <div style={{
          color:"red",
          border:"1px #000 solid",
          fontweight:"600",
          margin:"15px",
          padding:"15px",
          withdt:"300px",
          diplay:"flex"
          }}>
      
      <div>Component1 di {full_name()} anni {props.eta}</div>
      <Anagrafica></Anagrafica>
      <Messagio></Messagio>
    </div>
  );
};

const Anagrafica=()=>{
  return(<div> Anagrafica</div>)
}

const Messagio=()=>{
  return(<div> Messagio</div>)
}

export default Component1