from flask import Flask, jsonify
from models.pipeline_pnl import pipeline_pln

app = Flask(__name__)

@app.route('/route/<route>')
def usuario(route):
    pipeline_pln(route)
    return jsonify({'mensagem': f'Olá, {route}!'})

if __name__ == '__main__':
    app.run(debug=True)