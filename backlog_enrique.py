# Dicionarios 
usuario = []
produtos = []
caprodutos = []
carrinho = []
compras = []
visualizar_car = []
admin = {'admin': 'senhaadmin'}
def ln():
    print("-" *30)

def cadastro_usuario():
    nome = input("Digite o nome do novo usuario: ")
    gmail = input("Digite o gmail do novo usuario: ")
    senha = input("Digite o senha do novo usuario: ")
    novo_usuario = {'nome': nome, 'email': gmail, 'senha': senha}
    usuario.append(novo_usuario)
    print(f'Usuário {nome} cadastrado com sucesso!')

def login():
    gmail = input("Digite o gmail do novo usuario: ")
    senha = input("Digite o senha do novo usuario: ")
    for i in usuario:
        if gmail[usuario] == gmail and i and i [senha] == senha:
            return True
    return False

def admin_at_estoque():
    ln()
    print('Atualização de Estoque:')
    ln()
    nome_produto = input('Digite o nome do produto: ')
    ln()
    quantidade = int(input('Digite a quantidade a ser adicionada: '))
    ln()

    for j in produtos:
        if j['nome'] == nome_produto:
            j['quantidade'] += quantidade
            nome_produto.append(produtos)
            ln()
            print(f'Estoque do produto {nome_produto} atualizado para {j["quantidade"]}.')
            ln()
            return
    ln()
    print(f'O produto {nome_produto} não foi encontrado no catálogo.')
    
    ln()
  
def add_novo_produto():

    if not admin():
        ln()
        print("Acesso Negado, você não e Admin")
        ln()
        return
    ln()
    print("Adicione novo produto: ")
    ln()
    nome = input('Digite o nome do novo produto: ')
    ln()
    preco = float(input('Digite o preço do novo produto: '))
    ln()
    descricao = input('Digite a descrição do novo produto: ')
    ln()
    quantidade = int(input('Digite a quantidade inicial em estoque: '))
    ln()
    
    novo_produto = {'nome': nome, 'preco': preco, 'descricao': descricao, 'quantidade': quantidade}
    produtos.append(novo_produto)
    ln()
    print(f'Produto {nome} adicionado ao catálogo.')
    ln()

def listar_produtos():
    ln()
    print('Catálogo de Produtos:')
    ln()
    for i in produtos:
        ln()
        print(f"Nome: {i['nome']} | Preço: R${i['preco']} | Descrição: {i['descricao']}")
        ln()

def adicionar_ao_carrinho():
    ln()
    print('Adicionar Produto ao Carrinho:')
    ln()
    nome_produto = input('Digite o nome do produto que deseja adicionar ao carrinho: ')
    ln()
    quantidade = int(input('Digite a quantidade desejada: '))
    ln()
    
    for i in produtos:
        if i['nome'] == nome_produto:
            if i['quantidade'] >= quantidade:
                if nome_produto in carrinho:
                    carrinho[nome_produto] += quantidade
                else:
                    carrinho[nome_produto] = quantidade
                i['quantidade'] -= quantidade
                ln()
                print(f'{quantidade} unidades do produto {nome_produto} adicionadas ao carrinho.')
                ln()
                return
            else:
                ln()
                print(f'Quantidade insuficiente em estoque para {nome_produto}.')
                ln()
                return
    ln()
    print(f'O produto {nome_produto} não foi encontrado no catálogo.')
    ln()

def remover_do_carrinho():
    ln()
    print('Remover Produto do Carrinho:')
    ln()
    nome_produto = input('Digite o nome do produto que deseja remover do carrinho: ')
    quantidade = int(input('Digite a quantidade a ser removida: '))
    
    if nome_produto in carrinho:
        if quantidade >= carrinho[nome_produto]:
            produtos.append({'nome': nome_produto, 'quantidade': quantidade})
            del carrinho[nome_produto]
        else:
            carrinho[nome_produto] -= quantidade
            for produto in produtos:
                if produto['nome'] == nome_produto:
                    produto['quantidade'] += quantidade
        ln()            
        print(f'{quantidade} unidades do produto {nome_produto} removidas do carrinho.')
        ln()
    else:
        ln()
        print(f'O produto {nome_produto} não está no carrinho.')
        ln()

def visualizar_carrinho():
    total = 0
    ln()
    print('Produtos no Carrinho:')
    ln()
    for i, y in carrinho.items():
        ln()
        print(f"{i}: {y} unidades")
        ln()
        for u in produtos:
            if u['nome'] == i:
                total += u['preco'] * y
    ln()           
    print(f'Valor total a pagar: R${total}')
    ln()

def processo_de_compra():
    ln()
    print('Processo de Compra:')
    ln()
    if not carrinho:
        ln()
        print('Seu carrinho está vazio. Adicione produtos antes de finalizar a compra.')
        ln()
        return
    
    nome_usuario = input('Digite seu nome para finalizar a compra: ')
    for i in usuario:
        if i['nome'] == nome_usuario:
            break
    else:
        ln()
        print('Usuário não encontrado.')
        ln()
        return
    ln()
    print(f'Compra realizada com sucesso por {nome_usuario}!')
    ln()
    compras.append({'usuario': nome_usuario, 'carrinho': carrinho.copy()})
    carrinho.clear()

def historico_de_compras():
    ln()
    print('Histórico de Compras:')
    ln()
    for x in compras:
        ln()
        print(f'Usuário: {x["usuario"]}')
        ln()
        for produto, quantidade in x['carrinho'].items():
            ln()
            print(f'{produto}: {quantidade} unidades')
            ln()
        ln()

def admin_login():
    usuario = input('Digite o nome de usuário admin: ')
    senha = input('Digite a senha admin: ')
    if usuario in admin and admin[usuario] == senha:
        return True
    return False


# Exemplo de uso das funções:

while True:
    ln()
    print("\n== Sistema de E-commerce ==")
    ln()
    print("1. Cadastro de Usuário")
    ln()
    print("2. Login de Usuário")
    ln()
    print("3. Administração de Estoque")
    ln()
    print("4. Catálogo de Produtos")
    ln()
    print("5. Adicionar Produtos ao Carrinho")
    ln()
    print("6. Remover Produtos do Carrinho")
    ln()
    print("7. Visualização de Carrinho")
    ln()
    print("8. Processo de Compra")
    ln()
    print("9. Histórico de Compras")
    ln()
    print("0. Sair")
    ln()

    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':
        cadastro_usuario()
    elif opcao == '2':
        if login():
            ln()
            print('Usuário autenticado!')
            ln()
        else:
            ln()
            print('Falha na autenticação.')
            ln()
    elif opcao == '3':
        if admin_login():
            ln()
            print('Acesso autorizado como administrador.')
            ln()
            print('1. Atualizar Estoque')
            ln()
            print('2. Adicionar Novo Produto')
            ln()
            admin_opcao = input('Digite a opção desejada: ')
            if admin_opcao == '1':
                admin_at_estoque()
            elif admin_opcao == '2':
                admin_at_estoque()
            else:
                ln()
                print('Opção inválida.')
                ln()
        else:
            ln()
            print('Acesso não autorizado!')
            ln()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        adicionar_ao_carrinho()
    elif opcao == '6':
        remover_do_carrinho()
    elif opcao == '7':
        visualizar_carrinho()
    elif opcao == '8':
        processo_de_compra()
    elif opcao == '9':
        historico_de_compras()
    elif opcao == '0':
        ln()
        print('Saindo do sistema...')
        ln()
        break
    else:
        ln()
        print('Opção inválida. Por favor, escolha novamente.')
        ln()