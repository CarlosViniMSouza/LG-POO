import requests

def insert_product_db(product):
    url = "http://127.0.0.1:5000/product"
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