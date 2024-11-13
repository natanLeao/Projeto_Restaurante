from comanda import ComandaBebida
from comanda import ComandaComida
from cliente import Cliente

class Mesa:
    def __init__(self):
        self.vazia = True
        self.clientes = [Cliente() for _ in range(5)]  # Cria uma lista de 5 clientes
        self.bebidas = ComandaBebida()
        self.comidas = ComandaComida()
        self.total_clientes = 0

    def add_clientes(self):
        self.vazia = False

        nome = input("\tNome do cliente: ")
        self.clientes[self.total_clientes].nome = nome

        email = input("\tEmail do cliente: ")
        self.clientes[self.total_clientes].email = email

        self.total_clientes += 1

    def add_consumo(self, tipo):
        while True:
            try:
                opcao = int(input("\n1 - Comidas  \n2 - Bebidas\nO que deseja adicionar?: "))
                if opcao == 1:
                    self.comidas.escolher_produto(tipo)
                elif opcao == 2:
                    self.bebidas.escolher_produto(tipo)
                else:
                    print("\tOpção inválida. Tente novamente.")
                    continue
                break
            except ValueError:
                print("\tPor favor, insira um número válido.")

    def listar_consumo(self):
        self.comidas.listar_consumo()
        self.bebidas.listar_consumo()

    def divide_conta(self):
        if self.total_clientes > 0:
            return (self.bebidas.get_total() + self.comidas.get_total()) / self.total_clientes
        return 0.0

    def get_total(self):
        return self.bebidas.get_total() + self.comidas.get_total()

    def gorjeta(self):
        self.bebidas.aplicar_gorjeta()
        self.comidas.aplicar_gorjeta()

    def get_clientes(self):
        return self.clientes

    def get_num_clientes(self):
        return self.total_clientes

    def get_vazia(self):
        return self.vazia

