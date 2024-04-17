from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# a linha abaixo cria a chave de segurança
app.secret_key = 'aprendendodoiniciocomdaniel'

# ** a linha abaixo configura o acesso ao banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'cmb110205',
        servidor = 'localhost',
        database = 'loja'
    )

# a linha abaixo cria uma instancia com o SQLALCHEMY
db = SQLAlchemy(app)

class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nome_produto = db.Column(db.String(50), nullable=False)

    marca_produto = db.Column(db.String(40), nullable=False)
    
    preco_produto = db.Column(db.Float, nullable=False) 

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/inicio')
def ola():
    return'<h1> Iniciando flask</h1>'


@app.route('/lista')
def lista():

    produtos_cadastrados = Produto.query.order_by(Produto.id_produto)

    return render_template('lista.html',
                           descricao="Aqui estão seus produtos cadastrados",
                           lista_prod = produtos_cadastrados)

@app.route('/cadastrar')
def cadastrar_produto():
    return render_template('cadastrar.html')


@app.route('/adiciona', methods=['POST',])
def adicionar_produto():
    
    # as variaveis abaixo recebem as informações digitadas 
    # pelo usuario
    nome_prod = request.form['TxtNome']
    marca_prod = request.form['TxtMarca']

    #a linha abaixo altera o (,) por (.)
    preco_prod = request.form['TxtPreco'].replace(',','.')
    
    # linha abaixo converto o valor digitado pelo usuario
    preco_prod = float(preco_prod)

    produto_adicionado = Produto(nome_produto = nome_prod,
                                 marca_produto = marca_prod,
                                 preco_produto = preco_prod)
    
    
    # a linha abaixo é feito um preparo para enviar para o banco
    db.session.add(produto_adicionado)

    db.session.commit()




    return render_template("lista.html",
                           descricao = "Novo produto cadastrado")

app.run()
