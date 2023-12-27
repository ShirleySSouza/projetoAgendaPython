from uteis import opcoes
from manipulaAluno import cadastrar, listar, buscar, exibir, alterar, excluir

escola = []

while True:
    menu = opcoes()
    
    if menu == 1:
       cadastrar(escola)
       
    elif menu == 2:
       listar(escola)
       
    elif menu == 3:
        posicao = buscar(escola)
        exibir(escola, posicao)
        
    elif menu == 4:
        posicao = buscar(escola)
        alterar(escola, posicao)
            
    elif menu == 5:
        posicao = buscar(escola)
        excluir(escola, posicao)
       
    elif menu == 9:
        break
    
    else:
        print('Opção invalida.')