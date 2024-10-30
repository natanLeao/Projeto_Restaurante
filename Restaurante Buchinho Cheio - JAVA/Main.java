import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Restaurante restaurante = new Restaurante("Buchinho Cheio", "Endereço do Restaurante");
        int opcao;

        System.out.println("\nBem vindo ao restaurante " + restaurante.getNome());

        do {
            System.out.print("-----------------------------------------\n" +
                             "1 - Add cliente               \n" +
                             "2 - Add pedido                \n" +
                             "3 - Listar consumo            \n" +
                             "4 - Fechar comanda            \n" +
                             "0 - Sair                      \n");
            System.err.print("Digite a operação desejada [0:4]: ");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao){
                case 0:
                    break;

                case 1:
                    restaurante.addClientes(scanner);
                    break;

                case 2:
                    restaurante.addConsumo(scanner);
                    break;

                case 3:
                    restaurante.listarConsumo(scanner);
                    break;

                case 4:
                    restaurante.fechaComanda(scanner);
                    break;

                default:
                    System.out.println("Digite uma opção válida");
                    break;
            }
        } while (opcao != 0);

        System.out.print("\nVolte Sempre!\n");

        scanner.close();
    }
}
