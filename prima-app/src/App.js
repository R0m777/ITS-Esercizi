import './App.css';
import Component1 from './Component1';
import Clock from './Clock';

function getDate(date){
  return date.toLocaleDateString()+" "+ date.toLocaleTimeString()
}

function App() {
  let nome="Philip";
  
  const persona1=[{
    nome:"Leo",
    cognome:"Messi",
    eta:"36"
  },]

  const persona2=[{
    nome:"Philip",
    cognome:"Del",
    eta:"27"
  },]

  const persona3=[{
    nome:"Chiara",
    cognome:"Ciotti",
    eta:"25"
  },]

  

  
  return (
    <div className="App">
      <Component1 {...persona1}></Component1>
      <Component1 {...persona2}></Component1>
      <Component1 {...persona3}></Component1>
        <h1>Prima App Web di {nome}</h1>
        <h2>
          {
            new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()
          }
          </h2>  
          <h2>{getDate(new Date())}</h2>  
      <Clock timezone="0" country="Italia" >qualcosa</Clock>
      <Clock timezone="-6" country="USA" ></Clock>
      <Clock timezone="7" country="Russia" ></Clock>
    </div>
  );
}

export default App;
