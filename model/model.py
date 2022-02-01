from multiprocessing import connection
import pymysql.cursors
from contextlib import contextmanager

class Model:

    @contextmanager
    def connect():
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            yield connection
        finally:
            connection.close()

    def create(user_id, name, score, cpf, valid_cpf):

        table = """CREATE TABLE IF NOT EXISTS aproved ( 
                    id int(10) NOT NULL,
                    `name` varchar(100) NOT NULL,
                    `score` varchar(100) NOT NULL,
                    `cpf` varchar(14) NOT NULL,
                    `valid_cpf` varchar(8) NOT NULL,
                    PRIMARY KEY (id)) """

        with Model.connect() as connect:
            print(f'Cadastro realizado em nome de {name}')
            with connect.cursor() as cursor:
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS `db_aprovados`')
                cursor.execute(f'USE `db_aprovados`')
                cursor.execute(table)
                SQL = 'INSERT INTO `aproved` (`id`, `name`, `score`, `cpf`, `valid_cpf`) VALUES ' \
                    '(%s, %s, %s, %s, %s)'
                cursor.execute(SQL, (user_id, name, score, cpf, valid_cpf))
                connect.commit()


    def count_datas(user_id):

        with Model.connect() as connect:
            with connect.cursor() as cursor:
                try:
                    cursor.execute(f'USE `db_aprovados`')
                    cursor.execute(f'SELECT COUNT(`name`) FROM `aproved`')
                    result = cursor.fetchone()
                    user_id = int(*result.values()) + 1
                    return user_id
                except:
                    return user_id