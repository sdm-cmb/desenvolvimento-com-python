
from flask import Flask, render_template
#flask com f minusculo é a biblioteca, Flask com F maiusculo é a classe 


class Produto:
    def __init__(self, nome_prod, marca_prod, preco_prod ):
        self.nome =  nome_prod
        self.marca = marca_prod
        self.preco = preco_prod

# a variavel abaixo é a variavel que roda a aplicação (todos os objetos de prjeto dependelm dela)
app = Flask(__name__)
#Varialvel da aplicação sempre pede __name__

# @ signfica criar uma rota
@app.route('/inicio')
def ola():
    return '<h1>Inciando Flask</h1>'

@app.route('/lista')
def lista():

# a linha abaixo instancia um novo produto
    prod01 = Produto("Camisa", "Nike", "R$300,00")
    prod02 = Produto("Blusa", "Lacoste", "R$255,00")
    prod03 = Produto("Calça", "Oakley", "R$200,00")
    
    produtos_cadastrados = [prod01, prod02, prod03]

    return render_template('lista.html',
                           descricao ="Aqui estão seus produtos cadastrados", 
                           lista_prod = produtos_cadastrados)
#render template busca a pagina dentro de uma paste templates 

app.run()

#400 a 404 - pagina nao encontrada nos rastros 
#200 a 209 - retorno encontrado 