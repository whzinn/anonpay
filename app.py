# servidor central
from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def barra():
    return render_template("inicio.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")
    
@app.route('/enviar')
def enviar():
    return render_template("enviar.html")
    
@app.route('/gerar')
def gerar():
    return render_template("gerar.html")
    
@app.route('/forma')
def forma():
    return render_template("forma.html")
    
    
@app.route('/pagar')
def pagar():
    return render_template("pagar2.html")
    
    
@app.route('/aqui', methods=['POST'])
def aqui():
    if request.method == 'POST':
        campo = request.form['campo-texto']
        email = request.form['campo-email']
        #pix = mp.pix(email, campo)
        #pix = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/043fb990-1619-4c98-9c47-9d9609ff5959/payment-option-form/?preference-id=422523501-2a076704-eab2-4679-8ac8-797650077d75&router-request-id=f4563d60-f88f-40cd-8a74-730b5e41a969&webview=true&source=link&p=47edabca0cceb46bc47aa8decfeeaf16#/"
        # fazer algo com os dados recebidos
        return render_template('pagar.html',campo=campo, email=email)
@app.route('/', methods=['GET', 'POST'])
def form():
    ip_address = request.remote_addr
    print(f"O Ip {ip_address} acessou nosso site")
    return render_template('busca.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
