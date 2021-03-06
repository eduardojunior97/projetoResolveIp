from flask import request
from flask.app import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Ips(Resource):

    def post(self):

        print('=' * 100)
        entrada = request.json['ip_address']
        print('=' * 100)
        address = entrada.split("-")
        ip = address[0]
        bitcount = address[1]

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

        gateway = converter_binario_para_decimal(identificacao, 1)
        id_rede = converter_binario_para_decimal(identificacao)

        rede = id_rede + '-' + bitcount
        return {'rede': rede, 'gateway': gateway}


class Lista_ip(Resource):
    def get(self, rede):
        entrada = request.json['ip_address']
        address = entrada.split("-")
        ip = address[0]
        bitcount = address[1]

        def decimal_to_binary(ip):
            ip = '.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')])
            abin = ip[:8]
            bbin = ip[9:17]
            cbin = ip[18:26]
            dbin = ip[27:35]
            resultado = abin + bbin + cbin + dbin
            return resultado

        var_decimal_binary = decimal_to_binary(ip)

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

        def converter_binario_para_decimal(identificacao, num=0):
            AbinStr = str(int(identificacao[0:8], 2))
            BbinStr = str(int(identificacao[8:16], 2))
            CbinStr = str(int(identificacao[16:24], 2))
            DbinStr = str(int(identificacao[24:32], 2) + num)
            return AbinStr + "." + BbinStr + "." + CbinStr + "." + DbinStr

        gateway = converter_binario_para_decimal(identificacao, 1)
        id_rede = converter_binario_para_decimal(identificacao)

        rede = id_rede + '-' + bitcount
        return {'rede': rede, 'gateway': gateway}


# decorador
api.add_resource(Ips, '/newzin')
api.add_resource(Lista_ip, '/newzin/<int:rede>/<int:gateway>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="5000")
