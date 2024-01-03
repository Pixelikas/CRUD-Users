
# Function para cadastrar usuário
def Cadastrar():

    # Inicializa variável de posição e pergunta user a cadastrar
    userPos = -1
    addUser = input('User a cadastrar: ')

    # Percorre lista de usuários, verificando se existe e salvando a posição
    for user in userLista:
        if addUser == user:         
            userPos = userLista.index(user)
  
    # Se existir, mostra mensagem indicando não ser possível cadastrar
    if userPos != -1:

        print('User Já Existe! :/\n')

    # Se não existir, cadastra User        
    else:

        userLista.append(addUser)
        print('User Cadastrado! :D\n')    

# Function para deletar usuário
def Deletar():

    # Inicializa variável de posição e pergunta user a deletar
    userPos = -1
    delUser = input('User a deletar: ')
            
    # Percorre lista de usuários, verificando se existe e salvando a posição
    for user in userLista:
        if delUser == user:         
            userPos = userLista.index(user)

    # Se existir, deleta User     
    if userPos != -1:

        userLista.pop(userPos)                    
        print('User Deletado! :/\n')

    # Se não existir, mostra mensagem indicando não ser possível deletar
    else:

        print('User Não Encontrado! :/\n')

# Function para editar usuário
def Editar():

    # Inicializa variável de posição e pergunta user a editar
    userPos = -1
    editUser = input('User a editar: ')
        
    # Percorre lista de usuários, verificando se existe e salvando a posição
    for user in userLista:
        if editUser == user:         
            userPos = userLista.index(editUser)

    # Se existir, pergunta novo User e edita
    if userPos != -1:

        newUser = input('Novo user: ')
        userLista[userPos] = newUser                    
        print('User Editado! :D\n')

    # Se não existir, mostra mensagem indicando não ser possível editar
    else:

        print('User Não Encontrado! :/\n')

# Function para listar usuários
def Listar():

    # Verifica se não existem usuários na lista e mostra mensagem
    if len(userLista) == 0:

        print(f'Não Existem Users Cadastrados! :(\n')

    # Se existirem, mostra a lista
    else:
                
        print(f'Lista de Users Cadastrados\n\n{userLista}\n')


# Vetor para armazenar usuários
userLista = []

# Variável para armazenar a opção do menu
opEscolhida = 0

# Loop do menu
while(opEscolhida != 5):

    # Menu com as opções e variável que armazena opção escolhida
    opEscolhida = int(input(f'>>>>> MENU <<<<<\n\n1 - Cadastrar User\n2 - Deletar User\n3 - Editar User\n4 - Listar Users\n5 - Sair\n\nOpção: '))
    
    # Estrutura de seleção para verificar a opção escolhida e chamar as functions
    match opEscolhida:

        case 1:
            # Caso a opção escolhida seja 1, chama function de cadastro
            Cadastrar()
            
        case 2:
        
            # Caso a opção escolhida seja 2, chama function de deleção
            Deletar()
            
        case 3:
            
            # Caso a opção escolhida seja 3, chama function de edição
            Editar()

        case 4:

            # Caso a opção escolhida seja 4, chama function de lista
            Listar()
            
        case 5:
            
            # Caso a opção escolhida seja 5, finaliza programa
            print('Tchauuuuuuu!\n')
            
        case other:
            
            # Caso a opção escolhida não seja de 1 a 5, mostra mensagem de inválido
            print('Opção inválida! :(\n')