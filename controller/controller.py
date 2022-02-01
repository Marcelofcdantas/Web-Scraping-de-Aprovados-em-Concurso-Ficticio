from cpf_validation import Cpf_validation
from model.model import Model
import unidecode


class Controller:

    def data_cleaning(name):
        name = unidecode.unidecode(name)
        return name.lower()


    def controller(name, cpf, score):
        valid_cpf = Cpf_validation.validation(cpf)
        name = Controller.data_cleaning(name)
        Model.model(name, score, cpf, valid_cpf)