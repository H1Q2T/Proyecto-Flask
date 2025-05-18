from flask import Flask, render_template, request, jsonify
import io
import contextlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/condicionales')
def condicionales():
    return render_template('condicionales.html')

@app.route('/bucles')
def bucles():
    return render_template('bucles.html')

@app.route('/estructuras')
def estructuras():
    return render_template('estructuras.html')

@app.route('/comprensiones')
def comprensiones():
    return render_template('comprensiones.html')

@app.route('/poo_animales')
def poo_animales():
    return render_template('poo_animales.html')

@app.route('/poo_vehiculos')
def poo_vehiculos():
    return render_template('poo_vehiculos.html')

@app.route('/flask')
def flask_info():
    return render_template('flask.html')

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    data = request.get_json()
    codigo = data.get("codigo", "")
    salida = io.StringIO()
    try:
        with contextlib.redirect_stdout(salida):
            exec(codigo, {})
        resultado = salida.getvalue()
    except Exception as e:
        resultado = f"Error: {str(e)}"
    return jsonify({"resultado": resultado})

@app.errorhandler(404)
def pagina_no_trobada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
