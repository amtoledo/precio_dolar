from bs4 import BeautifulSoup
import requests
import dollar_table

class DollarScraper:
    def __init__(self):
        self.dollars_list = []
        self.url = 'https://dolarhoy.com/'

    def scrape_dollar(self):
        
        res = requests.get(self.url)
        content = res.text

        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('div', class_='tile is-parent is-9 cotizacion is-vertical')
        dolares = box.find_all('div', class_='tile is-child')
        
        for dollar in dolares:
            dollar_type = dollar.find('a', class_='titleText').text
            
            try: 
                buy = dollar.find('div', class_='compra').find('div', class_='val').text
            except:
                buy = ''

            try: 
                sell_div = dollar.find('div', class_='venta')
                sell = sell_div.find('div', class_='val').text
                sell_variance_percentage = sell_div.find('div', class_='var-porcentaje').text                
                sell = sell + ' (' + sell_variance_percentage + ')'
            except:
                sell = ''
            
            
            self.dollars_list.append([dollar_type, buy, sell])

        self.date = box.find('div', class_='tile update').text.strip('Actualizdo el')

    
    def run_app(self):
        date = 'Actualizado ' + self.date
        dollar_table.Dollar_table(self.dollars_list)

if __name__ == '__main__':
    dolar_scraper = DollarScraper()
    dolar_scraper.scrape_dollar()
    dolar_scraper.run_app()