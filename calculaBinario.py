
ip = "172.20.17.23" #str(input("Digite seu ip: \n")) #Recebendo o IP
listIp = ip.split(".") # Convertendo a string em lista separando por pontos
mask = 25 #int(input("Digite a mascara de rede: \n")) # Recebendo mascara de rede

#função que converta em binario
def converteBinario(numeroBinarios):
    for i in range(len(numeroBinarios)): # Laço para percorrer os index da lista
        numeroBinarios[i] = int(numeroBinarios[i]) # Transforma o item corrente em inteiro
        numeroBinarios[i] = bin(numeroBinarios[i]) # Transforma o item em um binário
        numeroBinarios[i] = numeroBinarios[i][2:] # Pega apenas o caracteres a partir do segundo até o final
    
    return numeroBinarios # Retorna a lista em binario em string

print('OLA')

def verificaZeros(binarios):
    for i in range(len(binarios)): # Laço para percorrer os index da lista
        if len(binarios[i]) < 8: # Verifica se o item corrente é maior que 8
            num = 8 - len(binarios[i]) # Verifica quantos zeros vai precisar adicionar
            num = "0" * num # Atribui os zeros a variavel
            binarios[i] = num + binarios[i] # Atribui os zeros ao numero binario
        
    return binarios # Retorna a lista com os zeros preenchidos

def calculaMascara(ipBinario): #Recebe um ip em string
    rede = list(ipBinario) #Converte ele para lista
    mascara = 32 - mask #Calculo para descobrir quantos 0 substituir nos octetos
    num = "0" * mascara # Atribuindo os zeros a uma variável
 

