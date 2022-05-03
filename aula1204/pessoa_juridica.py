from aula1204.pessoa import Pessoa

class PessoaFisica:

    def __init__(self, nome, endereco, telefone, cnpj, ie, nome_fantasia):
        super().__init__(nome, endereco, telefone)
        self._cnpj = cnpj
        self._ie = ie
        self._nome_fantasia = nome_fantasia

    def validar_cnpj (cnpj=None):
        if cnpj is not None:
            return True

        return False