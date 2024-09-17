def soma ( a, b ):
    return a + b

def subtracao( a, b ):
    return a - b


def mulltiplicacao( a, b ):
    return a * b


def divisao( a, b ):
    return a / b

def exibir_resultado( a, b, funcao ):
    resultado = funcao( a, b )
    print(f'O Resuiltado é = {resultado}')
    
exibir_resultado( 10, 20, soma)
exibir_resultado( 10, 20, subtracao)
exibir_resultado( 2, 20, mulltiplicacao)
exibir_resultado( 20, 2, divisao)

operacao = soma
exibir_resultado( 10, 20, operacao) 
print(operacao(2, 4))