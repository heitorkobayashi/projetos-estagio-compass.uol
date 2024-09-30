'''
Crie uma classe chamada Pessoa, com um atributo privado chamado nome
(declarado internamente na classe como __nome) e um atributo público de nome id.

Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.
Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente. 
Você pode alcançar este comportamento através do recurso de properties do Python.
'''

class Pessoa:
    def __init__(self, id):
        self.id = id        #ciando a pessoa com um ID
        self.__nome = ""    #inicia o nome como uma str vazia e privada

    @property
    def nome(self):
        return self.__nome  #metodo: permite acessar o nome da pessoa

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome   #método: permite definir um novo nome para a pessoa

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
