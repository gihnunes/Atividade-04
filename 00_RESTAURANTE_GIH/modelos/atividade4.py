# Definição da classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in lista_de_livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis

# Criação de instâncias da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("A Metamorfose", "Franz Kafka", 1915)

# Exibindo os livros criados
print(livro1)
print(livro2)

# Exemplo de empréstimo de um livro
livro1.emprestar()

# Lista de livros disponíveis de um determinado ano
ano_desejado = 1915
lista_de_livros = [livro1, livro2]  # Supondo que você tenha uma lista de livros

livros_disponiveis = Livro.verificar_disponibilidade(ano_desejado)
print(f"Livros disponíveis em {ano_desejado}:")
for livro in livros_disponiveis:
    print(livro)



def __str__(self):
    return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"

def emprestar(self):
    self.disponivel = False

@staticmethod
def verificar_disponibilidade(ano):
    livros_disponiveis = []
    for livro in lista_de_livros:
        if livro.ano_publicacao == ano and livro.disponivel:
            livros_disponiveis.append(livro)
    return livros_disponiveis

