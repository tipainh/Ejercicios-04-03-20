# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:51:05 2020

@author: TiagoFilipe
"""

def mission(R,C):
    import numpy, random
    grid = numpy.zeros([R,C], dtype=int)                     #Creación del terreno
    print("\nGalaxy:\n", grid)
    ship_0 = random.choice(grid)                             #Colocación de la nave
    ship_0[random.randint(0,len(ship_0)-1)] += 1
    print("\nGalaxy. Ship set:\n", grid)
    
    for r in range(R):                                       #Movimientos de la nave
        for c in range(C):
            if grid[r][c] == 1:
                for i in range(R):
                    for j in range(C):
                        if (r==i) or (c==j) or (r-c==i-j) or (r+c==i+j):
                            continue
                        else:                                           #mal
                            grid[random.randint(0,i)][random.randint(0,j)]=1
    print("\nGalaxy:\n", grid)

if __name__=="__main__":
    mission(2,5)