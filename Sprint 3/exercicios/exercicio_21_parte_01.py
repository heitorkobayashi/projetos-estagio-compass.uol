'''
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse
chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes
(de maneira escrita) no console, conforme o modelo a seguir.
'''

class Passaro:
    def voar(self):
        return "Voando..."

class Pato(Passaro):
    def __init__(self):
        self.som = "Quack Quack"

    def emitir_som(self):
        return f"Pato emitindo som...\n{self.som}"

class Pardal(Passaro):
    def __init__(self):
        self.som = "Piu Piu"

    def emitir_som(self):
        return f"Pardal emitindo som...\n{self.som}"


pato = Pato()
print("Pato")
print(pato.voar())
print(pato.emitir_som(), '\n')
pardal = Pardal()
print("Pardal")
print(pardal.voar())
print(pardal.emitir_som())
