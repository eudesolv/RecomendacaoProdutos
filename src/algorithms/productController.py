from products import Produto

class ProdutController:
    def __init__(self):
        self.produtos = []
        self.next_id = 1

    def adicionar(self, nome, preco, estoque):
        produto = Produto(self.next_id, nome, preco, estoque)
        self.produtos.append(produto)
        self.next_id += 1
        return produto

    def listar(self):
        return self.produtos

    def atualizar(self, id, nome=None, preco=None, estoque=None):
        for produto in self.produtos:
            if produto.get_id() == id:
                if nome is not None: produto.set_nome(nome)
                if preco is not None: produto.set_preco(preco)
                if estoque is not None: produto.set_estoque(estoque)
                return True
        return False

    def remover(self, id):
        for produto in self.produtos:
            if produto.get_id() == id:
                self.produtos.remove(produto)
                return True
        return False