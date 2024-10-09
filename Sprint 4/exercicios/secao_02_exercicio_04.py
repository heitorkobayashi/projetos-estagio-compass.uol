def calcular_valor_maximo(operadores, operandos):
    def aplicar_operacao(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b
        else:
            raise ValueError(f"Operador desconhecido: {op}")

    resultados = map(lambda x: aplicar_operacao(x[0], x[1][0], x[1][1]), zip(operadores, operandos))

    return max(resultados)


operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))
