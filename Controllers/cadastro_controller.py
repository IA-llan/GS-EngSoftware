from Models import cadastro_model
import tkinter as tk
from tkinter import ttk

NORM_FONT = ("Verdana", 10)


class Cadastro_controller:
    def __init__(self):
        self.cliente = cadastro_model.Cadastro_model()

    def salvar(self, nome, email, cpf, telefone):
        if nome is not None and email is not None and cpf is not None and telefone is not None:
            self.cliente.salvar(nome, email, cpf, telefone)
        else:
            self.popupmsg("Insira valores válidos")

    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        b1.pack()
        popup.mainloop()
