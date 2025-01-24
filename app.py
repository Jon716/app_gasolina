from flask import Flask, render_template, request

app = Flask(__name__)

# Função para calcular o custo da gasolina
def calcular_custo_gasolina(distancia, preco_gasolina=6.50, consumo_medio=10):
    litros_necessarios = distancia / consumo_medio
    custo_total = litros_necessarios * preco_gasolina
    return custo_total

# Rota principal para exibir o formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Obtém a distância do formulário
            distancia = float(request.form['distancia'])
            # Calcula o custo
            custo = calcular_custo_gasolina(distancia)
            # Exibe o resultado na página
            return render_template('index.html', custo=f'R$ {custo:.2f}')
        except ValueError:
            return render_template('index.html', erro="Por favor, insira um valor numérico válido.")
    return render_template('index.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa a porta definida pelo Render
    app.run(host='0.0.0.0', port=port)
