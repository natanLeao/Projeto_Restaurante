import java.util.Scanner;

public class Comanda{
    protected Pedidos[] pedidos = new Pedidos[1];
    protected int totalPedidos = 0;
    protected double valorTotal = 0;

    public void addPedidos(Scanner scanner){
        if (pedidos[pedidos.length - 1] != null){
            Pedidos[] novoArray = new Pedidos[pedidos.length + 1];
    
            for (int j = 0; j < pedidos.length; j++){
                novoArray[j] = pedidos[j];
            }
    
            pedidos = new Pedidos[novoArray.length];
    
            for (int j = 0; j < novoArray.length; j++){
                pedidos[j] = novoArray[j];
            }
        }
        
        pedidos[pedidos.length - 1] = new Pedidos();

        System.out.print("\t\tDigite o nome do pedido: ");
        pedidos[pedidos.length - 1].setNome(scanner.nextLine());

        System.out.print("\t\tDigite o preço do pedido: ");
        pedidos[pedidos.length - 1].setPreco(scanner.nextDouble());

        valorTotal += pedidos[pedidos.length - 1].getPreco();
        totalPedidos++;
    }

    public void listarConsumo(){
        if (totalPedidos != 0){
            for (Pedidos pedidos : pedidos){
                System.out.println("\t\t" + pedidos.getNome() + " R$" + pedidos.getPreco());
            }
        }
    }

    public void gorjeta(){
        valorTotal *= 1.1;
    }

    public double getTotal(){
        return this.valorTotal;
    }
}
