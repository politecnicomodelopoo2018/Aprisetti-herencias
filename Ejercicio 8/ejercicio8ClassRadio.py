
class Radio(object):

    def __init__(self):

        self.listaProgramas = []


    def compHor(self, programaAComp):

        for prog in self.listaProgramas:
           if prog.checkHorario(programaAComp.listaBloques):
           # for bloq in prog.listaBloques:
            #    for bloqComp in programaAComp.listaBloques:
             #       if bloqComp.dia == bloq.dia and bloqComp.horario == bloq.horario:
                        return False

        return True

    def addPrograma(self, programaAIngresar):

        if self.compHor(programaAIngresar):
            self.listaProgramas.append(programaAIngresar)
            return True
        return False