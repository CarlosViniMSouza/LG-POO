# from .database import create_db
import database

# Verificar se Pedido existe
def check_order_exists(id):
    exists: False

    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM order WHERE id = '{id}'"
        
        cursor.execute()
        list_orders = cursor.fetchall()
        
        if len(list_orders) == 0:
            exists = False
        else:
            exists = True

    except Exception as ex:
        print(f'Erro: {ex}')

    return exists

# Add Pedido com as devidas informações
def create_order(order):
    try:
        conect = database.create_db()
        cursor = conect.cursor()

        sql = f"INSERT INTO order(products, quantity, client, status) VALUES('{order['products']}', '{order['quantity']}', '{order['client']}', '{order['status']}')"

        print(sql)

        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return last_id

# Fornecer lista de Pedidos
def list_orders():
    orders = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM order ORDER BY status' # see it

        cursor.execute(sql)
        list_orders = cursor.fetchall()

        for order in list_orders:
            orders.append({
                'id': order[0],
                'products': order[1],
                'quantity': order[2],
                'client': order[3],
                'status': order[4]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return orders

# Buscar Pedido pelo ID
def get_order_id(id):
    orders = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM order WHERE id = '{id}'"

        cursor.execute(sql)
        list_orders = cursor.fetchall()

        for order in list_orders:
            orders.append({
                'id': order[0],
                'products': order[1],
                'quantity': order[2],
                'client': order[3],
                'status': order[4]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return orders

# Atualizar infos cadastradas
def update_order(order):
    try:
        conect = database.create_db()
        cursor = conect.cursor()

        sql = f"UPDATE order SET products = '{order['products']}', quantity = '{order['quantity']}', client = '{order['client']}', status = '{order['status']}' WHERE id = '{order['id']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

# Remover Pedido
def delete_order(id):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM order WHERE id = {id}'

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()
    