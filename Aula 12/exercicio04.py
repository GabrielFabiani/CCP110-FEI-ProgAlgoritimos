MENU = {
    '1': 'Adicionar usuário',
    '2': 'Buscar usuário',
    '3': 'Atualizar usuário',
    '4': 'Remover usuário',
    '0': 'Sair',
}

def exibir_menu():
    for chave, valor in MENU.items():
        print(f"{chave} - {valor}")
    print()


def novo_contato():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    with open('contato.txt', 'a') as arquivo:
        arquivo.write(f"Nome: {nome},Sobrenome: {sobrenome},Telefone: {telefone},Email: {email}")
        print("Contato adicionado com sucesso")
        print()

def buscar_contato():
    nome_busca = input("Digite o nome que deseja buscar: ")
    encontrado = False
    with open('contato.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, sobrenome, telefone, email = linha.strip().split(',')
            if nome.lower() == nome_busca.lower():
                print(f'Contato encontrado: {nome} {sobrenome}, Telefone: {telefone}, Email: {email}')
                encontrado = True
                break
            if not encontrado:
                print("Contato não encontrado!")
            print()


def atualizar_contato():
    nome_busca = input("Digite o nome que deseja atualizar: ")
    linhas = []
    atualizado = False
    with open ('contatos.txt', 'r') as arquivo:
        linhas = arquivo.readline()
    with open ('contatos.txt', 'w') as arquivo:
        for linha in linhas:
            nome, sobrenome, telefone, email = linha.strip().split(',')
            if nome.lower() == nome_busca.lower():
                print("Contato encontrado. Insira os novos dados:")
                novo_nome = input("Novo nome: ")
                novo_sobrenome = input("Novo sobrenome: ")
                novo_telefone = input("Novo telefone: ")
                novo_email = input("Novo email: ")
                arquivo.write(f"Nome: {novo_nome}, Sobrenome: {novo_sobrenome}, Telefone: {novo_telefone}, Email: {email}")
                atualizado = True
            else:
                arquivo.write(linha)
        if atualizado:
            print("Contato atualizado com sucesso")
        else:
            print("Erro ao atualizar o contato!")


def deletar_contato():
    nome_busca = input("Digite o nome do contato que deseja deletar: ")
    deletado = False
    with open('contato.txt', 'r') as arquivo:
        linhas = arquivo.readline()
        with open ('contatos.txt', 'w') as arquivo:
         for linha in linhas:
            nome, sobrenome, telefone, email = linha.strip().split(',')
            if nome.lower() == nome_busca.lower():
                print(f'Contato encontrado: {nome} {sobrenome}, Telefone: {telefone}, Email: {email}')
                confirma_delete = input("Tem certeza que deseja deletar este contato: S/N ?")
                if confirma_delete == 'S':
                    del nome
                    del sobrenome
                    del telefone
                    del email
                    print("Dados deletados com sucesso!")
                elif confirma_delete == 'N':
                    print("Operação cancelada!")
                deletado = True
                break
            if not deletado:
                print("Contato não encontrado!")
            print()



while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print('Saindo do programa...')
        break
    elif opcao == '1':
        novo_contato()
    elif opcao == '2':
        buscar_contato()
    elif opcao == '3':
        atualizar_contato()
    elif opcao == '4':
        deletar_contato()
    else:
        print("Digite um número válido!")