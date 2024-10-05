from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa a extensão CORS
from models.pipeline_pnl import pipeline_pln
import json

app = Flask(__name__)

# Habilita CORS para todas as rotas
CORS(app)

@app.route('/process', methods=['POST'])
async def process_data():
    content = request.json
    if 'route' not in content:
        return jsonify({'error': 'Missing "route" field in the request'}), 400
    
    route = content.get('route')
    
    # print("Received route:", route)
    
    data = await pipeline_pln(route)
    
    return data

if __name__ == '__main__':
    app.run(debug=True)
