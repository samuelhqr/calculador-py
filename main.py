import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg="black")
        
        self.visor = tk.Entry(root, font=("Arial", 20), bg="black", fg="white")
        self.visor.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        
        for (texto, linha, coluna) in botoes:
            botao = tk.Button(root, text=texto, font=("Arial", 20), bg="black", fg="white", command=lambda t=texto: self.on_click_botao(t))
            botao.grid(row=linha, column=coluna, sticky="nsew")
        
       
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
       
        self.expressao = ''
    
    def on_click_botao(self, texto):
        if texto == '=':
            try:
                resultado = eval(self.expressao)
                self.visor.delete(0, tk.END)
                self.visor.insert(tk.END, str(resultado))
                self.expressao = str(resultado)
            except Exception as e:
                self.visor.delete(0, tk.END)
                self.visor.insert(tk.END, "Erro")
                self.expressao = ''
        else:
            self.expressao += texto
            self.visor.insert(tk.END, texto)
        

if __name__ == "__main__":
    janela = tk.Tk()
    app = Calculadora(janela)
    janela.mainloop()
