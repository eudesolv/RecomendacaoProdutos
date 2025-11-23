from products import Produto
from srhp import ArvoreAVL

# atualizando os componentes para o que o antonio tinha adicionado no front, alterando a lógica para ser usada com srph e a arvoreavl, 
# incluindo o dicio para o mapeamento dos produtos, e instanciar a arvore para

class ProductController:
    def __init__(self):
        self.produtos = []
        self.produtos_map = {}
        self.arvore_categorias = ArvoreAVL()

    def adicionar(self, dados):
        id = dados["id"]
        produto = Produto(id, dados['nome'], dados['autor'], dados['ano'], dados['preco'], dados['estoque'], dados['categoria'], dados['idioma'])
        self.produtos.append(produto)
        self.produtos_map[id] = produto
        # se for categoria, insere na arvore
        self.arvore_categorias.inserir_categoria(dados['categoria'])
        return True, "Produto Adicionado"

    def listar(self):
        # precisa retornar como dicio pro view
        return [p.to_dict() for p in self.produtos]

    def atualizar(self, id, dados: dict):
        # atualizado para lidar com o mapa, ao invés dos ids
        if id not in self.produtos_map:
            return False, "Livro não encontrado"
        # coloquei as outras categorias tmb
        produto = self.produtos_map[id]
        produto.set_nome(dados['nome'])
        produto.set_autor(dados['autor'])
        produto.set_ano(dados['ano'])
        produto.set_preco(dados['preco'])
        produto.set_estoque(dados['estoque'])
        produto.set_idioma(dados['idioma'])
        # Se a categoria mudou, remove a antiga e insere a nova
        if produto.get_categoria() != dados['categoria']:
            produto.set_categoria(dados['categoria'])
            self.arvore_categorias.inserir_categoria(dados['categoria'])
        return True, "Livro atuaalizado"
    
    def remover(self, id):
        # atualizei para realmente remover :D
        if id not in self.produtos_map:
            return False, "Livro não encontrado"
        
        produto_a_remover = self.produtos_map[id]
        self.produtos.remove(produto_a_remover)
        # descobri del e agora nada me para de colocar quando precisar
        del self.produtos_map[id]
        
        categoria = produto_a_remover.get_categoria()
        if not any(p.get_categoria() == categoria for p in self.produtos):
             self.arvore_categorias.remover_categoria(categoria)

        return True, "Livro removido"
    
    def buscar_por_termo(self, termo, filtro):
        termo = termo.lower()
        resultados = []
        
        for produto in self.produtos:
            dados = produto.to_dict()
            encontrado = False
            
            if filtro == "Todos":
                if any(termo in str(v).lower() for v in dados.values()):
                    encontrado = True
            elif filtro == "Código" and termo == str(dados['codigo']).lower():
                encontrado = True
            elif filtro == "Nome" and termo in dados['nome'].lower():
                encontrado = True
            elif filtro == "Autor" and termo in dados['autor'].lower():
                encontrado = True
            elif filtro == "Gênero" and termo in dados['categoria'].lower():
                encontrado = True
            elif filtro == "Ano" and termo in str(dados['ano']):
                encontrado = True
                
            if encontrado:
                resultados.append(dados)
                
        return resultados

    def recomendar_produtos_por_categoria(self, categoria_raiz):
        categorias_alvo = self.arvore_categorias.listar_categorias_hierarquicas(categoria_raiz)
        
        produtos_recomendados = []
        for produto in self.produtos:
            if produto.get_categoria() in categorias_alvo:
                produtos_recomendados.append(produto.to_dict())
                
        return produtos_recomendados, categorias_alvo