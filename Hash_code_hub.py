# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:58:29 2020

@author: TiagoFilipe
"""

def order_pizza(M,N,S):
    from itertools import combinations    #Esto es para hacer las combinaciones posibles y coger la mayor
    auxk = []
    aux = []
    for i in range(1,N):                #Variar la longitud de las combinaciones
        for j in (i,N):                      #Iterar las combinaciones
            for comb in combinations(S,j):
                for k in range(M,0,-1):         #Para ver si alguna comb. suma M y sino M-1, M-2...
                    if sum(comb) == k :
                        slices_comb = list(comb)
                        aux.append(slices_comb)
                        auxk.append(k)
                        #print(slices_comb, "=", k)
    
    for sublist in aux:                             #Este bloque es para elegir la opción óptima
        if (max(auxk)) == (sum(sublist)):
            slices_comb_opt = sublist
    
    K = len(slices_comb_opt)                               
    print("K =", K)
    L = []                           
    for i in range(0,K):
        pos = S.index(slices_comb_opt[i])                  
        L.append(pos)                    
    print("L =", L)

if __name__=="__main__":
    order_pizza(17, 4, [2,5,6,8])