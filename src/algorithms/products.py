class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def __str__(self):
        return f"{self.__id} - {self.__nome} | R$ {self.__preco} | Estoque: {self.__estoque}"