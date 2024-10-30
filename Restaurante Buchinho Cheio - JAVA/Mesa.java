import java.util.Scanner;

public class Mesa{
    private boolean vazia = true;
    private Cliente[] clientes = new Cliente[5];
    private ComandaBebida bebidas = new ComandaBebida();
    private ComandaComida comidas = new ComandaComida();
    private int totalClientes;

    public Mesa (){
        for (int i = 0; i < clientes.length; i++){
            clientes[i] = new Cliente();
        }
    }

    public void addClientes(Scanner scanner){
        vazia = false;

        System.out.print("\tNome do cliente: ");
        clientes[totalClientes].setNome(scanner.nextLine());

        System.out.print("\tEmail do cliente: ");
        clientes[totalClientes].setEmail(scanner.nextLine());

        totalClientes++;
    }

    public void addConsumo(Scanner scanner){
        int opcao;

        do {
            System.out.print("\tDeseja adicionar uma bebida (1) ou uma comida (2)? ");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao){
                case 1:
                    bebidas.addPedidos(scanner);
                    break;

                case 2:
                    comidas.addPedidos(scanner);
                    break;
            }
        } while (opcao < 1 || opcao > 2);
    }

    public void listarConsumo(){
        comidas.listarConsumo();
        bebidas.listarConsumo();
    }

    public double divideConta(){
        return bebidas.getTotal() / totalClientes + comidas.getTotal() / totalClientes;
    }

    public double getTotal(){
        return bebidas.getTotal() + comidas.getTotal();
    }

    public void gorjeta(){
        bebidas.gorjeta();
        comidas.gorjeta();
    }

    public Cliente[] getClientes(){
        return this.clientes;
    }

    public int getNumClientes(){
        return this.totalClientes;
    }

    public boolean getVazia(){
        return vazia;
    }
}
