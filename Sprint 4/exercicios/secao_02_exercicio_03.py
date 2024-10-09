from functools import reduce

def calcula_saldo(lancamentos) -> float:
    conteudo_lancamentos = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    soma_lancamentos = reduce(lambda x, y: x + y, conteudo_lancamentos)
    return soma_lancamentos
    
    
lancamentos = [
    (10, 'D'),
    (300, 'C'),
    (20, 'C'),
    (80, 'D'),
    (300, 'D')
]

resultado = calcula_saldo(lancamentos)
print(resultado)
