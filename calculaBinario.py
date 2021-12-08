
ip = "172.20.17.23"  # str(input("Digite seu ip: \n")) #Recebendo o IP
listIp = ip.split(".")  # Convertendo a string em lista separando por pontos
# int(input("Digite a mascara de rede: \n")) # Recebendo mascara de rede
mask = 25

# função que converta em binari
def converteBinario(numeroBinarios):
    for i in range(len(numeroBinarios)):  # Laço para percorrer os index da lista
        # Transforma o item corrente em inteiro
        numeroBinarios[i] = int(numeroBinarios[i])
        # Transforma o item em um binário
        numeroBinarios[i] = bin(numeroBinarios[i])
        # Pega apenas o caracteres a partir do segundo até o final
        numeroBinarios[i] = numeroBinarios[i][2:]

    return numeroBinarios  # Retorna a lista em binario em string

def verificaZeros(binarios):
    for i in range(len(binarios)):  # Laço para percorrer os index da lista
        if len(binarios[i]) < 8:  # Verifica se o item corrente é maior que 8
            # Verifica quantos zeros vai precisar adicionar
            num = 8 - len(binarios[i])
            num = "0" * num  # Atribui os zeros a variavel
            # Atribui os zeros ao numero binario
            binarios[i] = num + binarios[i]

    return binarios  # Retorna a lista com os zeros preenchidos


def calculaMascara(ipBinario):  # Recebe um ip em string
    rede = list(ipBinario)  # Converte ele para lista
    mascara = 32 - mask  # Calculo para descobrir quantos 0 substituir nos octetos
    num = "0" * mascara  # Atribuindo os zeros a uma variável

    rede.reverse()
    for i in range(len(num)):
        rede[i] = "0"
    
    rede.reverse()

    for i in range(len(num)):  # Faz laço com o número de zeros, removendo o último item da lista
        rede.pop(-1)

    rede = "".join(rede)  # Transfoma a lista  com o itens removidos em string
    rede = rede + num  # Concatera os zeros no final da string

    return rede  # Retorna uma um ip em string


# Recebe uma sitring de 1 octeto do número binario
def transformaDecimal(numeroBinario):
    numDecimal = []  # Cria uma lista vazia
    # Calcula o numero de elementos -1 para a exponenciação
    pot = len(numeroBinario) - 1

    # Transfoma a string binario em lista, e faz um laço para  percorrer cada item
    for i in list(numeroBinario):
        num = int(i)  # Transforma o item corrente em inteiro
        num = num * (2 ** pot)  # Faz o calculo do primeiro numero para decimal
        pot -= 1  # Reduz 1 na potencia
        numDecimal.append(num)  # Atribui o primeiro valor em uma lista

    return sum(numDecimal)  # Soma toda a lista para retornar o número decimal
