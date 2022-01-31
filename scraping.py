import requests
from time import sleep
from parsel import Selector
from controller.controller import Controller


class Scraping:

    def getting_data(url, response):
        aproved_data = Selector(text=response.text)
        cpfs_numbers = aproved_data.css("body > li > a ::text").getall()
        id = 0
        for cpfs in aproved_data.css('li'):
            page = cpfs.css("a::attr(href)").get()
            individual_response = requests.get(url + page)
            result = Selector(individual_response.text)
            cpf = cpfs_numbers[id]
            name = result.css("body > div:nth-child(2)::text").get()
            score = result.css("body > div:nth-child(3)::text").get()
            print(cpf)
            print(name)
            print(score)
            Controller(name, cpf, score)
            id += 1
        next_page = aproved_data.css('body > div > a::attr(href)').get()
        response = requests.get(url + next_page)
        if response.status_code == 200:
            Scraping.getting_data(url, response)


    def fetch(delay = 1, timeout = 3):
        url = 'https://sample-university-site.herokuapp.com'
        try:
            sleep(delay)
            response = requests.get(url, timeout=timeout)
        except (requests.ReadTimeout, requests.HTTPError):
            return 'Erro na resposta ou no endereço'
        else:
            if response.status_code == 200:
                Scraping.getting_data(url, response)


print(Scraping.fetch())