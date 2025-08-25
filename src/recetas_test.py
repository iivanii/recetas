from recetas import *
ruta= 'C:\\Users\\ivanb\\Desktop\\myp\\LAB-Recetas-main\\data\\recetas.csv'
registro=lee_recetas(ruta)

def test_lee_recetas():
    registro=lee_recetas(ruta)
    print(registro)

def test_ingredientes_en_unidad():
    ieu=ingredientes_en_unidad(registro,'gr')
    print(ieu)

def test_recetas_con_ingredientes():
    rci=recetas_con_ingredientes(registro,{'pimiento', 'tomate', 'cebolla'})
    print(rci)

def test_receta_mas_barata():
    rmb=receta_mas_barata(registro,   {'Postre', 'Plato Principal'}, 5)
    print(rmb)

def test_recetas_mas_baratas_con_menos_calorias():
    rmbcmc=recetas_baratas_con_menos_calorias(registro, 5)
    print(rmbcmc)

if __name__ == '__main__':
    #test_lee_recetas()
    #test_ingredientes_en_unidad()
    #test_recetas_con_ingredientes()
    #test_receta_mas_barata()
    test_recetas_mas_baratas_con_menos_calorias()