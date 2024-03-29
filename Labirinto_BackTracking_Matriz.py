# -*- coding: utf-8 -*-
import numpy as np
import random

class matrix: # tad matrix para gerar e guardar a matriz do problema.
    def __init__(self,tam):
        self.matriz = np.zeros((tam,tam), dtype=np.float64) #inicializa matriz com zero
        self.k=tam
        self.l=tam
        self.fim=(0,0)
        self.inicio =(0,0)
    def setIndice(self,i,j,v):
        self.matriz[i][j]=v
    def getIndice(self,i,j):
        return self.matriz[i][j]
    def setInicio(self,i,j):
        self.inicio = (i,j)
    def setFim(self,i,j):
        self.fim=(i,j)

    
def passo(x,y,matrix,tam):  # verifica se o passo é válido
    if(x>=0 and x<tam and y>=0 and y<tam and matrix[x][y]==1):
        return True
    else:
        return False
    

def encontrarSolucao( matrix,tam ):
    spath= np.zeros((tam,tam), dtype=np.float64) # cria matriz solução com zeros
    arquivo = open('labirinto.txt','a')   # escrever solução em txt
    inicioI=int(input("inicio i : "))
    inicioJ=int(input("inicio j : "))
    if caminho(inicioI,inicioJ,matrix, spath,tam,0,int(input("Fim i: ")),int(input("Fim j: "))) == False: #se retornar false não tem solução
            print("Sem solução"); 
            arquivo.writelines("\n SEM SOLUÇÃO ! \n")
            return False
    print(spath)
    arquivo = open('labirinto.txt','a')
    arquivo.writelines('\n SOLUCAO : \n' )
    arquivo.writelines(str(spath)+"\n") # escreve solução em txt
    arquivo.close()
    return True 
            
def caminho(x,y,matrix,spath,tam,m,f1,f2):
    m=m+1 
    if x==f1-1:
        if y==f2-1:
            spath[x][y] = 1*m    #se é caminho possivel marca na solução
            return True
          
            #checagem do labirinto
    if passo(x,y,matrix,tam) == True: 
        # salva na matriz solução 
        spath[x][y] = 1*m
        
          
        # Movimento em x
        if caminho(x+1,y,matrix, spath,tam,m,f1,f2) == True: 
            return True
              
            # Move em y
        if caminho(x,y+1,matrix, spath,tam,m,f1,f2) == True: 
            return True
          
        # Retira passos que não estão na solução. MARCA com -1 para mostrar por onde
        #o algoritmo tentou chegar a solução.
        spath[x][y] = -1
        return False
    
    
x=input("Digitar o tamanho do labirinto") # inicia tamanho matriz         
arquivo = open('labirinto.txt', 'a')
matrix = matrix(int(x))  ## inicia matriz de tamanho x
for i in range(int(x)):
    for j in range(int(x)):
        k=random.randint(0,6)  # cria matriz com valores aleatórios
        if(k!=0):
            k=1
        matrix.setIndice(i,j,k)
arquivo.writelines("\n MATRIZ GERADA \n")
arquivo.writelines(str(matrix.matriz))  # escreve matriz em txt
arquivo.writelines("\n")
print(matrix.matriz)
encontrarSolucao(matrix.matriz,int(matrix.k)) # inicia backtracking na matriz
arquivo.close()
        
    