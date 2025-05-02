import tkinter as tk
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)

        if imc < 18.5:
            resultado = 'Você esta com baixo peso'
        elif imc <= 24.9:
            resultado = 'Seu peso esta normal'
        elif imc <=29.9:
            resultado = 'Você está com sobrepeso'
        elif imc <=34.9:
            resultado = 'Obesidade grau 1 '
        elif imc <= 39.9:
            resultado = 'Obesidade grau 2 '
        else:
            resultado = 'Obesidade grau 3 '

        rotulo_resultado.config(text=f"imc: {imc:.2f}\n{resultado}")
    except ValueError:
        rotulo_resultado.config(text="Por favor insira valores válidos.")

janela = tk.Tk()
janela.title('Calculadora de IMC')
tk.Label(janela, text='peso (kg):').pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

tk.Label(janela, text="Altura (m):").pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()

botao_calcular = tk.Button(janela, text="Calcular IMC",command=calcular_imc)
botao_calcular.pack(pady=10)

rotulo_resultado = tk.Label(janela, text="")
rotulo_resultado.pack()
janela.mainloop()