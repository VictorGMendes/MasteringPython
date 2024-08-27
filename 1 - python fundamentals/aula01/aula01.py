"""
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
print(a+b)
"""

"""
nota1 = int(input("nota 1: "))
nota2 = int(input("nota 2: "))

if (nota1 + nota2)/2 >=5:
    print("passou")
else: print("não passou")
"""

altura = float(input("altura: "))
peso = float(input("peso: "))

imc = peso/(altura**2)
if imc <20 :
    print(f"abaixo do peso, IMC: {imc}")
elif imc<25:
    print(f"peso ideal, IMC: {imc}")
else: print(f"sobrepeso, IMC: {imc}")
