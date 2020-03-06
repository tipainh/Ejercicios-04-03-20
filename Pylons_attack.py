# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:51:05 2020

@author: TiagoFilipe
"""

def mission(R,C):
    import numpy, random
    grid = numpy.zeros([R,C], dtype=int)                     #Creación del terreno
    print("\nGalaxy:\n", grid)
    ship_0 = random.choice(grid)
    ship_0[random.randint(0,len(ship_0)-1)] += 1
    print("\nGalaxy:\n", grid)


if __name__=="__main__":
    mission(2,5)