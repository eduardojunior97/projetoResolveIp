
input = input('Informe o IP: ')
#input = '172.17.135.233/25'

#Separar o IP da máscara (bitcount) (172.17.135.233/25)
separar = input.split('/')
ip = separar[0]
mascara = separar[1]

#Converter o IP para binário
#Separar cada octeto (A,B,C e D)
octeto = ip.split('.')
a = octeto[0]
b = octeto[1]
c = octeto[2]
d = octeto[3]

#Converte cada octeto para binário (Abin, Bbin, Cbin, Dbin)
Abin = bin(int(a))[2:]
Bbin = bin(int(b))[2:]
Cbin = bin(int(c))[2:]
Dbin = bin(int(d))[2:]

#Converte cada binário em string, com 8 caracteres completando com 0 a esquerda
AbinStr = Abin.zfill(8) #acrescenta zero a esquerda
BbinStr = Bbin.zfill(8)
CbinStr = Cbin.zfill(8)
DbinStr = Dbin.zfill(8)

#Concatenar AbinStr, BbinStr, CbinStr, DbinStr
IPbinStr = AbinStr + BbinStr + CbinStr + DbinStr

print('-'*65)
print('IP convertido para binário: ', IPbinStr)
print('-'*65)

#Identificar o IP de rede
Nmascara = int(mascara)
NetbinStr = IPbinStr[:Nmascara] 
NetbinStr = NetbinStr.ljust(32,'0') #acrescenta a direita os zeros

print('NET em binário: ', NetbinStr)
print('-'*65)

#Converter para decimal em 4 octetos
#A = bintodec(substr(NetbinStr, 1,8))   = bintodec("10101100") = 172
PrimeiroOcteto = NetbinStr[0:8]
SegundoOcteto  = NetbinStr[8:16]
TerceiroOcteto = NetbinStr[16:24]
QuartoOcteto   = NetbinStr[24:32]

#converte de binario para decimal :http://ptcomputador.com/P/python-programming/93577.html
Adec = int(PrimeiroOcteto,2) 
Bdec = int(SegundoOcteto,2)
Cdec = int(TerceiroOcteto,2)
Ddec = int(QuartoOcteto,2)

IP_rede = str(Adec) +'.'+ str(Bdec) +'.'+ str(Cdec) +'.'+ str(Ddec) + '/' + mascara
print('IP da rede: :', IP_rede)
print('-'*65)

Default_gateway = str(Adec) +'.'+ str(Bdec) +'.'+ str(Cdec) +'.'+ str(Ddec +1)
print('Default Gateway:', Default_gateway)
print('-'*65)
