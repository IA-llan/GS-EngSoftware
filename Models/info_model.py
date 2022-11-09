import json


class Info_model:
    def __init__(self):
        self.info = None

    def infos(self, index):
        with open("../dados_produtos.json", mode='r', encoding='utf-8') as file:
            registro = json.load(file)

            for item in registro[0][f'Item {index}']:
                print(f"{item}: {registro[0][f'Item {index}'][item]}")
