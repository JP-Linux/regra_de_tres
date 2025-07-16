import tkinter as tk


def calcular():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        x = (b * c) / a

        label_resultado.config(text=str(x))

    except:
        label_resultado.config(text="Error")


janela = tk.Tk()
janela.title("Calculadora Proporcional")

# Primeira linha
quadro1 = tk.Frame(janela)
quadro1.pack(pady=10)

entrada_a = tk.Entry(quadro1, width=5, font=("Arial", 14))
entrada_a.pack(side=tk.LEFT, padx=10)

tk.Label(quadro1, text="ESTÁ PARA", font=(
    "Arial", 12)).pack(side=tk.LEFT, padx=10)

entrada_b = tk.Entry(quadro1, width=5, font=("Arial", 14))
entrada_b.pack(side=tk.LEFT, padx=10)

# Segunda linha
tk.Label(janela, text="ASSIM COMO", font=("Arial", 12)).pack(pady=10)

# Terceira linha
quadro2 = tk.Frame(janela)
quadro2.pack(pady=10)

entrada_c = tk.Entry(quadro2, width=5, font=("Arial", 14))
entrada_c.pack(side=tk.LEFT, padx=10)

tk.Label(quadro2, text="ESTÁ PARA", font=(
    "Arial", 12)).pack(side=tk.LEFT, padx=10)

label_resultado = tk.Label(quadro2, text="X", font=("Arial", 14))
label_resultado.pack(side=tk.LEFT, padx=10)

# Botão de cálculo
btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack(pady=15)

janela.mainloop()
