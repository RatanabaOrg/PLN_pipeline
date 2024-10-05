from flask import Flask, jsonify, request
from models.pipeline_pnl import pipeline_pln
import pandas as pd
import numpy as np

app = Flask(__name__)

def convert_to_serializable(data):
    if isinstance(data, np.ndarray):
        return data.tolist()
    # Adicione mais condições se necessário para outros tipos
    return data

@app.route('/process', methods=['POST'])
async def process_data():
    content = request.json
    route = content.get('route')
    
    print("Received route:", route)
    
    data = await pipeline_pln(route)
    
    print("Type of processed data:", type(data))
    print("Processed data:", data)
    print(data)

    return jsonify(convert_to_serializable(data))

if __name__ == '__main__':
    app.run(debug=True)
