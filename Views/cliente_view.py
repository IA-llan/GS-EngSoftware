from PyQt6 import uic, QtWidgets
from Controllers.cadastro_controller import Cadastro_controller
from Controllers.infos_cotroller import Info_controller


class Cliente_view:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.primeira_tela = uic.loadUi("cadastro.ui")
        self.segunda_tela = uic.loadUi("produtos_view.ui")
        self.primeira_tela.pushButton.clicked.connect(self.cadastrar)
        self.primeira_tela.pushButton.clicked.connect(self.new_window)
        self.segunda_tela.pushButton.clicked.connect(self.index1)
        self.segunda_tela.pushButton_2.clicked.connect(self.index2)
        self.segunda_tela.pushButton_3.clicked.connect(self.index3)
        self.segunda_tela.pushButton_4.clicked.connect(self.index4)

        self.primeira_tela.show()
        app.exec()

    def new_window(self):
        self.primeira_tela.hide()
        self.segunda_tela.show()

    def cadastrar(self):
        print("Salvando dados...")
        nome = self.primeira_tela.lineEdit.text()
        email = self.primeira_tela.lineEdit_2.text()
        cpf = self.primeira_tela.lineEdit_3.text()
        telefone = self.primeira_tela.lineEdit_4.text()
        controller = Cadastro_controller()
        controller.salvar(nome, email, cpf, telefone)
        print(f"Salvo: {nome}, {email}, {cpf}, {telefone}")

    def index1(self):
        index = Info_controller()
        index.get_index(1)

    def index2(self):
        index = Info_controller()
        index.get_index(2)

    def index3(self):
        index = Info_controller()
        index.get_index(3)

    def index4(self):
        index = Info_controller()
        index.get_index(4)


Cliente_view()
