# Python web-scraping

Projeto desenvolvido no qual faz-se web scraping de dados que são tratados e validados para serem salvos em um banco de dados MySQL.

_Project developed to web scrape data which will be treated and validated to be saved on a MySQL database._

## Clonagem do projeto / _Project cloning_

- A clonagem é feita através do comando:
- _To clone the project use the following command:_

```git clone https://github.com/Marcelofcdantas/web-scraping.git```

- Após a clonagem, deve-se ativar o ambiente virtual e instalar as dependências do projeto:
- _After cloning, the virtual environment should be activated and install project's dependencies:_

```
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

- Por fim, ao dar o comando abaixo será realizada a raspagem de dados e salva no banco de dados MySQL:]
- _Finally, use the following command to start scraping and saving on MySQL database:]_

``` python3 scraping.py```

## Projeto realizado em Python 
## _Project done in Python_

- Projeto realizado para capturar os dados dos aprovados em um fictício concurso cuja listagem encontra-se disponível em https://sample-university-site.herokuapp.com/
- _Project created to capture the data of the approved candidates in a fictional exam, the list of which is available at https://sample-university-site.herokuapp.com/_

- Após pegar os CPFs, nomes e notas, o sistema valida o CPF e informa se é válido ou não, salvando esta informação no banco de dados.
- _After retrieving the CPFs (a kind of Sin Number), names, and scores, the system validates the CPF and indicates whether it is valid or not, saving this information in the database._

- Anteriormente ao salvamento dos dados, ocorre a higienização dos dados, retirando acentos e letras maiúsculas visando a uniformização dos dados.
- _Prior to saving the data, data cleansing occurs, removing accents and uppercase letters to standardize the data._
