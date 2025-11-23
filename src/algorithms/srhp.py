class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.produtos_por_categoria = {}

    class NoAVL:
        def __init__(self, dado):
            self.dado = dado
            self.altura = 1
            self.esquerda = None
            self.direita = None

    def _get_altura(self, no):
        return no.altura if no else 0

    def _get_fb(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _atualizar_altura(self, no):
        if no:
            no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def inserir_categoria(self, dado):
        if dado not in self.produtos_por_categoria:
            self.produtos_por_categoria[dado] = []
        self.raiz = self._inserir_recursivo(self.raiz, dado)

    def _inserir_recursivo(self, raiz_atual, dado):
        if not raiz_atual:
            return self.NoAVL(dado)

        if dado < raiz_atual.dado:
            raiz_atual.esquerda = self._inserir_recursivo(raiz_atual.esquerda, dado)
        elif dado > raiz_atual.dado:
            raiz_atual.direita = self._inserir_recursivo(raiz_atual.direita, dado)
        else:
            return raiz_atual

        self._atualizar_altura(raiz_atual)
        fb = self._get_fb(raiz_atual)

        if fb > 1 and dado < raiz_atual.esquerda.dado:
            return self._rotacao_direita(raiz_atual)

        if fb < -1 and dado > raiz_atual.direita.dado:
            return self._rotacao_esquerda(raiz_atual)

        if fb > 1 and dado > raiz_atual.esquerda.dado:
            raiz_atual.esquerda = self._rotacao_esquerda(raiz_atual.esquerda)
            return self._rotacao_direita(raiz_atual)

        if fb < -1 and dado < raiz_atual.direita.dado:
            raiz_atual.direita = self._rotacao_direita(raiz_atual.direita)
            return self._rotacao_esquerda(raiz_atual)

        return raiz_atual

    def buscar_categoria(self, dado):
        return self._buscar_recursivo(self.raiz, dado)

    def _buscar_recursivo(self, no_atual, dado):
        if no_atual is None:
            return None

        if dado == no_atual.dado:
            return no_atual
        elif dado < no_atual.dado:
            return self._buscar_recursivo(no_atual.esquerda, dado)
        else:
            return self._buscar_recursivo(no_atual.direita, dado)
        
    def _get_sucessor(self, no):
        no_atual = no.direita
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual
    
    def remover_categoria(self, dado):
        self.raiz = self._remover_recursivo(self.raiz, dado)
        if dado in self.produtos_por_categoria:
            del self.produtos_por_categoria[dado]
            
    def _remover_recursivo(self, raiz_atual, dado):
        if raiz_atual is None:
            return raiz_atual

        if dado < raiz_atual.dado:
            raiz_atual.esquerda = self._remover_recursivo(raiz_atual.esquerda, dado)
        elif dado > raiz_atual.dado:
            raiz_atual.direita = self._remover_recursivo(raiz_atual.direita, dado)
        else:
            if raiz_atual.esquerda is None or raiz_atual.direita is None:
                temp = raiz_atual.esquerda if raiz_atual.esquerda is not None else raiz_atual.direita
                raiz_atual = temp
            else:
                temp = self._get_sucessor(raiz_atual)
                raiz_atual.dado = temp.dado
                raiz_atual.direita = self._remover_recursivo(raiz_atual.direita, temp.dado)

        if raiz_atual is None:
            return raiz_atual

        self._atualizar_altura(raiz_atual)
        fb = self._get_fb(raiz_atual)

        if fb > 1 and self._get_fb(raiz_atual.esquerda) >= 0:
            return self._rotacao_direita(raiz_atual)

        if fb > 1 and self._get_fb(raiz_atual.esquerda) < 0:
            raiz_atual.esquerda = self._rotacao_esquerda(raiz_atual.esquerda)
            return self._rotacao_direita(raiz_atual)

        if fb < -1 and self._get_fb(raiz_atual.direita) <= 0:
            return self._rotacao_esquerda(raiz_atual)

        if fb < -1 and self._get_fb(raiz_atual.direita) > 0:
            raiz_atual.direita = self._rotacao_direita(raiz_atual.direita)
            return self._rotacao_esquerda(raiz_atual)

        return raiz_atual

    def cadastrar_produto_em_categoria(self, nome_categoria, nome_produto):
        no_categoria = self.buscar_categoria(nome_categoria)
        if no_categoria:
            print(f"Produto '{nome_produto}' cadastrado na categoria '{nome_categoria}'.")
            return True
        else:
            print(f"Erro: Categoria '{nome_categoria}' não encontrada.")
            return False

    def recomendar_produtos(self, categoria_raiz):
        no_raiz = self.buscar_categoria(categoria_raiz)
        if not no_raiz:
            return f"Categoria '{categoria_raiz}' não encontrada para recomendação."

        print(f"Recomendacao para a Categoria Raiz: {categoria_raiz}")
        print("---")

        produtos_recomendados = self._get_produtos_recursivo(no_raiz)

        if produtos_recomendados:
            return f"Produtos recomendados (incluindo subcategorias): {', '.join(produtos_recomendados)}"
        else:
            return "Nenhum produto encontrado nesta hierarquia (simulada)."

    def _get_produtos_recursivo(self, no_atual):
        categorias = []
        if no_atual:
            categorias.append(no_atual.dado)
            categorias.extend(self._get_produtos_recursivo(no_atual.esquerda))
            categorias.extend(self._get_produtos_recursivo(no_atual.direita))
        return categorias
    
    def listar_categorias_hierarquicas(self, categoria_raiz=None):
        if categoria_raiz:
            no_raiz = self.buscar_categoria(categoria_raiz)
        else:
            no_raiz = self.raiz
            
        return self._get_produtos_recursivo(no_raiz)

    def travessia_em_ordem(self, no_atual):
        resultado = []
        if no_atual:
            resultado.extend(self.travessia_em_ordem(no_atual.esquerda))
            resultado.append(no_atual.dado)
            resultado.extend(self.travessia_em_ordem(no_atual.direita))
        return resultado
    
    def imprimir_hierarquia(self, no_atual, nivel=0):
        if no_atual is not None:
            # 1. Recuo
            prefixo = "    " * nivel
            
            # 2. Imprime o nó atual (Raiz)
            print(f"{prefixo}|- {no_atual.dado}")
            
            # 3. Percorre a subárvore esquerda
            self.imprimir_hierarquia(no_atual.esquerda, nivel + 1)
            
            # 4. Percorre a subárvore direita
            self.imprimir_hierarquia(no_atual.direita, nivel + 1)