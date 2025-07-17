import tkinter as tk

def calcular():
    try:
        # Obter valores com tratamento de vírgula como separador decimal
        a = entrada_a.get().replace(',', '.')
        b = entrada_b.get().replace(',', '.')
        c = entrada_c.get().replace(',', '.')
        
        a = float(a) if a else 0
        b = float(b) if b else 0
        c = float(c) if c else 0
        
        # Validar entrada 'a' para evitar divisão por zero
        if a == 0:
            label_resultado.config(text="Erro: 'a' não pode ser zero")
            return
            
        x = (b * c) / a
        
        # Formatar resultado com 2 casas decimais
        label_resultado.config(text=f"{x:.2f}")

    except ValueError:
        label_resultado.config(text="Erro: Valores inválidos")
    except Exception as e:
        label_resultado.config(text=f"Erro: {str(e)}")

janela = tk.Tk()
janela.title("Calculadora Proporcional")

# Primeira linha
quadro1 = tk.Frame(janela)
quadro1.pack(pady=10)

entrada_a = tk.Entry(quadro1, width=8, font=("Arial", 14))
entrada_a.pack(side=tk.LEFT, padx=10)

tk.Label(quadro1, text="ESTÁ PARA", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

entrada_b = tk.Entry(quadro1, width=8, font=("Arial", 14))
entrada_b.pack(side=tk.LEFT, padx=10)

# Segunda linha
tk.Label(janela, text="ASSIM COMO", font=("Arial", 12)).pack(pady=10)

# Terceira linha
quadro2 = tk.Frame(janela)
quadro2.pack(pady=10)

entrada_c = tk.Entry(quadro2, width=8, font=("Arial", 14))
entrada_c.pack(side=tk.LEFT, padx=10)

tk.Label(quadro2, text="ESTÁ PARA", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

label_resultado = tk.Label(quadro2, text="X", font=("Arial", 14), width=8, relief="sunken", padx=5)
label_resultado.pack(side=tk.LEFT, padx=10)

# Botão de cálculo
btn_calcular = tk.Button(janela, text="Calcular", command=calcular, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_calcular.pack(pady=15)

janela.mainloop()