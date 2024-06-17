#criando uma classe usando decoreitor @property

from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes=[]
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self._ativo=False
        self.avalicao=[]
        Restaurante.restaurantes.append(self)

    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐' 
    
    def _alternar_estado(self):
        self._ativo =not self._ativo

    def receber_avaliacao(self,cliente,nota):
        if 0<nota<=5:
            avaliacao=Avaliacao(cliente,nota)
            self.avaliacao.append(avaliacao)




#restaurante_praca=Restaurante('Praça','Gourmet')
#restaurante_pizza=Restaurante('Rosa','mexicana')
# restaurante_praca.nome='Rosa'
# restaurante_praca.categoria='Mexicana'

# restaurante_pizza=Restaurante()

# restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))
#Restaurante.listar_restaurantes()