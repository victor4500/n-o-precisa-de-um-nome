print("*************************************")
print("aqui e pra vc tentar acertar o numero")
print("*************************************")

numero = 10

chute = int (input("digita o numero que vc acredita que seja: "))

print(f"voce digitou: {chute}")

if chute == numero:
    print("vc acertou!!!")
else:
    print("vc errou!")