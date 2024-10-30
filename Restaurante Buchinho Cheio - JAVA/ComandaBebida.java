public class ComandaBebida extends Comanda{
    
    @Override
    public void listarConsumo(){
        if (totalPedidos != 0){
            for (Pedidos pedidos : pedidos){
                System.out.println("\t\t" + pedidos.getNome() + " R$" + pedidos.getPreco());
            }
        }
    }
}
