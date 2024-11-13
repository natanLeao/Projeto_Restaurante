from mesa import Mesa

class Restaurante:
    def __init__(self, nome_restaurante):
        self.mesas = [Mesa() for _ in range(5)]
        self.nome_restaurante = nome_restaurante

    def mesas_status(self):
        print("\nMesas Vazias:")
        for i, mesa in enumerate(self.mesas):
            if mesa.get_vazia():
                print(f" Mesa {i + 1}")

        print("\nMesas com Clientes:")
        for i, mesa in enumerate(self.mesas):
            if mesa.get_num_clientes() > 0:
                print(f" Mesa {i + 1}:")
                for cliente in mesa.get_clientes():
                    if cliente.nome is not None:
                        print(f"  {cliente.nome}")

        print("\nMesas Cheias:")
        for i, mesa in enumerate(self.mesas):
            if mesa.get_num_clientes() == 5:
                print(f" Mesa {i + 1}:")
                for cliente in mesa.get_clientes():
                    print(f"  {cliente.nome}")

    def add_clientes(self):
        self.mesas_status()
        
        while True:
            try:
                indice = int(input("\nAdicionar cliente em qual mesa?: ")) - 1
                if indice < 0 or indice >= len(self.mesas):
                    print(f"Por favor, insira uma mesa entre 1 e {len(self.mesas)}.")
                else:
                    break  # Sai do loop se o índice for válido
            except ValueError:
                print("Por favor, insira uma mesa válida.")

        if self.mesas[indice].get_num_clientes() == 4:
            print("Mesa Cheia\n")
        else:
            while True:
                self.mesas[indice].add_clientes()
                continuar = input("\n1 - Sim  \n2 - Não\nDeseja adicionar mais um cliente nessa mesa?: ")
                if self.mesas[indice].get_num_clientes() == 4:
                    print("Mesa Cheia\n")
                    break
                elif continuar != "1":
                    break

    def add_consumo(self, tipo):
        self.mesas_status()
        
        while True:
            try:
                indice = int(input("\nAdicionar pedido em qual mesa?: ")) - 1
                if indice < 0 or indice >= len(self.mesas):
                    print(f"Por favor, insira uma mesa entre 1 e {len(self.mesas)}.")
                else:
                    break  # Sai do loop se o índice for válido
            except ValueError:
                print("Por favor, insira uma mesa válida.")

        if self.mesas[indice].get_vazia():
            print("\nNão possui clientes")
        else:
            while True:
                self.mesas[indice].add_consumo(tipo)
                continuar = input("\n1 - Sim  \n2 - Não\nDeseja adicionar mais um pedido nessa mesa?: ")
                if continuar != "1":
                    break

    def listar_consumo(self):
        self.mesas_status()
        
        while True:
            try:
                indice = int(input("\nQual mesa deseja ver a lista de consumo?: ")) - 1
                if indice < 0 or indice >= len(self.mesas):
                    print(f"Por favor, insira uma mesa entre 1 e {len(self.mesas)}.")
                else:
                    break  # Sai do loop se o índice for válido
            except ValueError:
                print("Por favor, insira uma mesa válida.")

        if self.mesas[indice].get_total() == 0:
            print("\nNão possui pedidos")
        else:
            self.mesas[indice].listar_consumo()

    def fecha_comanda(self):
        self.mesas_status()
        
        while True:
            try:
                indice = int(input("\nQual mesa deseja fechar a conta?: ")) - 1
                if indice < 0 or indice >= len(self.mesas):
                    print(f"Por favor, insira uma mesa entre 1 e {len(self.mesas)}.")
                else:
                    break  # Sai do loop se o índice for válido
            except ValueError:
                print("Por favor, insira uma mesa válida.")

        if self.mesas[indice].get_num_clientes() == 0:
            print("\nNão possui clientes")
        else:
            self.mesas[indice].gorjeta()
            print(f"\tValor da conta: R${self.mesas[indice].get_total():.2f}")
            print(f"\tValor para {self.mesas[indice].get_num_clientes()} pessoas: R${self.mesas[indice].divide_conta():.2f}")
            self.mesas[indice] = Mesa()  # Reinicia a mesa

    def get_nome(self):
        return self.nome_restaurante

    def get_endereco(self):
        return self.endereco

    def get_num_mesas(self):
        return len(self.mesas)

