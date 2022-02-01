from multiprocessing import connection
import pymysql.cursors
from contextlib import contextmanager

class Model:

    @contextmanager
    def connect():
        connection = pymysql.connect(
            host='localhost',
            database='db_aprovados',
            user='marcelofcd',
            password='nany2302',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            yield connection
        finally:
            connection.close()

    def model(name, score, cpf, valid_cpf):
        
        table = """CREATE TABLE IF NOT EXISTS aproved ( 
                             `id` int AUTO_INCREMENT NOT NULL,
                             `cpf` varchar(14) NOT NULL,
                             `name` varchar(100) NOT NULL,
                             `score` varchar(5) NOT NULL,
                             `valid_cpf` varchar(8) NOT NULL,
                             PRIMARY KEY (`id`)) """

        with Model.connect() as connect:
            print('Conectado ao servidor MySQL')
            with connect.cursor() as cursor:
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS `db_aprovados`')
                cursor.execute(table)
                SQL = 'INSERT INTO `aproved` (`name`, score, cpf, valid_cpf) VALUES ' \
                    '(%s, %s, %s, %s)'
                cursor.execute(SQL, (name, score, cpf, valid_cpf))
                connect.commit()
