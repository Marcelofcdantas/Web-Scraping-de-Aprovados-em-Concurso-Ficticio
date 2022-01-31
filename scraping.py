import requests
from time import sleep
from parsel import Selector


class Scraping:

    def fetch(delay = 1, timeout = 3):
        url = 'https://sample-university-site.herokuapp.com'
        try:
            sleep(delay)
            response = requests.get(url, timeout=timeout)
        except (requests.ReadTimeout, requests.HTTPError):
            return 'Erro na resposta ou no endereço'
        else:
            if response.status_code == 200:
                # Transformar texto abaixo em nova função
                aproved_data = Selector(text=response.text)
                print(aproved_data)
                data = aproved_data.css("body > li > a ::text").getall()
                id = 0
                for cpfs in aproved_data.css('li'):
                    page = cpfs.css("a::attr(href)").get()
                    individual_response = requests.get(url + page)
                    result = Selector(individual_response.text)
                    cpf = data[id]
                    name = result.css("body > div:nth-child(2)::text").get()
                    score = result.css("body > div:nth-child(3)::text").get()
                    # print(cpf)
                    # print(name)
                    # print(score)
                    id += 1
                next_page = aproved_data.css('body > div > a::attr(href)').get()
                result = requests.get(url + next_page)
                aproved_data = Selector(text=result.text)
                print(aproved_data)


print(Scraping.fetch())