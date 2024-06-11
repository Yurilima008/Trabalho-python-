nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade<16:
    print(f"{nome} não pode emitir seu titulo")
else:
    print(f"{nome} pode emitir seu titulo")