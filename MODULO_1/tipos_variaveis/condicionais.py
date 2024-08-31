# if, elif e else

# exemplo de if

idade = int(input("Quanto anos vc tem?" ))
print("exemplo de comando if")
if idade >= 18:
    print("voce e maior de idade.")
elif idade >= 12:
    print("vc e um adolescente")
else:
    print("voce e menor de idade")

mensagem = "vc pode tirar a carteira de habilitaçao" if idade >= 18 else "voce nao tem idade suficiente"
print(mensagem)



#if idade == 19:
#    print("voce tem 19 anos")

#if idade < 18:
#    print("voce e menor de idade")

#if idade != 10:
#    print("vc nao tem 10 anos")
