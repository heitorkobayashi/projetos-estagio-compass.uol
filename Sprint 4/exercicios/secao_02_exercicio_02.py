def conta_vogais(texto: str) -> int:
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_encontradas = filter(lambda x: x in vogais, texto.lower())
    return len(list(vogais_encontradas))
