# Python web-scraping

Projeto desenvolvido no qual faz-se web scraping de dados que são tratados e validados para serem salvos em um banco de dados MySQL.


# Clonagem do projeto

- A clonagem é feita através do comando:

```git clone https://github.com/Marcelofcdantas/web-scraping.git```

- Após a clonagem, deve-se ativar o ambiente virtual e instalar as dependências do projeto:

```
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

- Por fim, ao dar o comando abaixo será realizada a raspagem de dados e salva no banco de dados MySQL:]

``` python3 scraping.py```

## Projeto realizado em Python 

- Projeto realizado para capturar os dados dos aprovados em um fictício concurso cuja listagem encontra-se disponível em https://sample-university-site.herokuapp.com/

- Após pegar os CPFs, nomes e notas, o sistema valida o CPF e informa se é válido ou não, salvando esta informação no banco de dados.

- Anteriormente ao salvamento dos dados, ocorre a higienização dos dados, retirando acentos e letras maiúsculas visando a uniformização dos dados.
