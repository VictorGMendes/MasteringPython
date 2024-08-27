pessoas = {
    "joao@gmail.com": {
        "nome": "joao",
        "idade": 20
        },
    
    "victor@gmail.com" : {
        "nome": "victor",
        "idade": 21
        }
    }


inicio = True

while inicio:
    escolha = int(input("""
1 - Inclusão
2 - Exclusão
3 - Exibição de todos os registros
4 - Alteração dos dados de uma pessoa
5 - Exibir uma pessoa
6 - Sair
\n
escolha uma opção: """))
    match escolha:
        case 1:
            e = input("\nDigite o email para adicionar: ")
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            
            pessoas[e] = {"nome": nome,
                          "idade" : idade,
                          "email" : e}
        
        case 2:
            n = input("Digite o email que quer excluir: ")
            pessoas.pop(n)
            print(f"{n} excluido")

        case 3:
            print("*"*30)
            for i, email in enumerate(pessoas):
                print(f"id : {i}\nnome : {pessoas[email]["nome"]}\nemail : {email}\nidade : {pessoas[email]["idade"]}\n{"*"*30}")
        case 4:
            e = input("\nDigite o email para alterar: ")
            pessoas.pop(n)
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            pessoas[e] = {"nome": nome,
                          "idade" : idade,
                          "email" : e}
        case 5:
            e = input("digite o email para pesquisar: ")
            print(f"\nnome : {pessoas[e]["nome"]}\nemail : {e}\nidade : {pessoas[e]["idade"]}\n{"*"*30}")
        case 6: 
            break
        case _:
            print("escolha algo valido")
            