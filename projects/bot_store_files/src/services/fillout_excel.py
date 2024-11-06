import pandas as pd
from openpyxl import Workbook
from IPython.display import display

def fillout_excel(products, filename) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Products Order"
    
    # Adicionar cabeçalhos 
    ws.append(["Name", "Price", "Category"])
    
    # Adicionar os products
    for product in products:
        ws.append([product.name, product.price, product.category])

    wb.save(filename) # Salvar o arquivo
    print(f"File save as {filename}")

def read_excel(path_file, name_spreadsheet):
    df = pd.read_excel(path_file, sheet_name=name_spreadsheet)

    return df

def show_data_excel(df) -> None:
    display(df)
