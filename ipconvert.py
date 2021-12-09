
#--------------------------------------
#Novos comentarios para calcula binario
#--------------------------------------

#--------------------------------------
#Novos comentarios para calcula binario
#--------------------------------------

# ip = 172.17.135.233/25
#
print('=' * 100)
entrada = str(input('Digite o IP: '))
print('=' * 100)
address = entrada.split("/")
ip = address[0]
bitcount = address[1]


# print(f'Testando máscara... {bitcount}')

def decimal_to_binary(ip):
    ip = '.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')])
    abin = ip[:8]
    bbin = ip[9:17]
    cbin = ip[18:26]
    dbin = ip[27:35]
    resultado = abin + bbin + cbin + dbin
    return resultado


var_decimal_binary = decimal_to_binary(ip)
print(f'Convertido os bits com o 0 a esquerda {var_decimal_binary}')


# Tentando alocar os ZEROS na rede
def identificar_ip_rede(num_convertido, bitcount):
    quantidade = 32 - int(bitcount)
    zeros = ""
    for i in range(quantidade):
        zeros = zeros + "0"
    # soma = num_convertido + zeros #
    soma = num_convertido[:int(bitcount)] + zeros
    return soma


# Chamando função do método de identificação de rede
identificacao = identificar_ip_rede(var_decimal_binary, bitcount)
print(f'Alocando a quantidade de 0 a esquerda {identificacao}')


def converter_binario_para_decimal(identificacao, num=0):
    AbinStr = str(int(identificacao[0:8], 2))
    BbinStr = str(int(identificacao[8:16], 2))
    CbinStr = str(int(identificacao[16:24], 2))
    DbinStr = str(int(identificacao[24:32], 2) + num)
    return AbinStr + "." + BbinStr + "." + CbinStr + "." + DbinStr


binary_to_decimal = converter_binario_para_decimal(identificacao, 1)
gateway = converter_binario_para_decimal(identificacao)
print(f'Ip convertido para decimal. ID da rede: {gateway}/{bitcount}')
print(f'Default Gateway {binary_to_decimal}')

print("=*", 90)
