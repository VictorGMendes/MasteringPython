#par e impar
"""

for i in range(10):
    if i%2 != 0:
        print(f"{i} : impar")
    else:
        print(f"{i} : par")
"""
#fibonacci
"""
a, b = 0 , 1
for _ in range(50):
    print(a)
    a,b = b, a+b
    
"""
#lista de alunos
"""
nomes = []

for i in range(5):
    x = input("Nome: ")
    nomes.append(x)

for i in nomes:
    print(i)

"""
#media aritmetica
"""
valores = []
for i in range(1, 5, 1):
    a = float(input(f"Valor {i}: "))
    valores.append(a)

result = sum(valores) / len(valores)
print(f"{result:.2f}")

"""
#digitar o numero até ser maior q o primeiro
"""
a = int(input("digite o numero 1: "))
b = int(input("digite o numero 2: "))

while b < a:
    b = int(input("digite o numero 2: "))
print("parabens animal")
"""