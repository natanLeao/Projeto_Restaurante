from dados_comanda import BancoDados

class Comanda:
    def __init__(self):
        self.pedidos = []
        self.valor_total = 0.0
        self.total_pedidos = 0
        self.banco = BancoDados()
        self.banco.criar_tabelas()  # Cria tabelas se não existirem
        self.banco.inserir_comidas_iniciais()  # Insere comidas iniciais
        self.banco.inserir_bebidas_iniciais()  # Insere bebidas iniciais
        self.menu_comidas = self.banco.carregar_menu('comidas')
        self.menu_bebidas = self.banco.carregar_menu('bebidas')

    def mostrar_menu(self, tipo):
        if tipo == 'comidas':
            print("\tMenu de Comidas:")
            menu = self.menu_comidas
        else:
            print("\tMenu de Bebidas:")
            menu = self.menu_bebidas

        for index, produto in enumerate(menu):
            print(f"\t{index + 1}. {produto.get_nome()} - R${produto.get_preco():.2f}")

    def escolher_produto(self, tipo):
        self.mostrar_menu(tipo)
        while True:
            try:
                escolha = int(input("\nEscolha o número do produto: ")) - 1
                if 0 <= escolha < len(self.menu_comidas if tipo == 'comidas' else self.menu_bebidas):
                    produto_escolhido = self.menu_comidas[escolha] if tipo == 'comidas' else self.menu_bebidas[escolha]
                    self.pedidos.append(produto_escolhido)
                    self.valor_total += produto_escolhido.get_preco()
                    self.total_pedidos += 1
                    print(f"\tVocê escolheu: {produto_escolhido.get_nome()} - R${produto_escolhido.get_preco():.2f}")
                    break
                else:
                    print("\tEscolha inválida. Tente novamente.")
            except ValueError:
                print("\tPor favor, insira um número válido.")

    def listar_consumo(self):
        if self.total_pedidos != 0:
            print("\n\tPedidos na comanda:")
            for pedido in self.pedidos:
                print(f"\t{pedido.get_nome()} - R${pedido.get_preco():.2f}")

    def aplicar_gorjeta(self):
        self.valor_total *= 1.1

    def get_total(self):
        return self.valor_total


class ComandaBebida(Comanda):
    def listar_consumo(self):
        if self.total_pedidos != 0:
            print("\n\tConsumo de Bebidas:")
            for pedido in self.pedidos:
                print(f"\t\t{pedido.get_nome()} - R${pedido.get_preco():.2f}")


class ComandaComida(Comanda):
    def listar_consumo(self):
        if self.total_pedidos != 0:
            print("\n\tConsumo de Comidas:")
            for pedido in self.pedidos:
                print(f"\t\t{pedido.get_nome()} - R${pedido.get_preco():.2f}")

