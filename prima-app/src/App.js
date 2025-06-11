import './App.css';
import Component1 from './Component1';

function getDate(date){
  return date.toLocaleDateString()+" "+ date.toLocaleTimeString()
}

function App() {
  let nome="Philip"
  return (
    <div className="App">
      <Component1></Component1>
        <h1>Prima App Web di {nome}</h1>
        <h2>
          {
            new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()
          }
          </h2>  
          <h2>{getDate(new Date())}</h2>  
          <h2>{getDate(new Date())}</h2> 
          <h2>{getDate(new Date())}</h2> 
    </div>
  );
}

export default App;
