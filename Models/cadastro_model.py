import json


class Cadastro_model:
    def __init__(self):
        self.dir = None

    def salvar(self, nome, email, cpf, telefone):
        try:
            with open("../dados_clientes.json", mode='r') as file:
                registro = json.load(file)
                dados = {
                    "nome": nome,
                    "email": email,
                    "cpf": cpf,
                    "telefone": telefone
                }
                registro.append(dados)
                self.dir = open("../dados_clientes.json", 'w')
                json.dump(registro, self.dir, indent=6)
                self.dir.close()
        except Exception as e:

            print(e)
