

console.log("Funzia")

for(let i=0;i<4;i++){
    console.log(i)
}



const arr1=[1,2,3];
let [a,b]=arr1;
console.log(a,b);

console.log(arr1,...arr1);

const arr2=[...arr1];

const arr3=[...arr1,...arr2];
console.log(arr3)

arr1.push(4);
arr2.unshift(0);
console.log(arr1,arr2);

const prof={
    nome:"Rob",
    cognome:"Del",
    età:48,
    indirizzo:{
        via:"via cesare",
        città:"Roma"
    }
}

let {nome:nomi,cognome}=prof
console.log(nomi,cognome)

console.log(prof.indirizzo.via);
console.log(prof["cognome"]);

const prof2=new Object();

prof2.nome="Rob";
prof2.cognome="Del";
console.log(prof2)

function persona(nome="", cognome=""){
    this.nome=cognome;
    this.cognome=nome;
}

const roberto=new persona("Rob","Del");
const mario=new persona("Mario","Rossi");

mario.telefono="1234";

console.log(roberto,mario);

