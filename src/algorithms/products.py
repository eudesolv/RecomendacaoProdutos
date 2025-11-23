class Produto:
    # coloquei o resto dos atributos
    def __init__(self, id, nome, autor, ano, preco, estoque, categoria, idioma):
        self.__id = id
        self.__nome = nome
        self.__autor = autor
        self.__ano = ano
        self.__preco = preco
        self.__estoque = estoque
        self.__categoria = categoria
        self.__idioma = idioma

    # Getters
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_autor(self):
        return self.__autor
    def get_ano(self):
        return self.__ano
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def get_categoria(self):
        return self.__categoria
    def get_idioma(self):
        return self.__idioma

    # Setters
    def set_nome(self, nome):
        self.__nome = nome
    def set_autor(self, autor):
        self.__autor = autor
    def set_ano(self, ano):
        self.__ano = ano
    def set_preco(self, preco):
        self.__preco = preco
    def set_estoque(self, estoque):
        self.__estoque = estoque
    def set_categoria(self, categoria):
        self.__categoria = categoria
    def set_idioma(self, idioma):
        self.__idioma = idioma
    
    # para uso no view
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'autor': self.__autor,
            'ano': self.__ano,
            'preco': self.__preco,
            'estoque': self.__estoque,
            'categoria': self.__categoria,
            'idioma': self.__idioma
        }

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__categoria}) | R$ {self.__preco} | Estoque: {self.__estoque}"