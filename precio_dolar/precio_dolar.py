from bs4 import BeautifulSoup
import requests
from tabla_tkinter import hacer_app
#defino e inicializo las tablas que me serviran mas adelante, aunque creo que pueden ir adentro de la funcion valor_dolar
lista_datos=[]
lista_general=[]

def valor_dolar():
    website = 'https://dolarhoy.com' #pagina de donde saco la info
    res = requests.get(website)
    content = res.text 

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    box = soup.find('div', class_= 'tile is-parent is-9 cotizacion is-vertical') #aislo la info que me sirve

    fecha = box.find('div', class_= 'tile update').text.strip('Actualizdo el') #busco la fecha de actualización 
    
    dolares = box.find_all('div', class_= 'tile is-child') #busco los contenedores que quiero utilizar

    for dolar in dolares:
        dolar_name = dolar.find('a', class_='title').text.replace(' ','_') #obtengo el nombre de cada dolar
        #Nota: hacer 'dolar.find('a', class_='title').text' es igual a 'dolar.a.text' en este caso.
        compra = dolar.find('div', class_ = 'compra').text.strip('Compra')  #obtengo el valor de compra de cada dolar
        venta = dolar.find('div', class_ = 'venta').text.strip('Venta') #obtengo el valor de venta de cada dolar
        more_info = dolar.a['href'] #obtengo el link de cada titulo.
          
        lista_datos = [] #inicializo la tabla por cada bucle
        lista_datos.append(dolar_name)#Por cada tipo de dolar obtenido, armo una lista y voy agregando el tipo de dolar; el preio de compra y el precio de venta
        lista_datos.append(compra)
        lista_datos.append(venta)
        lista_general.append(lista_datos) #A cada tabla creada recien la guardo en esta tabla asi tengo una tabla de tablas donde en la funcion hacer_app me es mas facil recorrer los datos de esta manera

    
    hacer_app(lista_general, fecha) #le paso los argumentos que requiere mi funcion para armar la pestaña emergente
      
valor_dolar()

#si quiero que mi programa se ejecute cada cierto tiempo utilizo el codigo de debajo, en este caso es cada 6 horas.
# if __name__ == '__main__':
#   while True:
    # valor_dolar()
    # time_wait = 6
    # print(f'Esperando {time_wait} minutos...')
    # time.sleep(time_wait * 60)
    
