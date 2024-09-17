def salvar_carro(marca, modelo, ano, placa):
    print(f'Carrro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
    
salvar_carro("Renault", "Sandeiro", 2008, "KBA-9876")
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2020, placa="OKI-0989") 
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "AVD-1234"})