import csv 
import pandas as pd
import time
ListEmpty = []
with open("ListaProdutos.csv","w",encoding="utf8",newline ="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(("Nome","Preço","Quantidade"))
def atual_arq(Rows):
    with open("ListaProdutos.csv","w",encoding="utf8",newline ="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(Rows)

def count_product():
    with open("ListaProdutos.csv","r",encoding="utf8",newline ="") as arquivo:
        Leitor = csv.reader(arquivo)
        Rows = list(Leitor)
        for Row_ in Rows:
            if Row_ == ListEmpty:
                Rows.remove(Row_)
    quanti_prod = len(Rows[1:])
    print("Você possui ",quanti_prod," produtos diferentes cadastrados") 
def adicionar(nome,preco,quantidade):
    var = True
    with open("ListaProdutos.csv","r",encoding="utf8",newline ="") as arquivo:
        Leitor = csv.reader(arquivo)
        Rows = list(Leitor)
        for Row_ in Rows:
            if (Row_[0])== nome:
                print("ja existe esse produto")
                var = False
        if var == True:
            with open("ListaProdutos.csv","a",encoding="utf8",newline ="") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow((nome,"R$" + preco,quantidade))
            print("Produto adicionado com sucesso.\nAguarde um instante para retornar ao menu.")
            time.sleep(3)
        elif var == False:
            Pergunta = input("Deseja Retornar ao menu, ou atualizar o produto?\n(R) para retornar e (A) para adicionar")
            if Pergunta == "A":
                atualizar(nome)
            elif Pergunta == "R":
                print("Aguarde um instante para retornar ao menu")
                time.sleep(3)
def atualizar(nome):
    with open("ListaProdutos.csv","r",encoding="utf8",newline ="") as arquivo:
        Leitor = csv.reader(arquivo)
        Rows = list(Leitor)
        for Row_ in Rows:
            if (Row_[0]) ==nome:
                escolha = input("\n\n*************************************************\nPara atualizar o valor, digite: 1\nPara atualizar a quantidade, digite: 2\nPara atualizar o nome, digite: 3\nPara atualizar o valor e a quantidade, digite: 4\n*************************************************")
                if escolha == "1":
                    preco = input("Qual o valor atual?")
                    Row_[1] ="R$" + preco
                elif escolha == "2":
                    quantidade = input("Qual a Quantidade atual?")
                    Row_[2] = quantidade
                elif escolha == "3":
                    name = input("Qual o nome atual?")
                    Row_[0] = name
                elif escolha == "4":
                    preco = input("Qual o valor atual?")
                    quantidade = input("Qual a Quantidade atual?")
                    Row_[1] ="R$" + preco
                    Row_[2] = quantidade          
                atual_arq(Rows)
while True:
    action = input("***************************************\nSistema de Gerenciamento\n***************************************\n|     Para adicionar um produto, digite: 1     |\n|     Para atualizar um produto, digite: 2     |\n|     Para ver todos os produtos, digite: 3     |\n|     Para ver a quantidade de produtos cadastrados, digite: 4     |\n")
    if action == "3":
        dt = pd.read_csv("ListaProdutos.csv")
        print(dt.head())
    elif action == "1":
        nome,preco,quantidade =input("Digite o nome do produto:\n"),input("Digite o valor do produto:\n"),input("Digite a quantidade em estoque:\n")
        adicionar(nome,preco,quantidade)
    elif action == "2":
        nome = input("Insira o nome do produto que deseja atualizar.\n")
        atualizar(nome)
    elif action == "4":
        count_product()