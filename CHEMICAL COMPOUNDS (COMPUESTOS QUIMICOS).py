from chemlib import Compound, Reaction

print("** Compuestos químicos **")

#FORMACION DEL COMPUESTO
dioxido_de_carbono = Compound("CO2")
print(f"Fórmula del compuesto: {dioxido_de_carbono.formula}")

#MASA MOLAR
masa_molar = dioxido_de_carbono.molar_mass()
print(f"Masa molar de {dioxido_de_carbono.formula}: {masa_molar:.2f} g/mol")

#COMPOSICION PORCENTUAL EN MASA
composicion = dioxido_de_carbono.percent_composition()
print("Composición porcentual en masa:")
for elemento, porcentaje in composicion.items():
    print(f" - {elemento}: {porcentaje:.2f}%")

#ESTEQUIOMETRIA
carbono = Compound("C")
oxigeno = Compound("O2")
reaccion_dioxido_de_carbono = Reaction({carbono: 1, oxigeno: 1}, {dioxido_de_carbono: 1})

print("\n** Reacción química **")
