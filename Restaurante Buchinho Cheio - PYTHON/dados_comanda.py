import sqlite3
from pedido import Pedido

class BancoDados:
    def __init__(self, nome_banco='restaurante.db'):
        self.nome_banco = nome_banco
        self.conectar_banco()

    def conectar_banco(self):
        # Conecta ao banco de dados (ou cria se não existir)
        return sqlite3.connect(self.nome_banco)

    def criar_tabelas(self):
        conn = self.conectar_banco()
        cursor = conn.cursor()

        # Cria a tabela comidas se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comidas (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            )
        ''')

        # Cria a tabela bebidas se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bebidas (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def inserir_comidas_iniciais(self):
        comidas_iniciais = [
            ("Feijoada", 25.00),
            ("Pão de Queijo", 8.00),
            ("Coxinha", 7.00),
            ("Brigadeiro", 3.00),
            ("Pastel", 5.00),
            ("Acarajé", 12.00),
            ("Moqueca", 30.00),
            ("Baião de Dois", 20.00),
            ("Farofa", 6.00),
            ("Esfiha", 6.00),
            ("Kibe", 7.00),
            ("Quindim", 4.00),
            ("Tapioca", 8.00),
            ("Arroz e Feijão", 10.00),
            ("Bolinho de Bacalhau", 9.00),
            ("Mousse de Maracujá", 5.00),
            ("Picanha", 35.00),
            ("Churrasco", 30.00),
            ("Carne de Sol", 22.00),
            ("Cuscuz", 7.00),
            ("Salpicão", 15.00),
            ("Sopa de Ervilha", 9.00),
            ("Pudim", 6.00),
            ("Bolo de Cenoura", 7.00),
            ("Bolo de Chocolate", 8.00),
            ("Mandioca Frita", 10.00),
            ("Salada de Frutas", 6.00),
            ("Peixe na Brasa", 25.00),
            ("Lasanha", 20.00),
            ("Pasta de Grão de Bico", 8.00),
            ("Torta de Limão", 5.00),
            ("Bacalhau à Brás", 28.00),
            ("Torta de Palmito", 12.00),
            ("Milho Verde", 4.00),
            ("Frango à Passarinho", 15.00),
            ("Sushi Brasileiro", 18.00),
            ("Sanduíche de Mortadela", 10.00),
            ("Hambúrguer", 15.00),
            ("Churrasquinho", 12.00),
            ("Cuscuz Paulista", 10.00),
            ("Geladinho", 2.00),
            ("Pipoca", 4.00),
            ("Crepe", 8.00),
            ("Paleta Mexicana", 6.00),
            ("Canjica", 5.00),
            ("Quibe Assado", 9.00),
            ("Pamonha", 6.00),
            ("Carne Moída", 15.00),
            ("Salada Caesar", 12.00),
            ("Empada", 7.00),
            ("Pudim de Leite", 6.00),
            ("Romeu e Julieta", 5.00),
            ("Açaí", 10.00),
            ("Chá de Hibisco", 4.00),
            ("Pé de Moleque", 3.00),
            ("Farinha de Mandioca", 3.00),
            ("Pão com Linguiça", 8.00),
            ("Café com Leite", 5.00),
            ("Fricassê de Frango", 20.00),
            ("Galinhada", 18.00),
            ("Bolo de Fubá", 6.00),
            ("Canelone", 15.00),
            ("Estrogonofe", 20.00),
            ("Sopa de Cebola", 9.00),
            ("Rondelli", 12.00),
            ("Bolo de Rolo", 8.00),
            ("Arroz à Grega", 10.00),
            ("Peixe ao Molho", 22.00),
            ("Tortinha de Frango", 9.00),
            ("Bolo de Beterraba", 7.00),
            ("Mousse de Chocolate", 6.00),
            ("Salada de Batata", 10.00),
            ("Quiche", 12.00),
            ("Arroz de Pato", 25.00),
            ("Bacalhau ao Forno", 30.00),
            ("Bolo de Maçã", 6.00),
            ("Bebida de Leite com Chocolate", 4.00),
            ("Torta de Frutas", 10.00),
            ("Cuscuz Nordestino", 8.00),
            ("Pavê", 8.00),
            ("Bolo de Milho", 6.00),
            ("Rocambole", 7.00),
            ("Peixe Frito", 20.00),
            ("Frango Grelhado", 15.00),
            ("Batata Frita", 6.00),
            ("Omelete", 8.00),
            ("Pasta de Atum", 7.00),
            ("Ceviche", 18.00),
            ("Frango com Quiabo", 18.00),
            ("Linguiça Calabresa", 12.00),
            ("Chester", 25.00),
            ("Coxão Mole", 30.00),
            ("Bolo de Aniversário", 10.00),
            ("Bolo de Laranja", 6.00)
        ]

        conn = self.conectar_banco()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM comidas")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO comidas (nome, preco) VALUES (?, ?)", comidas_iniciais)
            conn.commit()

        conn.close()

    def inserir_bebidas_iniciais(self):
        bebidas_iniciais = [
            ("Cerveja", 7.00),
            ("Vinho Tinto", 15.00),
            ("Vinho Branco", 14.00),
            ("Vodka", 12.00),
            ("Whisky", 20.00),
            ("Rum", 18.00),
            ("Tequila", 16.00),
            ("Cachaça", 10.00),
            ("Gin", 12.00),
            ("Limonada", 5.00),
            ("Refrigerante", 4.00),
            ("Água Mineral", 3.00),
            ("Suco de Laranja", 6.00),
            ("Suco de Maçã", 6.00),
            ("Smoothie de Frutas", 8.00),
            ("Chá Gelado", 4.50),
            ("Café", 3.00),
            ("Chocolate Quente", 5.00),
            ("Milkshake", 9.00),
            ("Sangria", 10.00),
            ("Margarita", 14.00),
            ("Mojito", 12.00),
            ("Piña Colada", 12.00),
            ("Caipirinha", 8.00),
            ("Bloody Mary", 10.00),
            ("Bellini", 10.00),
            ("Dry Martini", 15.00),
            ("Mai Tai", 14.00),
            ("Negroni", 15.00),
            ("Old Fashioned", 16.00),
            ("Cosmopolitan", 14.00),
            ("Aperol Spritz", 12.00),
            ("Paloma", 12.00),
            ("Espresso Martini", 14.00),
            ("Manhattan", 16.00),
            ("Bourbon", 18.00),
            ("Pilsner", 7.00),
            ("Stout", 8.00),
            ("Porto", 18.00),
            ("Champanhe", 25.00),
            ("Sidra", 10.00),
            ("Sake", 12.00),
            ("Cerveja Artesanal", 9.00),
            ("Chopp", 5.00),
            ("Tônica", 4.00),
            ("Água com Gás", 3.50),
            ("Energético", 6.00),
            ("Fanta", 4.00),
            ("Coca-Cola", 4.00),
            ("Guaraná", 4.00),
            ("Sprite", 4.00),
            ("Soda Limonada", 5.00),
            ("Água de Coco", 7.00),
            ("Chá Mate", 3.50),
            ("Mate Leão", 4.00),
            ("Capuccino", 6.00),
            ("Frappuccino", 7.00),
            ("Pisco Sour", 12.00),
            ("Mai Tai", 14.00),
            ("Daiquiri", 12.00),
            ("Whiskey Sour", 14.00),
            ("Long Island Iced Tea", 16.00),
            ("Sex on the Beach", 14.00),
            ("Tequila Sunrise", 12.00),
            ("Blue Lagoon", 12.00),
            ("Cuba Libre", 12.00),
            ("Rabo de Galo", 10.00),
            ("Café com Licor", 8.00),
            ("Jägermeister", 10.00),
            ("Absinto", 20.00),
            ("Fresco", 6.00),
            ("Bebida Energética", 5.00),
            ("Ginger Ale", 4.50),
            ("Frescolita", 5.00),
            ("Açaí", 8.00),
            ("Sucos Naturais", 7.00),
            ("Drink de Frutas", 9.00),
            ("Panna Cotta com Licor", 9.00),
            ("Licor de Chocolate", 10.00),
            ("Licor de Frutas", 10.00),
            ("Aperitivo", 9.00),
            ("Tinto de Verano", 10.00),
            ("Cerveja Sem Álcool", 5.00),
            ("Smoothie de Banana", 8.00),
            ("Lassi", 7.00),
            ("Água Aromatizada", 4.00),
            ("Chá de Hibisco", 4.00),
            ("Bebida de Soja", 5.00),
            ("Sopa Fria de Tomate", 6.00),
            ("Bebida de Iogurte", 7.00),
            ("Cerveja de Frutas", 8.00),
            ("Bebida de Leite", 4.00),
            ("Cerveja com Limão", 6.00),
            ("Cocktail de Frutas", 10.00),
            ("Drink Tropical", 12.00),
            ("Sangue de Dragão", 14.00),
            ("Drambuie", 18.00),
            ("Baileys", 12.00)
        ]

        conn = self.conectar_banco()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM bebidas")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO bebidas (nome, preco) VALUES (?, ?)", bebidas_iniciais)
            conn.commit()

        conn.close()

    def carregar_menu(self, tipo):
        produtos = []
        conn = self.conectar_banco()
        cursor = conn.cursor()

        if tipo == 'comidas':
            cursor.execute("SELECT nome, preco FROM comidas")
        else:
            cursor.execute("SELECT nome, preco FROM bebidas")

        for nome, preco in cursor.fetchall():
            produtos.append(Pedido(nome, preco))

        conn.close()
        return produtos

