#criando uma classe usando construtor
class Restaurante:
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'


restaurante_praca=Restaurante('Praça','Gourmet')
# restaurante_praca.nome='Rosa'
# restaurante_praca.categoria='Mexicana'

# restaurante_pizza=Restaurante()

# restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))
print(restaurante_praca)