import requests
from . import database

def insert_product_db(product):
    url = "http://127.0.0.1:5500/projects/bot_store_files/web/index.html"
    headers = {"Content-Type": "application/json"}
    data = {
        "name": product["Name"],
        "price": product["Price"],
        "category": product["Category"],
    }

    print(data)

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    
    except Exception as ex:
        print(f"Error Exception: {ex}")

def insert_product_forms(bot):
    products = database.fetch_products() 
    # bot.browse("url_do_formulario")
    
    for product in products: 
        name, price, category = product
        bot.kb_type("input[name='name']", name) 
        bot.kb_type("input[name='price']", price) 
        bot.kb_type("input[name='category']", category)

        bot.click("button#addProduct") # Botão para adicionar cada produto
        bot.click("button#showOrder") # Botão para mostrar o pedido
