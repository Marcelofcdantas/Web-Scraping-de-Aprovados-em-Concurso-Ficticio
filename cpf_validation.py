class Cpf_validation:
    
    def validation(cpf):
        while True:
            new_cpf = cpf[:-2]
            reverse = 10
            total = 0

            for index in range(19):
                if index > 8:
                    index -= 9
                total += int(new_cpf[index]) * reverse
                reverse -= 1
                if reverse < 2:
                    reverse = 11
                    digit = 11 - (total % 11)
                    if digit > 9:
                        digit = 0
                    total = 0
                    new_cpf += str(digit)

            sequence = new_cpf == str(new_cpf[0]) * len(cpf)

            if cpf == new_cpf and not sequence:
                return 'Válido'
            else:
                return 'Inválido'