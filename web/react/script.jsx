const elementRoot=document.querySelector("#root");
const root=ReactDOM.createRoot(elementRoot)

const App=()=>{
    return(
        <main>
        <h1>Primo componente</h1>
        {props.children}
        </main>
    );
};

const List=function(){
    return (
        <ul>
            <li>PHP</li>
            <li>JS</li>
            <li>Python</li>
        </ul>
    );
};

root.render(
    <>
    <App>
        <h2>Lista componente</h2>
    </App>
    <List/>
    </>
)