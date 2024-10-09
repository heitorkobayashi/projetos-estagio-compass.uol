def processamento_notas():
    with open('estudantes.csv', 'r') as grade_notas:
        conteudo_grade = grade_notas.readlines()

    resultado = []
    for linha in conteudo_grade:
        dados = linha.strip().split(',')
        nome = dados[0]
        notas = list(map(float, dados[1:]))

        maiores_3_notas = sorted(notas, reverse=True)[:3]
        media_notas = round(sum(maiores_3_notas) / 3, 2)

        notas_formatadas = [int(n) if n.is_integer() else n for n in maiores_3_notas]
        
        resultado.append(f"Nome: {nome} Notas: {notas_formatadas} Média: {media_notas}")

    for r in sorted(resultado):
        print(r)

processamento_notas()
