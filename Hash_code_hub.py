# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:58:29 2020

@author: TiagoFilipe
"""

def order_pizza(M,N,S):
    slices_total = sum(S)                   #Esto era inicialmente para separar ese caso de los demás
    if slices_total > M :
        from itertools import combinations    #Esto es para hacer las combinaciones posibles y coger la mayor
        for i in range(1,N):                #Variar la longitud de las combinaciones
            for j in (i,N):                      #Iterar las combinaciones
                for comb in combinations(S,j):
                    for k in range(M,0,-1):         #Para ver si alguna comb. suma M y sino M-1, M-2...
                        if sum(comb) == k :
                            slices_total = list(comb)         
                            print(slices_total, "=", k)                               

    """
    El problema es que no consigo expresar como pretendo que si sum(comb) no es M, que evalúe M-1 y después
    (si ninguna combinación da eso) M-2, etc. Ahora lo hace bien, es decir, llega hasta el [2,6,8] que es
    16 (M-1), pero cómo podría hacer para que se quede únicamente con la combinación que da la suma más alta?
    Porque de esta manera se queda con la última combinación (que en este caso vale, pero no siempre). Por
    ejemplo, con M=14, la solución es la combinación [6,8], pero esto se queda con [2,5,6]
    """
    
    K = len(slices_total)                               #Un esbozo de lo que hay que hacer después
    print("K =", K)
    L = []                           
    for i in range(0,K):
        pos = S.index(slices_total[i])                  
        L.append(pos)                    
    print("L =", L)

if __name__=="__main__":
    order_pizza(17, 4, [2,5,6,8])