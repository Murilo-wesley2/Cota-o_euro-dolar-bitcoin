import requests

#lista de opção
cotacoes=['Euro','Dolar','Bitcoin','Exit']

#fuções
def menu(texto):
    print('='*35)
    print(f'{texto:^35}')
    print('='*35)

def escolha(lista):
    for n,o in enumerate(lista):
        print(f'{n+1}-{o}')

#loop principal
while True:
     try:
         #envia a requisição e recebe o arquivo json 
        requisicao=requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

     except:
        print('\033[31mERRO:verifique sua conexcão com a internet\033[m')
    
     else:
           menu('cotações')
           escolha(cotacoes)
           try:
            opc=int(input('digite o numero da sua escolha:'))

           except:
            print('digite apenas numeros inteiros que estejam entre 1 é 4')
           else:
            #trasforma o arquivo json em dicionario
            dic_requisicao=requisicao.json()
            if opc==4:
                print('\033[33mencerrando o sistema\033[m')
                break
            elif opc == 3:
                cotacao = float(dic_requisicao['BTCBRL']['bid'])
                moeda='Bitcoin'
            elif opc == 2:
                cotacao = float(dic_requisicao['USDBRL']['bid'])
                moeda='Dolar'
            elif opc == 1:
                cotacao = float(dic_requisicao['EURBRL']['bid'])
                moeda='Euro'
            else:
                print('digite um numero entre 1 é 4')
    
            print(f'a cotação do {moeda} está em R$ {cotacao:.2f}')
