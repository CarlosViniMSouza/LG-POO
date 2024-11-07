import database

# Verificar se Usuario existe
def check_product_exists(id):
    exists: False

    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM product WHERE id = '{id}'"
        
        cursor.execute()
        list_products = cursor.fetchall()
        
        if len(list_products) == 0:
            exists = False
        else:
            exists = True

    except Exception as ex:
        print(f'Erro: {ex}')

    return exists

# Add Usuario com as devidas informações
def create_product(product):
    try:
        conect = database.create_db()
        print(conect)
        cursor = conect.cursor()
        sql = f"INSERT INTO product(name, price, category) VALUES('{product['name']}', '{product['price']}', '{product['category']}')"

        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return last_id

# Fornecer lista de Usuarios
def list_products():
    products = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM product ORDER BY name'

        cursor.execute(sql)
        list_products = cursor.fetchall()

        for product in list_products:
            products.append({
                'id': product[0],
                'name': product[1],
                'price': product[2],
                'category': product[3],
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return products

# Buscar Usuario pelo ID
def get_product_id(id):
    products = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM product WHERE id = '{id}'"

        cursor.execute(sql)
        list_products = cursor.fetchall()

        for product in list_products:
            products.append({
                'id': product[0],
                'name': product[1],
                'price': product[2],
                'category': product[3]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return products

# Atualizar infos cadastradas
def update_product(product):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"UPDATE product SET name = '{product['name']}', price = '{product['price']}', category = '{product['category']}' WHERE id = '{product['id']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

# Remover Usuario
def delete_product(id):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM product WHERE id = {id}'

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()