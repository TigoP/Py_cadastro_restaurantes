import os

restaurantes = [{'nome': 'Praça', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'Pizza', 'categoria': 'pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'italiano', 'ativo': False}]

def exibir_nome_do_programa():
    # Definição criada unicamente para exibir o nome do programa
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
  """)

def exibir_opcoes():
        # Esta função exibe um lista de comandos solicitados ao usiário
    print('1. Cadastrar restaurante')
    print('2. Lista restaurante')
    print('3. Ativar/desativar restaurante')
    print('4. Sair')

def finalizar_app():
    # Definição criada para apresentar ao usuário que o programa será fechado
    exibir_subtitulo('Finalizando app\n')
    print('--------------------------------\n')

def voltar_ao_menu_principal():
      # Definição que pede ao usuário que volte ao menu principal
    input('\nDigite enter para voltar ao menu\n')
    main()

def opcao_invalida():
    # Definição que apresenta msg de erro ao usuário que pressionou teclas diferentes das esperadas
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    # Definição que faz o subtitulo ficar estilizado
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
      # Esta definição solicita ao usuário que insira o nome do restaurante, a categoria dele e apensa à lista restaurantes colocando o novo restaurante em inativo (regra de negócios)
    exibir_subtitulo('| Cadastro de novos restaurantes |')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria = input(f'Diga em qual categoria o restaurante {nome_do_restaurante} se encaixa\n')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    print(f'Os dados do restaurante cadastrado são: {dados_do_restaurante}')

    voltar_ao_menu_principal()

def listar_restaurantes():
      # Definição que estiliza os cabeçalhos e lista procurando cada restaurante na lista de restaurante por categoria
    exibir_subtitulo('|   Listando os restaurantes   |')
    
    print(f'{'Nome do restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'| - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
     # Definição que procura o nome do restaurante digitado pelo usuario. Se o encontrar, faz varredura alterando o estado se estiver ativo, muda pra inativo e vice versa
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'

    voltar_ao_menu_principal()

def escolher_opcao():
    # Definição que traz as opçoes ao usuario e chama as referidas funções
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    # Definição main. Onde vai apresentar na tela chamando as funções desejadas
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
