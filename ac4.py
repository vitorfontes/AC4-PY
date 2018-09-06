class Pessoa ():
    def __init__ (self,Nome,Cpf,Rg,Endereço ):
        self.Nome = Nome
        self.Cpf = Cpf
        self.Rg = Rg
        self.Endereço = Endereço

class Aluno (Pessoa):
    def __init__ (self,RA):
        Pessoa.__init__ (self)
        self.RA = RA
    def imprimealuno (self):
        return self.Nome, self.Cpf, self.Rg , self.Endereço,self.RA
class Professor (Pessoa):
    def __init__ (self,Matriculaprof):
        Pessoa.__init__ (self,Matriculaprof )
        self.Matriculaprof = Matriculaprof
    def imprimeprof (self):
        return self.Nome, self.Cpf, self.Rg , self.Endereço,self.Matriculaprof
class Curso (Aluno, Professor):


x = Aluno()
y = Professor()
print (x.imprimealuno())
print (y.imprimeprof())




