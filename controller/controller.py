from cpf_validation import Cpf_validation
from model.model import Model


class Controller:

    def controller(name, cpf, score):
        valid_cpf = Cpf_validation.validation(cpf)
        Model.model(name, score, cpf, valid_cpf)