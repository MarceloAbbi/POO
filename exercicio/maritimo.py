from veiculos import Veiculo

class Aereo(Veiculo):

    def __init__(self, categoria, placa, cor, chassi, marca) -> None:
        super().__init__(categoria, placa, cor, chassi, marca)