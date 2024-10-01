import sys
print(sys.executable)
print(sys.version)
from flask import Flask, render_template, request, redirect, url_for
from estacionamento import Estacionamento

app = Flask(__name__)

# Inicializando o estacionamento
parking = Estacionamento(preco_inicial=0, preco_hora=1.5, lista_veiculos=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        placa = request.form['placa']
        if parking.adicionar_veiculo(placa.upper()):
            return redirect(url_for('listar_veiculos'))
        else:
            error = "Formato de placa inválido! A placa deve ter 3 letras seguidas de 4 números."
            return render_template('adicionar.html', error=error)
    return render_template('adicionar.html')

@app.route('/remover', methods=['GET', 'POST'])
def remover_veiculo():
    if request.method == 'POST':
        placa = request.form['placa']
        if parking.remover_veiculo(placa.upper()):
            horas = int(request.form['horas'])
            total = float(parking.calcular_valor(horas))
            total_formatado = f"{total:.2f}"
            return render_template('remover.html', total=total_formatado, placa=placa)
        else:
            error = "Veículo não encontrado!"
            return render_template('remover.html', error=error)
    return render_template('remover.html')

@app.route('/listar')
def listar_veiculos():
    veiculos = parking.listar_veiculos()
    return render_template('listar.html', veiculos=veiculos)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
"""     
 http://127.0.0.1:5000/  página inicial.

adicionar um veículo acessando http://127.0.0.1:5000/adicionar

Liste os veículos em http://127.0.0.1:5000/listar

remover um veículo em http://127.0.0.1:5000/remover

"""
