import datetime

# Dados do usuário
dados = {'login': [], 'senha': []}

for n in range(1, 2):
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    dados['login'].append(login)
    dados['senha'].append(senha)
print(dados)

l = [1, 2]
historico = []

for i in l:
    login_usuario = input('Digite o login: ')
    senha = input('Digite a senha: ')

    if login_usuario in dados['login']:
        index = dados['login'].index(login_usuario)
        if senha == dados['senha'][index]:
            print('Acesso liberado')
            saldo = 1000
            print(f'Saldo inicial: {saldo}')
            
            while True: 
                print('\nO que deseja fazer?')
                print('1- Depositar')
                print('2- Sacar')
                print('3- Ver extrato')
                print('4- Sair do aplicativo')
                
                acao = int(input('Escolha uma opção: '))
                
                if acao == 1:
                    deposito = float(input('Insira o valor do depósito: '))
                    saldo += deposito
                    historico.append({
                        'acao': 'Depósito',
                        'valor': deposito,
                        'saldo_atual': saldo,
                        'data_hora': datetime.datetime.now()
                    })
                    print(f'Depósito realizado. Seu saldo agora é de {saldo}')
                
                elif acao == 2:
                    quantidade_saq = float(input('Qual valor do saque? '))
                    if quantidade_saq <= saldo:
                        saldo -= quantidade_saq
                        historico.append({
                            'acao': 'Saque',
                            'valor': quantidade_saq,
                            'saldo_atual': saldo,
                            'data_hora': datetime.datetime.now()
                        })
                        print(f'Saque realizado. Seu saldo agora é de: {saldo}')
                    else:
                        print('Saldo insuficiente para o saque.')
                
                elif acao == 3:
                    print("\n--- Extrato ---")
                    for item in historico:
                        print(f"{item['data_hora']} - {item['acao']} de {item['valor']} | Saldo atual: {item['saldo_atual']}")
                    
                    print('\nDeseja continuar? (1- Sim / 2- Não)')
                    acaoopcao = int(input())
                    if acaoopcao == 2:
                        print('Até logo!')
                        break  
                   
                
                elif acao == 4:
                    print('Até logo!!')
                    exit()  
                
                else:
                    print('Opção inválida. Tente novamente.')
            
            break 
        else:
            print('Senha incorreta')
    else:
        print('Login não encontrado')

else:
    print('Conta bloqueada')