class Pessoa ():

    def __init__(self, Nome, Cpf, Rg, Endereço):
        self.Nome = Nome
        self.Cpf = Cpf
        self.Rg = Rg
        self.Endereço = Endereço

    def imprimepessoa (self):
        return self.Nome + " " + self.Cpf + " " + self.Rg + " " + self.Endereço

class Aluno (Pessoa):

    def __init__(self, Nome, Cpf, Rg, Endereço, RA):
        Pessoa.__init__ (self, Nome, Cpf, Rg, Endereço,)
        self.RA = RA

    def imprimialuno(self):
        return self.imprimepessoa() + ", " +  self.RA
class Professor (Pessoa):
    def __init__ (self,Nome, Cpf, Rg, Endereço ,Matriculaprof,Materia):
        Pessoa.__init__ (self, Nome, Cpf, Rg, Endereço )
        self.Matriculaprof = Matriculaprof
        self.Materia = Materia
    def imprimeprof (self):
        return self.imprimepessoa() + " " +  self.Matriculaprof + " " + self.Materia
class Curso (Aluno):
    def __init__(self,Nome, Cpf, Rg, Endereço,RA, Curso, Turma):
        Aluno.__init__ (self, Nome, Cpf, Rg, Endereço,RA)
        self.Curso = Curso
        self.Turma = Turma
    def impricurso (self):
        return self.imprimialuno() + " " +  self.Curso + " " + self.Turma


x = Pessoa("joao", "455", "555", "rua")
y = Aluno("joao","455","555","rua","180")
P = Professor("carlos","486","666","rua2","18064","Linguagem de progomação")
c = Curso("joao","455","555","rua","180","ADS","1NOITE")

print(x.imprimepessoa())
print(y.imprimialuno())
print(P.imprimeprof())
print(c.impricurso())
