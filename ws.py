import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

print("  ========================================")
print(" | - BIENVENIDOS AL BUSCADOR DE PRECIOS - |")
print("  ========================================\n") 

#--| Setup
options = Options()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ['enable-automation'] )
options.add_experimental_option("excludeSwitches", ["enable-logging"] )   
options.add_argument("--window-size=1920,1080")
options.add_argument("--allow-insecure-localhost")   
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
s = Service('C:/Users/the_b/Downloads/chromedriver') 
browser = webdriver.Chrome(service= s, options= options)

#--| Ruta donde se guarda el archivo Excel que genera el programa
cwd = os.path.expanduser('~\Desktop\Precios.xlsx')
    
#--| Funcion que hace scraping en la pagina de Jumbo
def scrap_products_jumbo(opcion=""):   
    productos = []
    browser.delete_all_cookies()
    browser.get('https://www.jumbo.com.ar/') 
    time.sleep(5)
    buscador = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[4]/div[1]/div/div/div[2]/section/div/div[2]/div/div/div[1]/div/label/div/input')
    buscador.send_keys(opcion)
    time.sleep(1)
    buscador.send_keys(Keys.ENTER)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'lxml') 
       
    items = soup.find_all('article', class_= 'vtex-product-summary-2-x-element pointer pt3 pb4 flex flex-column h-100')      
    for item in items:
        producto = {} 
        producto['Productos de Jumbo'] = item.find('span' , class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body').text
        producto['Precio'] = item.find('div', class_='vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--shelf-main-price-box pb0').text 
        productos.append(producto)

        # Se crea el Dataframe y se guarda en un archivo excel
        df = pd.DataFrame.from_dict(productos) 
        with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'Precios.xlsx'), 'wb') as fh:
            df.to_excel (fh, sheet_name = 'Comparacion', index = False)                 
    return productos  

def scrap_products_dia(opcion=""):   
    productos = []
    browser.delete_all_cookies()
    browser.get('https://diaonline.supermercadosdia.com.ar/') 
    time.sleep(5)
    buscador = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[4]/div/div/div/div/div[1]/div/label/div/input')
    buscador.send_keys(opcion)
    time.sleep(1)
    buscador.send_keys(Keys.ENTER)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'lxml') 
       
    items = soup.find_all('div', class_= 'vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--default pa4')      
    for item in items:
        producto = {} 
        producto['Productos de Dia'] = item.find('span' , class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body').text
        producto['Precio'] = item.find('span', class_='vtex-product-price-1-x-currencyContainer').text  
        productos.append(producto)

        # Se crea el Dataframe y se añade al archivo excel previamente creado
        df = pd.DataFrame.from_dict(productos) 
        with pd.ExcelWriter(cwd, engine="openpyxl",if_sheet_exists='overlay', mode='a') as writer:  
                df.to_excel(writer, sheet_name='Comparacion', startcol = 6,  index = False)                  
    return productos  

#--| Funcion que hace scraping de la pagina de Changomas
def scrap_products_chango(opcion=""): 
    productos = []
    browser.get('https://www.masonline.com.ar/')
    time.sleep(5)
    buscador = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div/section/div/div[3]/div/div[1]/div/label/div/input')
    buscador.send_keys(opcion)
    time.sleep(1)
    buscador.send_keys(Keys.ENTER)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    items = soup.find_all('section', class_= 'vtex-product-summary-2-x-container')           
    for item in items:
        producto = {}
        producto['Productos de Changomas'] = item.find('span' , class_='vtex-product-summary-2-x-productBrand').getText()
        producto['Precio'] = item.find('div', class_= 'lyracons-dynamic-product-0-x-dynamicProductPrice').getText()        
        productos.append(producto)        
           
        # Se crea el Dataframe y se añade al archivo excel previamente creado
        df = pd.DataFrame.from_dict(productos) 
        with pd.ExcelWriter(cwd, engine="openpyxl",if_sheet_exists='overlay', mode='a') as writer:  
                df.to_excel(writer, sheet_name='Comparacion', startcol = 2,  index = False)                            
    return productos
  
#--| Funcion que hace scraping de la pagina de Coto   
def scrap_products_coto(opcion= ""):    
    productos = []
    browser.get('https://www.cotodigital3.com.ar/sitios/cdigi/')
    time.sleep(7) 
    buscador = browser.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/form/div[4]/input')
    buscador.send_keys(opcion)
    time.sleep(2)
    buscador.send_keys(Keys.ENTER)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    items = soup.find_all('li', class_= 'clearfix')       
    for item in items:
        producto = {}
        producto['Productos de Coto'] = item.find('div' , class_='descrip_full').text
        producto['Precio'] = item.find('span', class_= 'atg_store_newPrice').getText().strip()        
        productos.append(producto)

        # Se crea el Dataframe y se añade al archivo excel previamente creado
        df = pd.DataFrame.from_dict(productos)        
        with pd.ExcelWriter(cwd, engine="openpyxl", mode='a',if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='Comparacion', startcol = 4,  index = False)                                                                        
    return productos

    
#--| Funcion principal que ejecuta el programa
def main():
    opcion = input("Introduce el producto que quieres buscar >> ")
    print("")

    print("************************************************************")    
    print(f"      >>>>>>  Buscando {opcion.upper()} en Jumbo  <<<<<<<<<")
    print("************************************************************\n") 
    productos_jumbo = scrap_products_jumbo(opcion) 
    print("------------------------------------------------------------")    
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en Jumbo  <<<<<<<<<")
    print("------------------------------------------------------------\n")    
    for producto in productos_jumbo:
        print(f'{producto["Productos de Jumbo"]} = {producto["Precio"]}')
        print("\n") 

    print("************************************************************")    
    print(f"      >>>>>>  Buscando {opcion.upper()} en ChangoMas  <<<<<<<<<")
    print("************************************************************\n")      
    productos_chango = scrap_products_chango(opcion) 
    print("------------------------------------------------------------------")
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en ChangoMas  <<<<<<<<<")
    print("------------------------------------------------------------------\n")
    for producto in productos_chango:
        print(f'{producto["Productos de Changomas"]} = {producto["Precio"]}')
        print("\n")

    print("************************************************************")    
    print(f"    >>>>>>  Buscando {opcion.upper()} en Coto  <<<<<<<<<")
    print("************************************************************\n")     
    productos_coto = scrap_products_coto(opcion) 
    print("--------------------------------------------------------------")    
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en Coto  <<<<<<<<<")
    print("--------------------------------------------------------------\n")
    for producto in productos_coto:
        print(f'{producto["Productos de Coto"]} = {producto["Precio"]}')
        print("\n") 

    print("************************************************************")    
    print(f"      >>>>>>  Buscando {opcion.upper()} en DIA  <<<<<<<<<")
    print("************************************************************\n")      
    productos_dia = scrap_products_dia(opcion) 
    print("------------------------------------------------------------------")
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en DIA  <<<<<<<<<")
    print("------------------------------------------------------------------\n")
    for producto in productos_dia:
        print(f'{producto["Productos de Dia"]} = {producto["Precio"]}')
        print("\n")
        

    print(" ---------------------------------------------------------")
    print("| - SE GUARDO LA INFORMACION EN EL ARCHIVO Precios.xlsx - |")
    print(" ---------------------------------------------------------\n")

    # Se pregunta al usuario si quiere visualizar el archivo generado
    respuesta = input("¿Queres abrir el archivo Excel? (S/N) : ").upper()
    print("")
    if respuesta == "S" :
        os.startfile(cwd)
    else:
        print("El archivo se guardo en el Escritorio\n")    
 
main()

#--| Bucle para seguir buscando productos
while True:  
     nuevo = input("¿Buscar otro Producto? (S/N) : ").upper()
     print("")
     if nuevo == "S":
            main()
     else:
        print("Cerrando el programa...")
        browser.quit()
        break

        
     
       
    




    



