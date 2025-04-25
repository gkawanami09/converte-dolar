from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    try:
        moeda = float(request.form['moeda'])
        conversao = round(moeda/5.67, 2)

        return render_template('index.html', moeda=moeda, conversao=conversao)
    except ValueError as e:
        return render_template('erro.html', mensagem=f"Entrada inválida: {e}")
    finally:
        print("obrigado por usar o programa ")

if __name__ == '__main__':
    app.run(debug=True)
