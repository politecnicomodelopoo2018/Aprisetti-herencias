from ejercicio8ClassRadio import Radio
from ejercicio8ClassPrograma import Programa
from ejercicio8ClassProgramaMusica import programaMusica
from ejercicio8ClassPersona import Persona
from ejercicio8ClassBloque import Bloque
import datetime

aprisettiLaRadio = Radio()

datetime.date(2031, 3, 3)

operetti = Persona("Ingenieretti", "Aprisetti", 666, datetime.date(2031, 3, 3), "Operario")
musiquetti = Persona("musiquetti", "Aprisetti", 1352,datetime.date(2031, 7, 8), "musicalizadoretti")

elMejorPrograma = Programa("AprisettiShow", operetti, "Diversion")
for i in range(3):
    bloques = Bloque(1+i,6-i)
    elMejorPrograma.addBloque(bloques)


elProgramaPromedio = programaMusica("Rocking w/ ur mom", operetti,"musica", musiquetti, "Hard Rock")
for i in range(3):
    bloques = Bloque(2+i,5-i)
    elProgramaPromedio.addBloque(bloques)

elPeorPrograma = programaMusica("Rocking w/ ur mom", operetti,"musica", musiquetti, "Hard Rock")
bloques = Bloque(0,5)
elPeorPrograma.addBloque(bloques)

print(aprisettiLaRadio.addPrograma(elMejorPrograma))
print(aprisettiLaRadio.addPrograma(elProgramaPromedio))
print(aprisettiLaRadio.addPrograma(elPeorPrograma))


with open("Persona.aps", "w") as f:
    f.write(operetti.codificacion() + "\n")

with open("Persona.aps", "r") as f:
    for line in f:
        datosPersona = line.split("|")
        personaArchivo = Persona(datosPersona[0], datosPersona[1], datosPersona[2], datosPersona[3], datosPersona[4])
        elMejorPrograma.addConductor(personaArchivo)
        for item in datosPersona:
            print(item)

with open("Programas.aps", "w") as f:
    for item in aprisettiLaRadio.listaProgramas:
        f.write(item.codificacion() + "\n")
with open("Programas.aps", "r") as f:
    for line in f:
        datos = line.split("|")
        clase = eval(datos[0])
        x = clase()
        x.decodificacion(datos)
        print(x.nombre)



