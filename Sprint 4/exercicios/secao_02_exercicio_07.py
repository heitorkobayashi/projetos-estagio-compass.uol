def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    produtos_filtro = filter(lambda x: x[1] > media, conteudo.items())
    produtos_filtro_ordenados = sorted(produtos_filtro, key=lambda x: x[1])
    return produtos_filtro_ordenados

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo)
print(resultado)
