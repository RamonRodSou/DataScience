def exibir_mensagem():
    print("Olá, mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem_3(nome="Anoniomo"):   # Se nao for passado nenhum parametro, ele vai retornar Anomimo
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem_2(nome="Ramon")
exibir_mensagem_3()
exibir_mensagem_3("Samara")


def calcular_total(numero):
    return sum(numero)

def retorna_antecessor_e_sucessor(numero):
    return (numero - 1, numero + 1)