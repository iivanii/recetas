import csv
from typing import NamedTuple
from datetime import date
from typing import List
from datetime import datetime

#1

Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

#2

def lee_recetas(ruta):
    recetas=[]
    with open(ruta, encoding='utf-8') as f:
        lector=csv.reader(f,delimiter=';' )
        next(lector)
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            denominacion=str(denominacion)
            tipo=str(tipo)
            dificultad=str(dificultad)
            ingredientes=parsea_ingredientes(ingredientes)
            tiempo=int(tiempo)
            calorias=int(calorias)
            fecha=datetime.strptime(fecha, '%d/%m/%Y')
            precio= float(precio.replace(',','.'))
            receta= Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            recetas.append(receta)
    return recetas


def parsea_ingredientes(cadena_ingredientes:str):
    if len(cadena_ingredientes) != 0:
        lista_ingredientes=[]
        cadena_ingredientes=cadena_ingredientes.split(',')
        for i in cadena_ingredientes:
            ingrediente=parsea_ingrediente(i)
            lista_ingredientes.append(ingrediente)
    else:
        lista_ingredientes=[]
    return lista_ingredientes

def parsea_ingrediente(ingrediente_pars:str):
    ingrediente_pars=ingrediente_pars.split('-')
    nombre, cantidad, unidad = ingrediente_pars
    nombre= str(nombre)
    cantidad=float(cantidad)
    unidad=str(unidad)
    ingrediente_fix=Ingrediente(nombre, cantidad, unidad)
    return ingrediente_fix

#3
  

def ingredientes_en_unidad(registro:List[Receta],unidad_medida:str = None):
    ingredientes_distintos=[]
    for r in registro:
        if len(r.ingredientes) != 0:
            for i in r.ingredientes:
                if i.nombre not in ingredientes_distintos and i.unidad == unidad_medida:
                    ingredientes_distintos.append(i.nombre)
                elif unidad_medida== None and i.nombre not in ingredientes_distintos:
                    ingredientes_distintos.append(i.nombre)
    return len(ingredientes_distintos)


#4

def recetas_con_ingredientes(registro:List[Receta],nombres:set):
    res=[]
    for r in registro:
        for i in r.ingredientes:
            dcp=(r.denominacion, r.calorias, r.precio)
            if i.nombre in nombres and dcp not in res:
                res.append(dcp)
    return res

#5

def receta_mas_barata(registro:List[Receta],recetas:set,n:int = None):
    registro.sort(key=lambda x: x.precio)
    n_mas_baratas=[]
    for i in registro:
        if len(n_mas_baratas) < n and i.tipo in recetas:
            n_mas_baratas.append(i)
    
    n_mas_baratas.sort(key=lambda x:x.calorias)


    return n_mas_baratas[0]


#6

from statistics import mean

def recetas_baratas_con_menos_calorias(registro:List[Receta],n:int):
    registro.sort(key=lambda x:x.calorias)
    res=[]
    for r in registro:
        if len(res) < n:
            res.append(r)

    precio_medio=mean([e.precio for e in registro])
    sol=[]
    for i in res:
        if i.precio <= precio_medio:
            nombre_calorias=(i.denominacion, i.calorias)
            sol.append(nombre_calorias)
    print(res)

    return sol






