class Biblioteca:
    def adicionar_livro(self, lista_de_livros, titulo, autor):
        livro = {
            'titulo': titulo,
            'autor': autor,
            'disponivel': True
        }
        lista_de_livros.append(livro)
        print(f'Livro "{titulo}" adicionado com sucesso.')

    def listar_livros(self, lista_de_livros):
        if not lista_de_livros:
            print("Nenhum livro cadastrado.")
            return
        print("Lista de Livros:")
        for livro in lista_de_livros:
            status = "Disponível" if livro['disponivel'] else "Emprestado"
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Status: {status}')

    def pesquisar_livro(self, lista_de_livros, titulo):
        for livro in lista_de_livros:
            if livro['titulo'].lower() == titulo.lower():
                status = "Disponível" if livro['disponivel'] else "Emprestado"
                print(f'Encontrado: Título: {livro["titulo"]}, Autor: {livro["autor"]}, Status: {status}')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def remover_livro(self, lista_de_livros, titulo):
        for i, livro in enumerate(lista_de_livros):
            if livro['titulo'].lower() == titulo.lower():
                del lista_de_livros[i]
                print(f'Livro "{titulo}" removido com sucesso.')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def emprestar_livro(self, lista_de_livros, titulo):
        for livro in lista_de_livros:
            if livro['titulo'].lower() == titulo.lower():
                if livro['disponivel']:
                    livro['disponivel'] = False
                    print(f'Livro "{titulo}" emprestado com sucesso.')
                else:
                    print(f'Livro "{titulo}" já está emprestado.')
                return
        print(f'Livro "{titulo}" não encontrado.')

biblioteca = Biblioteca()
lista_de_livros = []

biblioteca.adicionar_livro(lista_de_livros, "Dom Casmurro", "Machado de Assis")
biblioteca.adicionar_livro(lista_de_livros, "1984", "George Orwell")
biblioteca.listar_livros(lista_de_livros)
biblioteca.pesquisar_livro(lista_de_livros, "1984")
biblioteca.emprestar_livro(lista_de_livros, "1984")
biblioteca.listar_livros(lista_de_livros)
biblioteca.remover_livro(lista_de_livros, "Dom Casmurro")
biblioteca.listar_livros(lista_de_livros)
