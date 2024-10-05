from flask import Flask, jsonify, request
from models.pipeline_pnl import pipeline_pln

app = Flask(__name__)

@app.route('/process', methods=['POST'])
async def process_data():

    content = request.json
    route = content.get('route')  
    print(route)
    print("oii")
    data = await pipeline_pln(route)
    return jsonify(data) 

if __name__ == '__main__':
    app.run(debug=True)
