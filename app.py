from flask import request, jsonify
from flasgger import swag_from, Swagger
from init import app, HTTP_METHODS, objbank
from business import set_contaBN, get_contaBN, transacaoBN
import os


"""
    Endpoints da API
"""

@app.route('/transacao', methods=['POST'])
def transacao():
    return transacaoBN(request.get_json())

@app.route('/conta', methods=['POST'])
def set_conta():
    return set_contaBN(request.get_json())

@app.route('/conta', methods=['GET'])
def get_conta():
    return get_contaBN(request.args.get('id', None))

@app.route('/extrato', methods=['GET'])
def extrato():
    return 1 #extratoBN(request.args.get('id', None))  ... implementação futura


"""
    Endpoints de tratamento
"""

@app.route('/', methods=HTTP_METHODS)
def index():
    return "Resource not found", 400

@app.errorhandler(500)
def internal_error(error):
    return "500 error", 500

@app.errorhandler(404)
def not_found(error):
    return "404 error", 404

@app.route('/ping', methods=['GET'])
def ping():
    return {"ping": "pong!"}


"""
    Start App
"""

app.register_blueprint(objbank)
swagger = Swagger(app)
app.run(host=os.environ.get("APP_HOST"), port=5000, debug=True)