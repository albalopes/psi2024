from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    #return '<ul><li>Arroz</li></ul>'
    return render_template('compras.html', item1 = 'Farinha', item2='Cuscuz')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')

'''
@app.route('/gastos')
def gastos():
    mes = 'Fevereiro'
    valor = '843,00'
    return render_template('gastos.html', a = mes, b = valor)
'''

@app.route('/gastos/<mes>')
def gastos(mes):
    return render_template('gastos.html', a = mes)

@app.route('/q1_pedirpizza/<sabor>')
def q1_pedirpizza(sabor):
    return render_template('q1_pedirpizza.html' , sabor=sabor )

@app.route('/dobro', defaults={"n":0})
@app.route('/dobro/<int:n>')
@app.route('/dobro/<float:n>')
def dobro(n):
    resultado = 2*n
    return render_template('dobro.html', n=n, resultado=resultado)

@app.route('/perfil', defaults={'nome': 'anonimo'})
@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome)


@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['GET'])
#@app.route('/recebedados', methods=['POST'])
def recebedados():
    #nome = request.form['nome']
    #email = request.form['email']
    nome = request.args['nome']
    email = request.args['email']
    estado = request.args['estado']
    formacao = request.args['formacao']
    modalidades = request.args.getlist('modalidades')
    return render_template('recebedados.html', nome=nome, email=email, estado=estado, formacao=formacao, modalidades=modalidades)