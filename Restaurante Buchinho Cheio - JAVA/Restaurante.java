import java.util.Scanner;

class Restaurante{
    private Mesa[] mesas = new Mesa[10];
    private int numMesas;
    private String nomeRestaurante;
    private String endereco;
    private int indice;

    public Restaurante(String nomeRestaurante, String endereco){
        for (int i = 0; i < mesas.length; i++){
            mesas[i] = new Mesa();
        }

        this.nomeRestaurante = nomeRestaurante;
        this.endereco = endereco;
    }

    public void mesas(){
        System.out.println("\nVazias:");

        for (int i = 0; i < mesas.length; i++){
            if (mesas[i].getVazia()){
                System.out.println(" " + (i + 1));
            }
        }

        System.out.println("\nCom pessoas:");

        for (int i = 0; i < mesas.length; i++){
            if (mesas[i].getNumClientes() > 0 && mesas[i].getNumClientes() < 5){
                System.out.println(" " + (i + 1));

                for (Cliente cliente : mesas[i].getClientes()){
                    if (cliente.getNome() != null){
                        System.out.println("  " + cliente.getNome());
                    }
                }
            }
        }

        System.out.println("\nCheias:");

        for (int i = 0; i < mesas.length; i++){
            if (mesas[i].getNumClientes() == 5){
                System.out.println(" " + (i + 1));

                for (Cliente cliente : mesas[i].getClientes()){
                    System.out.println("  " + cliente.getNome());
                }
            }
        }

        System.out.println();
    }

    public void addClientes(Scanner scanner){
        mesas();

        System.out.print("Adcionar cliente em qual mesa? ");
        indice = scanner.nextInt() - 1;
        scanner.nextLine();

        if (mesas[indice].getNumClientes() == 4){
            System.out.println("Mesa Cheia");
        } else{
            do{
                mesas[indice].addClientes(scanner);
                System.out.print("\n1 - Sim  \n" +
                                 "2 - Não   \n");
                System.err.print("Deseja adicionar mais um cliente nessa mesa?: ");
            } while (scanner.nextLine().equalsIgnoreCase("1"));
        }
    }

    public void addConsumo(Scanner scanner){
        mesas();
        
        System.out.print("Adcionar pedido em qual mesa? ");
        indice = scanner.nextInt() - 1;
        scanner.nextLine();

        if (mesas[indice].getVazia()){
            System.out.println("Não possui clientes");
        } else{
            do{
                mesas[indice].addConsumo(scanner);
                System.out.print("\n1 - Sim  \n" +
                                 "2 - Não   \n");
                System.err.print("Deseja adicionar mais um pedido nessa mesa?: ");
            } while (scanner.nextLine().equalsIgnoreCase("1"));
        }
    }

    public void listarConsumo(Scanner scanner){
        mesas();

        System.out.print("Qual mesa deseja ver a lista de consumo? ");
        indice = scanner.nextInt() - 1;
        scanner.nextLine();

        if (mesas[indice].getTotal() == 0){
            System.out.println("Não possui pedidos");
        }

        else {
            mesas[indice].listarConsumo();
        }
    }

    public void fechaComanda(Scanner scanner){
        mesas();

        System.out.print("Qual mesa deseja fechar a conta? ");
        indice = scanner.nextInt() - 1;
        scanner.nextLine();

        if (mesas[indice].getNumClientes() == 0){
            System.out.println("Não possui clientes");
        }
        
        else {
            mesas[indice].gorjeta();

            System.out.println("\tValor da conta: R$" + mesas[indice].getTotal());
            System.out.println("\tValor para " + mesas[indice].getNumClientes() + " pessoas: R$" + mesas[indice].divideConta());

            mesas[indice] = new Mesa();
        }
    }

    public String getNome(){
        return this.nomeRestaurante;
    }

    public String getEndereco(){
        return this.endereco;
    }

    public int getNumMesas(){
        return numMesas;
    }
}
