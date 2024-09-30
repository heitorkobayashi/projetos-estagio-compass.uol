'''
Crie uma classe Ordenadora que contenha um atributo listaBaguncada
e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha
como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto,
decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto,
use o método ordenacaoDecrescente.
'''

class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)      #sorted ordena iteráveis, entao vai retornar a lista ordenada

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

#instancias
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()
print(resultado_crescente) 
print(resultado_decrescente) 
