from persona import Persona
from studente import Studente

#creare un ogetto p di classe Persona
p:Persona = Persona("Philip", "Daoud", 26)

#visulaizzare p
print(p)

#creare un oggetto della classe studente
studente1: Studente = Studente("Leo", "Messi", 35,"9696969")

if isinstance(studente1,Studente):
    print("\nstudente1 è un oggetto della classe studente")

# la funzione isinstance(obj,Class) -> true se l'oggetto è un isanza della classe Class

# voglio sapere se studente1 sia anche un oggetto della classe Persona

if isinstance(studente1,Persona):
    print("\nstudente1 è un oggetto della classe persona")
else:
    print("\nstudente1 è un oggetto della classe studente e non della class Persona")

# voglio controllare se p è un ogetto della classe persona

if isinstance(p,Persona):
   print("\np è un oggetto della classe persona")
else:
    print("\np non è un oggetto della classe persona")

# voglio controllare se p è in ogetto della classe studente

if isinstance(p,Studente):
   print("\np è un oggetto della classe studente")
else:
    print("\np non è un oggetto della classe studente")

# voglio controllare se studente è una sotto classe della class persona
#issubclass(class1,Class2) -> True

if issubclass(Studente,Persona):
    print("\nla classe Studente è sotto classe della classe Persona")

print(studente1)

print(p)

print(f"\nLa media dei voti relativi agli esami studente1 è: {studente1.getMediaEsami([10, 20, 30])}")

# oggetto della classe studente
studente2:Studente = Studente(p.getName(),p.getLast_name(),p.getAge(),"787878")

print(studente2)
# confrontare se studente1 è uguale a p
print("\n",p == studente1)
print("-"*30)
print("\n", studente1 == studente2)
print("-"*30)
print("\n", studente1 == studente1)
print("-"*30)
#modificare nome cognome età dello studente1 affinche abbia lo stesso nome, cognome, età
studente2.setName(studente1.getName())
studente2.setLast_name(studente1.getLast_name())
studente2.setAge(studente1.getAge())
#print
print("\n", studente1 == studente2)
print("-"*30)
# matricole uguali
studente2.setMatricola(studente1.getMatricola())
print("\n", studente1 == studente2)