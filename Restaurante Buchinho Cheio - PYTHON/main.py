from restaurante import Restaurante

class Main:
    @staticmethod
    def run():
        restaurante = Restaurante("Buchinho Cheio")
        opcao = -1

        print(f"\nBem-vindo ao restaurante {restaurante.get_nome()}")

        while opcao != 0:
            print("-----------------------------------------")
            print("1 - Add Cliente")
            print("2 - Add Pedido")
            print("3 - Listar Consumo")
            print("4 - Fechar Comanda")
            print("0 - Sair")
            opcao = input("Digite a operação desejada [0:4]: ")

            try:
                opcao = int(opcao)
            except ValueError:
                print("\nDigite uma opção válida.")
                continue

            if opcao == 0:
                break
            
            elif opcao == 1:
                restaurante.add_clientes()
                
            elif opcao == 2:
                restaurante.add_consumo()
                
            elif opcao == 3:
                restaurante.listar_consumo()
                
            elif opcao == 4:
                restaurante.fecha_comanda()
                
            else:
                print("\nDigite uma opção válida")

        print("\nVolte Sempre!")


# Executa o programa
if __name__ == "__main__":
    Main.run()

