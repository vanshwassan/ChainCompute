from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

## Sending in the graphql query and making it a Rest API
@app.route('/graph', methods=['GET'])
def theGraph():
    query = request.args.get('query')
    api_key = request.args.get('api_key')
    subgraph = request.args.get('subgraph')
    url = 'https://gateway.thegraph.com/api/%s/subgraphs/id/%s'%(api_key, subgraph)
    r = requests.post(url, json={"query": query})
    return r.json()

if __name__ == '__main__':
    app.run(debug=True)