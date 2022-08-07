from bs4 import BeautifulSoup
import requests
from tabla_tkinter import hacer_app


# def arhivo_txt(name,c,v,website,more_info,fecha):
#     with open(f'posts/{name}.txt', 'w') as f:
#             f.write(f'Tipo de dolar: {name}\n')
#             f.write(f'{c}\n')
#             f.write(f'{v}\n')
#             f.write(f'Mas Info: {website+more_info}\n\n')
#             f.write(fecha)
#     print(f'Archivo guardado: {name}')


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
        # arhivo_txt(dolar_name,compra,venta,website,more_info,fecha)
        
        lista_datos = []
        lista_datos.append(dolar_name)
        lista_datos.append(compra)
        lista_datos.append(venta)
        lista_datos.append(more_info)
        lista_general.append(lista_datos)
        
        # modifico la base de datos, segun los nuevos valores que voy obteniendo
        # guardar_db(dolar_name,compra,venta,fecha)

    
    hacer_app(lista_general, fecha)    
      
valor_dolar()
# if __name__ == '__main__':
#   while True:
    # valor_dolar()
    # time_wait = 6
    # print(f'Esperando {time_wait} minutos...')
    # time.sleep(time_wait * 60)
    