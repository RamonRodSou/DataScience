def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa!")
    
    print("Obrigado por ser nosso cliente!")

sacar(100)


def depositar(valor):
    saldo = 50
    
    if saldo >= valor:
        print("O valor depositado tem que ser acima de 50 Reais!")
    
    print("Obrigado por ser nosso cliente!")

depositar(1000)