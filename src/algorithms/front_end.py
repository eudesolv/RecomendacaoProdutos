import tkinter as tk
from tkinter import Frame, Button, Label, Entry, ttk, messagebox
from productController import ProductController 

class Application:
    def __init__(self,ctrl):
        janela = tk.Tk()
        self.janela = janela
        self.livros = []
        self.livro_selecionado = None
        self.ctrl = ctrl

        self.tela()
        self.frames_tela()
        self.widgets()
        self.buttons()
        self.busca()
        self.tabela()

        self.listar_livros() 
        self.preencher_categorias()
        janela.mainloop()

    def tela(self):
        self.janela.title("Shoppe da Shoppe")
        self.janela.configure(bg ="#06223d")
        self.janela.geometry("1200x750")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 1400, height= 900 )
        self.janela.minsize(width= 1000, height= 650)

    def frames_tela(self):
        self.frame_1 = Frame(self.janela, bd = 4, bg = "#D3D3D3", highlightbackground= "#94A3B8", highlightthickness= 3  )
        self.frame_1.place(relx= 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.28 )

        self.frame_busca = Frame(self.janela, bd =4,  bg ="#D3D3D3", highlightbackground= "#94A3B8", highlightthickness= 2 )
        self.frame_busca.place(relx= 0.02, rely= 0.32, relwidth= 0.96, relheight= 0.1)

        self.frame_2 = Frame(self.janela, bd = 4, bg = "#D3D3D3", highlightbackground= "#94A3B8", highlightthickness= 2  )
        self.frame_2.place(relx= 0.02, rely= 0.46, relwidth= 0.96, relheight= 0.42)
    
    def widgets(self):
        self.label_codigo = Label(self.frame_1, text = "Código do Livro", bg ="#D3D3D3", font = ("Dosis", 10, "bold"))
        self.label_codigo.place(relx=0.02, rely=0.05, relwidth=0.12)
        self.id_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.id_entry.place(relx=0.02, rely=0.20, relwidth=0.12, relheight=0.15)

        self.label_nome = Label(self.frame_1, text = "Nome do Livro", bg = "#D3D3D3", font = ("Dosis", 10, "bold"))
        self.label_nome.place(relx=0.15, rely=0.05, relwidth=0.25)
        self.nome_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.nome_entry.place(relx=0.15, rely=0.20, relwidth=0.25, relheight=0.15)

        self.label_categoria = Label(self.frame_1, text = "Gêneros Literários", bg = "#D3D3D3", font = ("Dosis", 10, "bold"))
        self.label_categoria.place(relx=0.41, rely=0.05, relwidth=0.18)
        self.categoria_combo = ttk.Combobox(self.frame_1, font = ("Arial", 10), 
        values = ["Religião", "Ficção-Cientifíca", "Romance", "Suspence & Mistério", "Infantojuvenil", "Fantasia", "Não-Ficção", "Didáticos", "Auto-ajuda"], state= "readonly")
        self.categoria_combo.place(relx=0.41, rely=0.20, relwidth=0.18, relheight=0.15)

        self.label_autor = Label(self.frame_1, text= "Autor", bg= "#D3D3D3" , font = ("Dosi", 10, "bold"))
        self.label_autor.place(relx=0.60, rely=0.05, relwidth=0.18)
        self.autor_entry = Entry(self.frame_1, font= ("Arial", 10))
        self.autor_entry.place(relx=0.60, rely=0.20, relwidth=0.18, relheight=0.15)

        self.label_preco = Label(self.frame_1, bg = "#D3D3D3", text= "Valor (R$)", font= ("Dosi", 10, "bold"))
        self.label_preco.place(relx=0.02, rely=0.45, relwidth=0.12)
        self.preco_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.preco_entry.place(relx=0.02, rely=0.60, relwidth=0.12, relheight=0.15)

        self.label_estoque = Label (self.frame_1, text= "Estoque", bg="#D3D3D3", font= ("Dosi", 10, "bold"))
        self.label_estoque.place(relx=0.15, rely=0.45, relwidth=0.10)
        self.estoque_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.estoque_entry.place(relx=0.15, rely=0.60, relwidth=0.10, relheight=0.15)

        self.label_idioma = Label(self.frame_1, bg = "#D3D3D3", text = "Idioma", font= ("Dosi", 10, "bold"))
        self.label_idioma.place(relx=0.26, rely=0.45, relwidth=0.18)
        self.idioma_combo = ttk.Combobox(self.frame_1, font= ("Arial", 10), 
        values = ["Português", "Inglês", "Russo", "Espanhol"], state="readonly")
        self.idioma_combo.place(relx=0.26, rely=0.60, relwidth=0.18, relheight=0.15)

        self.label_ano = Label(self.frame_1, bg = "#D3D3D3", text = "Ano", font= ("Dosi", 10, "bold"))
        self.label_ano.place(relx=0.45, rely=0.45, relwidth=0.08)
        self.ano_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.ano_entry.place(relx=0.45, rely=0.60, relwidth=0.08, relheight=0.15)
        
        self.label_rec = Label(self.frame_1, bg = "#D3D3D3", text = "Cat. Raiz (Rec.)", font= ("Dosi", 10, "bold"))
        self.label_rec.place(relx=0.54, rely=0.45, relwidth=0.14)
        self.rec_combo = ttk.Combobox(self.frame_1, font= ("Arial", 10), state="readonly")
        self.rec_combo.place(relx=0.54, rely=0.60, relwidth=0.14, relheight=0.15)

    def buttons(self):
        self.bt_add = Button(self.frame_1, text= "➕ADICIONAR", command= self.add_livro, bg= "#05C70B", fg = "white", font= ("Dosi", 10, "bold"), cursor= "hand2")
        self.bt_add.place(relx=0.68, rely=0.55, relwidth=0.14, relheight=0.25)

        self.bt_att = Button(self.frame_1, text = "🔄 ATUALIZAR", command= self.att_livro, bg= "#DEDE14", fg= "white", font=("Dosi", 10, "bold"), cursor = "hand2")
        self.bt_att.place(relx=0.83, rely=0.55, relwidth=0.14, relheight=0.25)

        self.bt_remover = Button(self.frame_2, text= "🗑️REMOVER", command= self.remover_livro, bg="#FF2C2C", fg="white", font=("Dosi", 10, "bold"), cursor="hand2")
        self.bt_remover.place(relx=0.02, rely=0.87, relwidth=0.12, relheight=0.1)

        self.bt_listar = Button(self.frame_2, text= "📋LISTAR", command= self.listar_livros, bg= "#087DDE", fg= "white", font= ("Dosi", 10, "bold"), cursor= "hand2")
        self.bt_listar.place(relx=0.15, rely=0.87, relwidth=0.12, relheight=0.1)

        self.bt_limpar = Button(self.frame_2, text= "LIMPAR CAMPOS", command= self.limpar_campos, bg= "#9E9E9E", fg= "white", font= ("Dosi", 10, "bold"), cursor= "hand2")
        self.bt_limpar.place(relx=0.28, rely=0.87, relwidth=0.13, relheight=0.1)
        
        self.bt_recomendar = Button(self.frame_2, text= "⭐ RECOMENDAR", command= self.recomendar_livros, bg= "#E91E63", fg= "white", font= ("Dosi", 10, "bold"), cursor= "hand2")
        self.bt_recomendar.place(relx=0.42, rely=0.87, relwidth=0.15, relheight=0.1)

    def busca(self):
        self.label_buscar = Label(self.frame_busca, bg = "#D3D3D3", text= "Pesquisar 🔍", font= ("Dosi", 11, "bold"))
        self.label_buscar.place(relx=0.02, rely=0.25, relwidth=0.08)

        self.busca_entry = Entry(self.frame_busca, font = ("Arial", 10))
        self.busca_entry.place(relx=0.11, rely=0.20, relwidth=0.25, relheight=0.55)
        self.busca_entry.bind("<KeyRelease>", lambda e: self.buscar_livro())

        self.label_filtrar = Label(self.frame_busca, bg = "#D3D3D3", text= "Filtrar por:", font= ("Dosi", 10, "bold"))
        self.label_filtrar.place(relx=0.38, rely=0.25, relwidth=0.10)

        self.filtrar_combo = ttk.Combobox(self.frame_busca, font= ("Arial", 10), values= ["Todos", "Código", "Nome", "Autor", "Gênero", "Ano"], state= "readonly")
        self.filtrar_combo.set("Todos")
        self.filtrar_combo.place(relx=0.49, rely=0.20, relwidth=0.15, relheight=0.55)

        self.bt_buscar = Button(self.frame_busca, text= "🔍", command= self.buscar_livro, bg= "#2196F3", font= ("Arial", 12), cursor= "hand2")
        self.bt_buscar.place(relx=0.66, rely=0.15, relwidth=0.06, relheight=0.65)

        self.bt_limpar_busca= Button(self.frame_busca, text= "LIMPAR BUSCA", command= self.limpar_busca, bg= "#9E9E9E", font = ("Dosi", 10, "bold"), cursor= "hand2")
        self.bt_limpar_busca.place(relx=0.74, rely=0.15, relwidth=0.12, relheight=0.65)

    def tabela(self):
        self.frame_tabela = Frame(self.frame_2, bg="#D3D3D3")
        self.frame_tabela.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.80)
        
        scroll_y = ttk.Scrollbar(self.frame_tabela, orient="vertical")
        scroll_x = ttk.Scrollbar(self.frame_tabela, orient="horizontal")

        self.tree = ttk.Treeview(
            self.frame_tabela,
            columns=("Código", "Nome", "Gênero", "Autor", "Valor", "Estoque", "Idioma", "Ano"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
        )
            
        colunas = {"Código": 80, "Nome": 180, "Gênero": 150, "Autor": 120, "Valor": 60, "Estoque": 100, "Idioma": 80, "Ano": 100}
        
        for col, width in colunas.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        self.tree.bind("<<TreeviewSelect>>", self.selecionar_livro)

        self.tree.tag_configure("oddrow", background="#FFFFFF")
        self.tree.tag_configure("evenrow", background="#F0F0F0")
        self.tree.pack(fill="both", expand=True)

    def preencher_categorias(self):
        categorias = self.ctrl.arvore_categorias.travessia_em_ordem(self.ctrl.arvore_categorias.raiz)
        self.categoria_combo.config(values=categorias)
        self.rec_combo.config(values=categorias)
    
    def add_livro(self):
        dados = self.obter_dados_formulario()
        if not dados:
            return
        sucesso, mensagem = self.ctrl.adicionar(dados)
        
        if sucesso:
            self.listar_livros()
            self.limpar_campos()
            self.preencher_categorias() 
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)

    def att_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        dados = self.obter_dados_formulario()
        if not dados:
            return
        
        sucesso, mensagem = self.ctrl.atualizar(self.livro_selecionado, dados)
        
        if sucesso:
            self.listar_livros()
            self.limpar_campos()
            self.preencher_categorias() 
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)
        
        self.listar_livros()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")

    def remover_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente remover este livro?")
        if resposta:
            sucesso, mensagem = self.ctrl.remover(self.livro_selecionado)
            if sucesso:
                self.listar_livros()
                self.limpar_campos()
                self.preencher_categorias() 
                messagebox.showinfo("Sucesso", mensagem)
            else:
                messagebox.showerror("Erro", mensagem)

    def preencher_tabela(self, produtos): # foi usado varias vezes no cod do antonio, melhor transformar em uma função
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for idx, livro in enumerate(produtos):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(
                livro['id'], 
                livro['nome'], 
                livro['categoria'], 
                livro['autor'],
                f"R$ {livro['preco']:.2f}", 
                livro['estoque'], 
                livro['idioma'], 
                livro['ano']
            ), tags=(tag,))
    
    def buscar_livro(self):
        termo = self.busca_entry.get().strip().lower()
        filtro = self.filtrar_combo.get()
        
        if not termo:
            self.listar_livros()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        resultados = self.ctrl.buscar_por_termo(termo, filtro)
        self.preencher_tabela(resultados)

    def limpar_busca(self):
        self.busca_entry.delete(0, tk.END)
        self.filtrar_combo.set("Todos")
        self.listar_livros()

    def listar_livros(self):
        produtos = self.ctrl.listar()
        self.preencher_tabela(produtos)

    def selecionar_livro(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            codigo_selecionado = item['values'][0] 
            produto = self.ctrl.produtos_map.get(codigo_selecionado)
            
            if produto:
                livro = produto.to_dict()
                
                self.id_entry.delete(0, tk.END)
                self.id_entry.insert(0, livro['id'])
                
                self.nome_entry.delete(0, tk.END)
                self.nome_entry.insert(0, livro['nome'])
                
                self.categoria_combo.set(livro['categoria'])
                
                self.autor_entry.delete(0, tk.END)
                self.autor_entry.insert(0, livro['autor'])
                
                self.preco_entry.delete(0, tk.END)
                self.preco_entry.insert(0, str(livro['preco']))
                
                self.estoque_entry.delete(0, tk.END)
                self.estoque_entry.insert(0, str(livro['estoque']))
                
                self.idioma_combo.set(livro['idioma'])
                
                self.ano_entry.delete(0, tk.END)
                self.ano_entry.insert(0, str(livro['ano']))
                
                self.livro_selecionado = livro['id']
                
                self.id_entry.config(state='disabled')
        else:
            self.limpar_campos()

    def limpar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.ano_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.estoque_entry.delete(0, tk.END)
        self.categoria_combo.set("")
        self.idioma_combo.set("")
        self.rec_combo.set("") 
        self.livro_selecionado = None
        self.id_entry.config(state='normal')

    def obter_dados_formulario(self):
        codigo = self.id_entry.get().strip()
        nome = self.nome_entry.get().strip()
        autor = self.autor_entry.get().strip()
        ano = self.ano_entry.get().strip()
        preco = self.preco_entry.get().strip()
        estoque = self.estoque_entry.get().strip()
        categoria = self.categoria_combo.get().strip()
        idioma = self.idioma_combo.get().strip()
        
        if not all([codigo, nome, preco, estoque]):
            messagebox.showwarning("Atenção", "Preencha pelo menos: Código, Nome, Valor e Estoque!")
            return None
        
        try:
            preco_float = float(preco)
            estoque_int = int(estoque)
            ano_int = int(ano) if ano else 0
        except ValueError:
            messagebox.showerror("Erro", "Valores numéricos inválidos!")
            return None
        
        return {
            'codigo': codigo,
            'nome': nome,
            'autor': autor if autor else "-",
            'ano': ano_int,
            'preco': preco_float,
            'estoque': estoque_int,
            'categoria': categoria if categoria else "-",
            'idioma': idioma if idioma else "-"
        }

    def recomendar_livros(self):
        categoria_raiz = self.rec_combo.get().strip()
        if not categoria_raiz:
            messagebox.showwarning("Atenção", "Selecione uma Categoria para recomendação!")
            return
        produtos_recomendados, categorias_alvo = self.ctrl.recomendar_produtos_por_categoria(categoria_raiz)
        
        if not produtos_recomendados:
            messagebox.showinfo("Recomendação", f"Nenhum produto encontrado para a hierarquia '{categoria_raiz}'.")
            self.listar_livros()
            return
            
        self.preencher_tabela(produtos_recomendados)
        messagebox.showinfo("Recomendação", 
                            f"Mostrando {len(produtos_recomendados)} produtos das categorias:\n{', '.join(categorias_alvo)}")

def iniciar_aplicacao(ctrl):
    Application(ctrl)