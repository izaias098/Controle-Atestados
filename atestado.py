#============================
#IMPORTAÇÕES
#============================
import time
import json
#============================
#FUNÇÕES
#============================
def Ver_Todos_os_Atestados():
    print("========= TODOS OS ATESTADOS SALVOS============")
    if not Atestados:
        print("Nenhum atestado cadastrado!")
        return
    for Atestado in Atestados:
        print("=============================")
        print(f"Nome: {Atestado['Nome']}")
        print(f"Data: {Atestado['Data de Recebimento']}")
        print(f"Dias: {Atestado['Dias de Atestado']}")
        print(f"Status: {Atestado['Status']}")
        print("=============================")
        return
def Carregar_Atestados ():
    try:
        with open("atestados.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
def Salvar_Atestados ():
    with open ("atestados.json", "w") as arquivo:
        json.dump (Atestados, arquivo, indent=4)
def Marcar_Concluido ():
    while True:
        nome = input("DIGITE O NOME: ")
        for Atestado in Atestados:
         if Atestado["Nome"] == nome:
            Atestado["Status"] = "Concluido"
            Salvar_Atestados()
            print ("Atestado marcado como concluído")
            return
        print("Nome não encontrado! Digite novamente. ")
def Ver_Atestados_Pendentes ():
    for Atestado in Atestados:
        if Atestado["Status"] == "Pendente":
           print("=============================")
           print(f"Nome: {Atestado['Nome']}")
           print(f"Data: {Atestado['Data de Recebimento']}")
           print(f"Dias: {Atestado['Dias de Atestado']}")
           print(f"Status: {Atestado['Status']}")
           print("=============================")
def Cadastrar_Atestado ():
    print("---------DADOS DO ATESTADO-------")
    nome = input("DIGITE O NOME DO ALUNO: ")
    turma = input("DIGITE A TURMA E O TURNO DO ALUNO: ")
    Data_Recebimento = input("DIGITE A DATA DE RECEBIMENTO: ")
    while len(Data_Recebimento) > 12 :
       print ("Data muito longa! Digite novamente.")
       Data_Recebimento = input("DIGITE A DATA DE RECEBIMENTO: ")
    try: 
     Dias_de_Atestado = int(input("DIGITE A QUANTIDADE DE DIAS DE ATESTADO: "))
    except ValueError:
        print("Digite apenas numero:")
        return
    status = input("DIGITE O STATUS DO ATESTADO: ")
    print("Nome: ", nome)
    print("Turma: ", turma)
    print("Data de recebimento", Data_Recebimento)
    print("Dias de atestado", Dias_de_Atestado)
    print("Status", status)
    #DICIONARIO DE ATESTADOS
    atestado = {
     "Nome": nome,
        "Turma": turma, 
        "Data de Recebimento": Data_Recebimento, 
        "Dias de Atestado": Dias_de_Atestado,
        "Status": status 
    }
    Atestados.append (atestado)
    Salvar_Atestados()
    return "cadastro"
Atestados = Carregar_Atestados()
#=============================
#MENU PRINCIPAL
#=============================
while True:
    print("\n" + "=" * 40)
    print("-------------------CONTROLE DE ATESTADO------------------")
    print("1- CADASTRAR ATESTADO")
    print("2- VER ATESTADO PENDENTES")
    print("3- MARCAR CONCLUIDO")
    print("4- MOSTRAR TODOS OS ATESTADOS SALVOS")
    print("5- sair")
    print("=" * 40)
    opcao = int(input("ESCOLHA UMA OPÇÃO: "))

    if opcao == 1:
        print ("Carregando cadastro...")
        time.sleep(3)
        Cadastrar_Atestado()
    elif opcao == 2:
        print ("Verificando...")
        time.sleep(3)
        Ver_Atestados_Pendentes()
    elif opcao == 3:
        print ("Carregando...")
        time.sleep(3)
        Marcar_Concluido()
    elif opcao == 4:
        Ver_Todos_os_Atestados()
        time.sleep(1)
    elif opcao == 5:
        print("Saindo...")
        time.sleep(1)
        exit()
    else:
        print("opção invalida")
        break