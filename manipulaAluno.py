def cadastrar(escola): 
    # O nome dentro da função pode ser qualquer um, inclusive o memso nome da variavel que nomeia o deicionário.
    lista = {}
    lista['nome'] = input('\nDigite o nome do aluno: ')
    lista['disciplina'] = input('Digite a disciplina: ')
    lista['nota1'] = float(input('Digite a nota da primeira prova: '))
    lista['nota2'] = float(input('Digite a nota da segunda prova: '))
    lista['nota3'] = float(input('Digite a nota da terceira prova: '))
    lista['nota4'] = float(input('Digite a nota da última prova: ' ))
    escola.append(lista)
    
def listar(escola):
    for posicao in escola:
        print(f"\nAs notas do aluno {posicao['nome']} na disciplina {posicao['disciplina']} são {posicao['nota1']}, {posicao['nota2']}, {posicao['nota3']} e {posicao['nota4']}.")
        media = ((posicao['nota1'] + posicao['nota2'] + posicao['nota3'] + posicao['nota4']) /4)  
        if media >= 7:
            print(f"A media do aluno {posicao['nome']} é {media} e o aluno está aprovado.")
        else:
            print(f"A media do aluno {posicao['nome']} é {media} e o aluno está reprovado.")
        
def buscar(escola):
    pesquisa = input('\nDigite o nome do aluno: ')
    posicao = -1
    i = 0
    for aluno in escola:
        if pesquisa.lower() == aluno['nome'].lower():
            posicao = i
            break
        i = i + 1
    return posicao

def exibir(escola, posicao):
    if posicao > -1:    
        print(f"\nAs notas do aluno {escola[posicao]['nome']} na disciplina {escola[posicao]['disciplina']} são {escola[posicao]['nota1']}, {escola[posicao]['nota2']}, {escola[posicao]['nota3']} e {escola[posicao]['nota4']}.")
    else:
        print('Nome não encontrado.')
        return posicao
    
def alterar(escola, posicao):
    if posicao > -1:
        escola[posicao]['nome'] = input('\nDigite o nome do aluno: ')
        escola[posicao]['disciplina'] = input('Digite a disciplina: ')
        escola[posicao]['nota1'] = float(input('Digite a nota da primeira prova: '))
        escola[posicao]['nota2'] = float(input('Digite a nota da segunda prova: '))
        escola[posicao]['nota3'] = float(input('Digite a nota da terceira prova: '))
        escola[posicao]['nota4'] = float(input('Digite a nota da última prova: '))
    else:
        print('\nNão encontrado.')
        return posicao
    
def excluir(escola, posicao):
    if posicao > -1:
        print(f"\nO aluno {escola[posicao]['nome']} foi removido da lista.")
        escola.pop(posicao)
    else:
        print('Nome não encontrado.')
        return posicao