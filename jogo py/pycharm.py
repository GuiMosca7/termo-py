import tkinter as tk
from tkinter import messagebox
import random

# Lista de palavras
palavras = ["chaves", "tabelas", "cedula", "delete", "script"]

class JogoAdivinhacao:
    def __init__(self, master):
        self.master = master
        master.title("Jogo de Adivinhação")
        master.geometry("400x300")
        master.config(bg="#282c34")

        self.palavra_secreta = random.choice(palavras)
        self.tentativas = 0

        # Título
        self.titulo = tk.Label(master, text="Adivinhe a Palavra!", font=("Helvetica", 20, "bold"), fg="white", bg="#282c34")
        self.titulo.pack(pady=20)

        # Dica sobre número de letras
        self.dica = tk.Label(master, text=f"A palavra tem {len(self.palavra_secreta)} letras.", font=("Helvetica", 14), fg="#61dafb", bg="#282c34")
        self.dica.pack(pady=5)

        # Entrada para o palpite
        self.entrada = tk.Entry(master, font=("Helvetica", 16))
        self.entrada.pack(pady=10)
        self.entrada.focus()

        # Botão para tentar adivinhar
        self.botao_tentar = tk.Button(master, text="Tentar", font=("Helvetica", 14), bg="#61dafb", fg="black", command=self.verificar_palpite)
        self.botao_tentar.pack(pady=10)

        # Label para feedback do jogo
        self.mensagem = tk.Label(master, text="", font=("Helvetica", 14), fg="white", bg="#282c34")
        self.mensagem.pack(pady=10)

        # Botão desistir
        self.botao_desistir = tk.Button(master, text="Desistir", font=("Helvetica", 12), bg="#ff4c4c", fg="white", command=self.desistir)
        self.botao_desistir.pack(pady=5)

    def verificar_palpite(self):
        palpite = self.entrada.get().strip().lower()
        self.tentativas += 1

        if palpite == self.palavra_secreta:
            messagebox.showinfo("Parabéns!", f"Você acertou a palavra '{self.palavra_secreta}' em {self.tentativas} tentativas!")
            self.master.destroy()
        else:
            self.mensagem.config(text="Errado! Tente novamente.")
            self.entrada.delete(0, tk.END)

    def desistir(self):
        if messagebox.askyesno("Desistir", f"Tem certeza que quer desistir?\nA palavra era '{self.palavra_secreta}'."):
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
