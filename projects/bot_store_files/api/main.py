from flask import Flask, make_response, jsonify, request
from repository import product

app_api = Flask('bot_store_files')
app_api.config['JSON_SORT_KEYS'] = False

# Rota pra inicio da API #
@app_api.route('/', methods=['GET'])
def hello_world():
    return "Hello, Fantastic World"

# -- Inicio: Serviços da api "Produto"

@app_api.route('/product', methods=['POST'])
def create_product():
    product_json = request.json
    id_product=0

    try:
        id_product = product.create_product(product_json)
        success = True
        _message = 'product insert successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            message = _message,
            id = id_product
        )
    )

@app_api.route('/products', methods=['GET'])
def list_products():
    list_products = list()
    list_products = product.list_products()

    if len(list_products) == 0:
        success = False
        _message = 'List Empty'
    else:
        success = True
        _message = 'List product OK'

    return make_response(
        jsonify(
            status = success, 
            message = _message,
            data = list_products
        )
    )

@app_api.route('/product/<int:id>', methods=['GET'])
def get_product_id(id):
    product_id = list()
    product_id = product.get_product_id(id)

    if len(product_id) == 0:
        success = False
        _message = 'product not found'
    else:
        success = True
        _message = 'product founded'

    return make_response(
        jsonify(
            status = success, 
            _message = _message,
            data = product_id
        )
    )

@app_api.route('/product', methods=['PUT'])
def update_product():
    product_json = request.json

    try:
        product.update_product(product_json)
        success = True
        _message = 'product updated successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            message = _message
        )
    )

@app_api.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product.delete_product(id)
        success = True
        _message = 'product deleted successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            mensagem = _message
        )
    ) 

# -- Inicio : Serviços da api "Produto" ---------------------

app_api.run()