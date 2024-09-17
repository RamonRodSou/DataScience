nome = 'Ramon'
idade = 31
profissao = "Programador"
linguagem = "Python"

dados = {
    "nome": "Ramon",
    "idade": 31
    }

print ("Nome: %s Idade %d" % (nome, idade))
print ("Nome: {} Idade {}".format(nome, idade))

print ("Nome: {} Idade {}".format(idade , nome))
print ("Nome: {0} Idade {1}{0}{1}".format(idade , nome))
print ("Nome: {nome} Idade {idade}".format(nome=nome, idade=idade))
print ("Nome: {name} Idade {age}{name}".format(name=nome, age=idade))
print ("Nome: {nome} Idade {idade}".format(**dados))
print(f"Eu sou {nome} e tenho {idade} anos, trabalho como {profissao} usando {linguagem}")


PI = 3.14159
print(f'Valor de Pi: {PI}')
print(f'Valor de Pi: {PI:2f}')
print(f'Valor de Pi: {PI:10.2f}')

