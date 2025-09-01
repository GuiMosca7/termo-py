import tkinter as tk
from tkinter import messagebox
import random

# Lista de palavras
palavras = ["chaves", "tabelas", "cedula", "delete", "script"]
# Dicas das palavras
dicas_palavras = {
    "chaves": "Serve para abrir portas.",
    "tabelas": "Usado para organizar dados em linhas e colunas.",
    "cedula": "Um tipo de papel usado como dinheiro.",
    "delete": "Comando para apagar algo.",
    "script": "Conjunto de instruções em programação."
}

class JogoAdivinhacao:
    def __init__(self, master):
        self.master = master
        master.title("Jogo de Adivinhação Sinistra")
        master.geometry("500x500")
        master.config(bg="#0d0d0d")

        self.inicializar_jogo()

        # Estilo
        fonte_titulo = ("Helvetica", 20, "bold")
        fonte_normal = ("Helvetica", 14)
        cor_fundo = "#0d0d0d"
        cor_destaque = "#e60000"
        cor_azul_fantasma = "#8a2be2"

        # Título
        self.titulo = tk.Label(master, text="ADIVINHE SE PUDER!", font=fonte_titulo, fg=cor_destaque, bg=cor_fundo)
        self.titulo.pack(pady=10)

        # Dica de tamanho da palavra
        self.dica = tk.Label(master, text="", font=fonte_normal, fg=cor_azul_fantasma, bg=cor_fundo)
        self.dica.pack(pady=5)

        # Label contador de tentativas
        self.label_tentativas = tk.Label(master, text="", font=fonte_normal, fg="white", bg=cor_fundo)
        self.label_tentativas.pack(pady=5)

        # Entrada
        self.entrada = tk.Entry(master, font=("Courier New", 16), fg="white", bg="#262626", insertbackground="white", justify="center", relief="flat")
        self.entrada.pack(pady=10, ipady=5, ipadx=10)
        self.entrada.focus()

        # Botão Tentar
        self.botao_tentar = tk.Button(master, text="⚔️ Tentar Sorte", font=fonte_normal, bg=cor_destaque, fg="white",
                                      activebackground="#990000", activeforeground="white", command=self.verificar_palpite, relief="flat")
        self.botao_tentar.pack(pady=10, ipadx=10, ipady=5)

        # Histórico de tentativas
        self.historico = tk.Text(master, height=10, font=fonte_normal, fg="white", bg=cor_fundo, relief="flat")
        self.historico.pack(pady=5)
        self.historico.config(state=tk.DISABLED)

        # Cores para o histórico
        self.historico.tag_configure("verde", foreground="green")
        self.historico.tag_configure("amarelo", foreground="yellow")
        self.historico.tag_configure("cinza", foreground="gray")

        ## Botão Dica
        self.botao_dica = tk.Button(master, text="💡 Dica", font=fonte_normal, bg="#ffaa00", fg="black",
                           activebackground="#cc8800", activeforeground="black", command=self.mostrar_dica, relief="flat")
        self.botao_dica.pack(pady=5, ipadx=10, ipady=5)


        # Dica extra
        self.dica_primeira_letra = tk.Label(master, text="", font=fonte_normal, fg="#ffa500", bg=cor_fundo)
        self.dica_primeira_letra.pack(pady=5)

        # Botão Desistir
        self.botao_desistir = tk.Button(master, text="💀 Desistir", font=("Helvetica", 12), bg="#444", fg="white",
                                        activebackground="#222", activeforeground="#ff4c4c", command=self.desistir, relief="flat")
        self.botao_desistir.pack(pady=5, ipadx=10, ipady=3)

        # Dica textual
        self.dica_completa = tk.Label(master, text="", font=fonte_normal, fg="#ffb347", bg=cor_fundo)
        self.dica_completa.pack(pady=5)

        # Tecla Enter
        master.bind('<Return>', self.verificar_palpite_enter)

        self.reiniciar_jogo()

    def inicializar_jogo(self):
        self.palavra_secreta = random.choice(palavras)
        self.tentativas = 0
        self.tamanho_esperado = len(self.palavra_secreta)
        self.dica_textual = dicas_palavras[self.palavra_secreta]

    def verificar_palpite(self):
        palpite = self.entrada.get().strip().lower()

        if not palpite.isalpha():
            messagebox.showinfo("Aviso", "Use apenas letras!")
            self.entrada.delete(0, tk.END)
            return

        self.tentativas += 1
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}")

        if self.tentativas == 5:
            primeira_letra = self.palavra_secreta[0].upper()
            self.dica_primeira_letra.config(text=f"Dica Extra: A palavra começa com a letra '{primeira_letra}'.")

        if palpite == self.palavra_secreta:
            messagebox.showinfo("Parabéns!", f"Você acertou a palavra '{self.palavra_secreta}' em {self.tentativas} tentativas!")
            jogar_novamente = messagebox.askyesno("Novo Jogo?", "Deseja jogar novamente?")
            if jogar_novamente:
                self.reiniciar_jogo()
            else:
                self.master.destroy()
        else:
            self.mostrar_dica_colorida(palpite)
            self.entrada.delete(0, tk.END)

    def mostrar_dica_colorida(self, palpite):
        palavra_temp = list(self.palavra_secreta)
        resultado = [None] * len(palpite)

        # Letras corretas no lugar certo
        for i in range(len(palpite)):
            if i < len(self.palavra_secreta) and palpite[i] == self.palavra_secreta[i]:
                resultado[i] = ("verde", palpite[i])
                palavra_temp[i] = None
            else:
                resultado[i] = (None, palpite[i])

        # Letras corretas no lugar errado
        for i in range(len(palpite)):
            cor, letra = resultado[i]
            if cor is not None:
                continue
            if letra in palavra_temp:
                resultado[i] = ("amarelo", letra)
                palavra_temp[palavra_temp.index(letra)] = None
            else:
                resultado[i] = ("cinza", letra)

        self.historico.config(state=tk.NORMAL)
        for cor, letra in resultado:
            self.historico.insert(tk.END, letra.upper() + " ", cor)
        self.historico.insert(tk.END, "\n")
        self.historico.config(state=tk.DISABLED)

    def verificar_palpite_enter(self, event):
        self.verificar_palpite()

    def mostrar_dica(self):
        messagebox.showinfo("Dica", self.dica_textual)

    def desistir(self):
        if messagebox.askyesno("👻 Desistir?", f"Tem certeza? A palavra era: '{self.palavra_secreta}'."):
            self.master.destroy()

    def reiniciar_jogo(self):
        self.inicializar_jogo()
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}")
        self.dica.config(text=f"A palavra tem {self.tamanho_esperado} letras.")
        self.dica_primeira_letra.config(text="")
        self.dica_completa.config(text="")  # só aparece se você quiser
        self.entrada.delete(0, tk.END)
        self.historico.config(state=tk.NORMAL)
        self.historico.delete("1.0", tk.END)
        self.historico.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
