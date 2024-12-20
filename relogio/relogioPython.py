import tkinter as tk
from time import strftime

class RelogioDigital:
    def __init__(self, master):
        self.master = master
        self.master.title("RelÃ³gio Digital Python")

        self.rotulo_relogio = tk.Label(
            master,
            font=("Comic Sans", 30, "bold"),
            background="light green",
            foreground="black"
        )
        self.rotulo_relogio.pack(anchor="center")

        self.atualizar_relogio()

    def atualizar_relogio(self):
        horario_atual = strftime("%H:%M:%S %p")
        self.rotulo_relogio.config(text=horario_atual)
        self.rotulo_relogio.after(1000, self.atualizar_relogio)

if __name__ == "__main__":
    janela = tk.Tk()
    relogio = RelogioDigital(janela)
    janela.mainloop()