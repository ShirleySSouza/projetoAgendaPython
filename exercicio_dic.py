escola = []

while True:
    menu = int(input('Menu de opções:\n1 - Cadastrar aluno.\n2 - Listar informações cadastradas\n3 - Pesquisar pelo nome.\n4 - Alterar cadastro.\n5 - Excluir cadastro.\n9 - Sair.\nDigite a opção desejada: '))
    
    if menu == 1:
        lista = {}
        lista['nome'] = input('Digite o nome do aluno: ')
        lista['disciplina'] = input('Digite a disciplina: ')
        lista['nota1'] = float(input('Digite a nota da primeira prova: '))
        lista['nota2'] = float(input('Digite a nota da segunda prova: '))
        lista['nota3'] = float(input('Digite a nota da terceira prova: '))
        lista['nota4'] = float(input('Digite a nota da última prova: '))
        escola.append(lista)
        
    elif menu == 2:
        for aluno in escola:
            print(f"As notas do aluno {aluno['nome']} na disciplina {aluno['disciplina']} são {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']} e {aluno['nota4']}.")
            media =  ((aluno['nota1'] + aluno['nota2'] + aluno['nota3'] + aluno['nota4']) /4)  
            if media >= 7:
                print(f"A media do aluno {aluno['nome']} é {media} e o aluno está aprovado.")
            else:
                print(f"A media do aluno {aluno['nome']} é {media} e o aluno está reprovado.")
    
    elif menu == 3:
        pesquisa = input('Digite o nome do aluno que deseja pesquisar: ')
        posicao = -1
        i = 0
        for aluno in escola:
            if aluno['nome'].lower() == pesquisa.lower():
                posicao = i
                break
            i = i + 1
        if posicao > -1:    
            print(f"As notas do aluno {aluno['nome']} na disciplina {aluno['disciplina']} são {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']} e {aluno['nota4']}.")
        else:
            print('Nome não encontrado.')
                
    elif menu == 4:
        mod = input('Digite o nome do aluno que deseja modificar: ')
        posicao = -1
        i = 0
        for aluno in escola:
            if aluno['nome'].lower() == mod.lower():
                posicao = i
                break
            i = i + 1
        if posicao > -1:
            escola[posicao]['nome'] = input('Digite o nome do aluno: ')
            escola[posicao]['disciplina'] = input('Digite a disciplina: ')
            escola[posicao]['nota1'] = float(input('Digite a nota da primeira prova: '))
            escola[posicao]['nota2'] = float(input('Digite a nota da segunda prova: '))
            escola[posicao]['nota3'] = float(input('Digite a nota da terceira prova: '))
            escola[posicao]['nota4'] = float(input('Digite a nota da última prova: '))
        else:
            print('Não encontrado.')
            
                
    elif menu == 5:
        deletar = input('Digite o nome do aluno que deseja excluir: ')
        posicao = -1
        i = 0
        for aluno in escola:
            if deletar.lower() == aluno['nome'].lower():
                escola.remove(aluno)
                posicao = i
                break
            i = i + 1
        if posicao > -1:
            print(f"O aluno {aluno['nome']} foi removido da lista.")
        else:
            print('Nome não encontrado.')
    
    elif menu == 9:
        break
    
    else:
        print('Opção invalida.')