def alugar():
    nome = input("digite o nome")
    pcd = int(input("É PCD\n [0] Sim\n [1] não"))
    dias_aluguel = int(input("digite os dias"))
    escolha_carro = int(input('''Qual carro você ira alugar:\n 1- executivo\n 2- carga\n 3- hatch\n 4- sedan'''))
    valor_carro = float()

    if escolha_carro == 1:
        escolha_carro = "executivo"
        valor_carro = 500.00 
    elif escolha_carro == 2:
        escolha_carro = "carga"
        valor_carro = 750.00 
    elif escolha_carro == 3:
        escolha_carro =  "hatch"
        valor_carro = 170.00 
    elif escolha_carro == 4:
        escolha_carro = "sedan"
        valor_carro = 250.00 
       

    if pcd == 0:
        valor_carro -= valor_carro * 0.3
    valor_total = valor_carro * dias_aluguel

    

    return print('Nome: {} \n Carro: {}\n Dias: {}\n custo total R${}'.format(nome, escolha_carro, dias_aluguel, valor_total))



