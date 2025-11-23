from productController import ProductController
from front_end import iniciar_aplicacao
import time

def configurar_dados_iniciais(controller):
    print("--- Configurando Dados Iniciais ---")
    controller.adicionar({
        'id': 'FICC001', 'nome': 'Duna', 'autor': 'Frank Herbert', 'ano': 1965, 
        'preco': 55.50, 'estoque': 100, 'categoria': 'Ficção-Cientifíca', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'FICC002', 'nome': 'Fundação', 'autor': 'Isaac Asimov', 'ano': 1951, 
        'preco': 62.00, 'estoque': 80, 'categoria': 'Ficção-Cientifíca', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'FAN001', 'nome': 'Hobbit', 'autor': 'J.R.R. Tolkien', 'ano': 1937, 
        'preco': 70.00, 'estoque': 120, 'categoria': 'Fantasia', 'idioma': 'Inglês'
    })
    controller.adicionar({
        'id': 'ROM001', 'nome': 'Orgulho e Preconceito', 'autor': 'Jane Austen', 'ano': 1813, 
        'preco': 35.00, 'estoque': 50, 'categoria': 'Romance', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'SUSP001', 'nome': 'Garota no Trem', 'autor': 'Paula Hawkins', 'ano': 2015, 
        'preco': 40.00, 'estoque': 90, 'categoria': 'Suspense & Mistério', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'NAOF001', 'nome': 'Sapiens', 'autor': 'Yuval Noah Harari', 'ano': 2011, 
        'preco': 85.00, 'estoque': 60, 'categoria': 'Não-Ficção', 'idioma': 'Português'
    })
    
    controller.adicionar({
        'id': 'FAN002', 'nome': 'O Nome do Vento', 'autor': 'Patrick Rothfuss', 'ano': 2007, 
        'preco': 68.00, 'estoque': 75, 'categoria': 'Fantasia', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'ROM002', 'nome': 'A Culpa é das Estrelas', 'autor': 'John Green', 'ano': 2012, 
        'preco': 45.00, 'estoque': 110, 'categoria': 'Romance', 'idioma': 'Português'
    })
    controller.adicionar({
        'id': 'NAOF002', 'nome': 'Fator Humano', 'autor': 'Carol Tavris e Elliot Aronson', 'ano': 2019, 
        'preco': 75.00, 'estoque': 40, 'categoria': 'Não-Ficção', 'idioma': 'Inglês'
    })
    controller.adicionar({
        'id': 'SUSP002', 'nome': 'O Silêncio dos Inocentes', 'autor': 'Thomas Harris', 'ano': 1988, 
        'preco': 48.50, 'estoque': 65, 'categoria': 'Suspense & Mistério', 'idioma': 'Inglês'
    })
    controller.adicionar({
        'id': 'FICC003', 'nome': '1984', 'autor': 'George Orwell', 'ano': 1949, 
        'preco': 50.00, 'estoque': 150, 'categoria': 'Ficção-Cientifíca', 'idioma': 'Português'
    })
    # Nova Categoria Adicionada
    controller.adicionar({
        'id': 'TERR001', 'nome': 'It - A Coisa', 'autor': 'Stephen King', 'ano': 1986, 
        'preco': 65.00, 'estoque': 95, 'categoria': 'Terror', 'idioma': 'Português'
    })
    
    print("\nEstrutura de Categorias AVL")
    controller.arvore_categorias.imprimir_hierarquia(controller.arvore_categorias.raiz)

if __name__ == "__main__":
    app_controller = ProductController()
    configurar_dados_iniciais(app_controller)
    
    print("\nIniciando a Aplicação")
    iniciar_aplicacao(app_controller)