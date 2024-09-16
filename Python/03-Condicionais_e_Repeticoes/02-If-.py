MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Infome sua idade: "))

if idade >= MAIOR_IDADE:
    print("1- Você é maior de idade")

if idade < MAIOR_IDADE:
    print("1- Você é menor de idade")



if idade >= MAIOR_IDADE:
    print("2- Você é maior de idade")
else: 
    print("2- Você é menor de idade")
    
    
    
if idade >= MAIOR_IDADE:
    print("3- Você é maior de idade")
elif idade == IDADE_ESPECIAL:
    print("3- Você já é menor de idade mais pode fazer auto escola")
else:
    print("3- Você é menor de idade")
    
