import tkinter as tk
from tkinter import Frame, Button, Label, Entry, ttk, messagebox

class Application():
    def __init__(self):
        janela = tk.Tk()
        self.janela = janela
        self.livros = []
        self.livro_selecionado = None

        self.tela()
        self.frames_tela()
        self.widgets()
        self.buttons()
        self.busca()
        self.tabela()

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
        self.codigo_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.codigo_entry.place(relx=0.02, rely=0.20, relwidth=0.12, relheight=0.15)

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

        self.label_valor = Label(self.frame_1, bg = "#D3D3D3", text= "Valor (R$)", font= ("Dosi", 10, "bold"))
        self.label_valor.place(relx=0.02, rely=0.45, relwidth=0.12)
        self.valor_entry = Entry(self.frame_1, font = ("Arial", 10))
        self.valor_entry.place(relx=0.02, rely=0.60, relwidth=0.12, relheight=0.15)

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

        self.bt_buscar = Button(self.frame_busca, text= "🔍", command= self.buscar_livro, bg= "#2196F3", font= 12, cursor= "hand2")
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

    def add_livro(self):
        dados = self.obter_dados_formulario()
        if not dados:
            return
        
        for livro in self.livros:
            if livro['codigo'] == dados['codigo']:
                messagebox.showerror("Erro", "Código já cadastrado!")
                return
        
        self.livros.append(dados)
        self.listar_livros()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

    def att_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        dados = self.obter_dados_formulario()
        if not dados:
            return
        
        for livro in self.livros:
            if livro['codigo'] == self.livro_selecionado:
                livro.update(dados)
                break
        
        self.listar_livros()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")

    def remover_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente remover este livro?")
        if resposta:
            self.livros = [l for l in self.livros if l['codigo'] != self.livro_selecionado]
            self.listar_livros()
            self.limpar_campos()
            messagebox.showinfo("Sucesso", "Livro removido com sucesso!")

    def buscar_livro(self):
        termo = self.busca_entry.get().strip().lower()
        filtro = self.filtrar_combo.get()
        
        if not termo:
            self.listar_livros()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        resultados = []
        for livro in self.livros:
            if filtro == "Todos":
                if any(termo in str(v).lower() for v in livro.values()):
                    resultados.append(livro)
            elif filtro == "Código" and termo in str(livro['codigo']).lower():
                resultados.append(livro)
            elif filtro == "Nome" and termo in livro['nome'].lower():
                resultados.append(livro)
            elif filtro == "Autor" and termo in livro['autor'].lower():
                resultados.append(livro)
            elif filtro == "Gênero" and termo in livro['categoria'].lower():
                resultados.append(livro)
            elif filtro == "Ano" and termo in str(livro['ano']):
                resultados.append(livro)
        
        for idx, livro in enumerate(resultados):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(
                livro['codigo'], livro['nome'], livro['categoria'], livro['autor'],
                f"R$ {livro['valor']:.2f}", livro['estoque'], livro['idioma'], livro['ano']
            ), tags=(tag,))

    def limpar_busca(self):
        self.busca_entry.delete(0, tk.END)
        self.filtrar_combo.set("Todos")
        self.listar_livros()

    def listar_livros(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for idx, livro in enumerate(self.livros):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(
                livro['codigo'], 
                livro['nome'], 
                livro['categoria'], 
                livro['autor'],
                f"R$ {livro['valor']:.2f}", 
                livro['estoque'], 
                livro['idioma'], 
                livro['ano']
            ), tags=(tag,))

    def selecionar_livro(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            valores = item['values']
            
            for livro in self.livros:
                if livro['codigo'] == valores[0]:
                    self.codigo_entry.delete(0, tk.END)
                    self.codigo_entry.insert(0, livro['codigo'])
                    
                    self.nome_entry.delete(0, tk.END)
                    self.nome_entry.insert(0, livro['nome'])
                    
                    self.categoria_combo.set(livro['categoria'])
                    
                    self.autor_entry.delete(0, tk.END)
                    self.autor_entry.insert(0, livro['autor'])
                    
                    self.valor_entry.delete(0, tk.END)
                    self.valor_entry.insert(0, str(livro['valor']))
                    
                    self.estoque_entry.delete(0, tk.END)
                    self.estoque_entry.insert(0, str(livro['estoque']))
                    
                    self.idioma_combo.set(livro['idioma'])
                    
                    self.ano_entry.delete(0, tk.END)
                    self.ano_entry.insert(0, str(livro['ano']))
                    
                    self.livro_selecionado = livro['codigo']
                    break

    def limpar_campos(self):
        self.codigo_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.ano_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.estoque_entry.delete(0, tk.END)
        self.categoria_combo.set("")
        self.idioma_combo.set("")
        self.livro_selecionado = None

    def obter_dados_formulario(self):
        codigo = self.codigo_entry.get().strip()
        nome = self.nome_entry.get().strip()
        autor = self.autor_entry.get().strip()
        ano = self.ano_entry.get().strip()
        valor = self.valor_entry.get().strip()
        estoque = self.estoque_entry.get().strip()
        categoria = self.categoria_combo.get().strip()
        idioma = self.idioma_combo.get().strip()
        
        if not all([codigo, nome, valor, estoque]):
            messagebox.showwarning("Atenção", "Preencha pelo menos: Código, Nome, Valor e Estoque!")
            return None
        
        try:
            valor_float = float(valor)
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
            'valor': valor_float,
            'estoque': estoque_int,
            'categoria': categoria if categoria else "-",
            'idioma': idioma if idioma else "-"
        }

if __name__ == "__main__":
    Application()
