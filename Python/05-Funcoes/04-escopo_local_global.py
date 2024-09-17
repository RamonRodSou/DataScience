salario = 5000      

def salario_bonus(bonus, lista):
    global salario
    lista.append(2)
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(1900, lista)
print(salario_com_bonus)
print(lista)


print('------------------------------------')
salario2 = 5000      

def salario2_bonus_2(bonus, lista2):
    global salario2
    lista2_aux = lista2.copy()
    lista2_aux.append(2)
    print(f'lista aux={lista2_aux}')
    salario2 += bonus
    return salario2

lista2 = [1]
salario2_com_bonus = salario2_bonus_2(1900, lista2)
print(salario2_com_bonus)
print(lista2)