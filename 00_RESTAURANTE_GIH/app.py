from modelos.restaurante4 import Restaurante

restaurante1=Restaurante('Le Petit Chef',' Francês')
restaurante2=Restaurante('SushiMoto','Japonês')
restaurante3=Restaurante('Mamma Mia Trattoria','Italiano')

restaurante1.alternar_status()

restaurante2.receber_avaliacao("Brenda", 4)
restaurante3.receber_avaliacao("Vitoria", 3)

def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()