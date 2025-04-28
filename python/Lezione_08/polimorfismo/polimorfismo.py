from persona import Persona
from alieno import Alieno


# creare un oggetto p della classe Persona
p: Persona = Persona("Philip","Daoud",26)

# visualizziamo le info della persona p
print(p)

# creare un oggetto et della classe Alieno
et:Alieno = Alieno("Atehdja")

# visualizzare le info dell'alieno et
print(et)

# l'oggetto p invoca il metodo speak()
p.speak()

# l'oggetto et invoca il metodo speak()
et.speak()