
from flask import Flask, render_template
#flask com f minusculo é a biblioteca, Flask com F maiusculo é a classe 

# a variavel abaixo é a variavel que roda a aplicação (todos os objetos de prjeto dependelm dela)
app = Flask(__name__)
#Varialvel da aplicação sempre pede __name__

# @ signfica criar uma rota
@app.route('/inicio')
def ola():
    return '<h1>Inciando Flask</h1>'

@app.route('/lista')
def lista():
    return render_template('lista.html')
#render template busca a pagina dentro de uma paste templates 

app.run()

#400 a 404 - pagina nao encontrada nos rastros 
#200 a 209 - retorno encontrado 