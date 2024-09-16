# If aninhado

conta_normal = True
conta_universitario = False

saldo = 2000
saque = 2500
cheque_especial = 400

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saque + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saque não realizado, saldo insuficiente")

elif conta_universitario:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saque não realizado, saldo insuficiente")
        
else: 
    print("Você não tem conta")