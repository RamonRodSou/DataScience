saldo = 100
saque = 250
limite = conta_especial = True

# Tabela Verdade

# | True  | True  | True  |
# | True  | False | False |
# | False | True  | True  |
# | False | False | False |



print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
