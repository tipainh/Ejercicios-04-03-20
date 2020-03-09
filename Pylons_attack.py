# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:51:05 2020

@author: TiagoFilipe
"""

def mission(R,C):
    import numpy, random
    grid = numpy.zeros([R,C], dtype=int)                     #Creación del terreno
    print("\nGalaxy:\n", grid)
    start = random.choice(grid)                             #Colocación de la nave
    start[random.randint(0,len(start)-1)] += 1
    print("\nGalaxy. Ship set:\n", grid)
    
    for r in range(R):                                  #Localizar el punto de partida de la nave
        for c in range(C):
            if grid[r][c] == 1:
                ship = [r,c]
    
    moves = [ship]                                      #Celdas por las que ha pasado la nave
    aux = []                                            #Celdas a las cuales la nave puede ir

    for k in range(2,R*C+1):
        for r in range(R):                                       #Movimientos de la nave
            for c in range(C):
                if grid[r][c] == grid[ship[0]][ship[1]]:
                    for i in range(R):
                        for j in range(C):
                            if (r==i) or (c==j) or (r-c==i-j) or (r+c==i+j) or (0 < grid[i][j] < k):
                                continue
                            else:                                           
                                aux.append([i,j])
    
        print("Possible next moves:", aux)
        if aux == []:                                       #Si no hay movimientos posibles, se para
            break
        else:
            ship = random.choice(aux)                      #Elegir el movimiento                           
            grid[ship[0]][ship[1]] += k
            moves.append(ship)
    
        print("\nGalaxy:\n", grid)
        print("Moves so far:", moves)
        aux.clear()                                 #Reestablecer los posibles destinos de la nave
            
    
    if len(moves) == R*C:
        Y = "POSSIBLE"
        L = moves
        print(Y, "\n", L)
    else:
        Y = "IMPOSSIBLE"
        print(Y)
        
if __name__=="__main__":
    mission(2,5)