from chemlib import Compound, Reaction

#FORMACION DE LA REACCION
print("** Reacción química: Formación de CO2 **")

carbono = Compound("C")
oxigeno = Compound("O2")
dioxido_de_carbono = Compound("CO2")

reaccion = Reaction({carbono: 1, oxigeno: 1}, {dioxido_de_carbono: 1})
print("Reacción química antes del balanceo")
print(reaccion)

#BALANCEO DE LA REACCION
reaccion.balance()

print("Reacción química balanceada:")
print(reaccion)
