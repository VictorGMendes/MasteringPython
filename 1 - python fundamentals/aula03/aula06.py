"""
tupla = ("a", "b", "a"," c", "a")
print(tupla.index)


print(tuple("aaaa"))

"""
nomes = ["joao", "gabriel"]
inicio = True

while inicio:
    escolha = int(input("""
1 - inclusão
2 - Exclusão
3 - Exibição
4 - Sair
\n
escolha uma opção: """))
    match escolha:
        case 1:
            n = input("\nDigite o nome para adicionar: ")
            nomes.append(n)
            print(f"\n{n} inserido")
        
        case 2:
            n = input("Digite o nome que quer excluir: ")
            nomes.remove(n)
            print(f"{n} excluido")

        case 3:
            for n in nomes:
                print(n)
        case 4:
            break
        case _:
            print("escolha algo valido")
            
            
                    