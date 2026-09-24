import pandas as pd

biblioteca = {"Nome": [], "Data": [], "Autor": []}

print(" Bem vindo sua biblioteca! :)")
print(" Aqui você pode inserir as informações de seus livros preferidos e armazena-las!")
print(" Para finalizar, basta escrever fim")

contagem = 1

while True:
    print("Insira as informações do Livro", contagem, ":" )
    info1 = input("Nome: ")
    if info1 == "fim":
        break
    info2 = input("Data: ")
    info3 = input("Autor: ")
    biblioteca["Nome"].append(info1)
    biblioteca["Data"].append(info2)
    biblioteca["Autor"].append(info3)
    contagem = contagem + 1

data_frame = pd.DataFrame.from_dict(biblioteca)

data_frame.to_excel('biblioteca.xlsx',  index=False)

print("Verifique no seu sistema o arquivo excel com seus livros!")

