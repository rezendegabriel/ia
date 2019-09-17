# -*- coding: utf-8 -*-

"""
Trabalho 1 - Problema do Labirinto
Inteligência Artificial - DCC014

Discentes: Gabriel Rezende
           Pedro Henrique Eveling
           
Prof.(a) Luciana Campos
"""

class No:
    
    def __init__(self, indice):
        self.indice = indice
        
    def getIndice(self):
        return self.indice
        
class Aresta:
    
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
        
    def getOrigem(self):
        return self.origem
    
    def getDestino(self):
        return self.destino

class Grafo:
    
    def __init__(self):
        self.nos = []
        self.arestas = []
        
    def criarNo(self, indice):
        auxIndice = self.buscarNo(indice)
        
        if auxIndice is None:
            self.nos.append(No(indice))
        
    def buscarNo(self, indice):
        for i in self.nos:
            if indice == i.getIndice():
                return i
            
        return None
        
    def criarAresta(self, origem, destino):
        auxOrigem = self.buscarNo(origem)
        auxDestino = self.buscarNo(destino)
        
        if (auxOrigem is not None) and (auxDestino is not None):
            self.arestas.append(Aresta(auxOrigem, auxDestino))
        else:
            print("Nó(s) inválido(s)!")
            
    def buscarAresta(self, origem, destino):
        for i in self.arestas:
            auxOrigem = i.getOrigem()
            auxDestino = i.getDestino()
            
            if auxOrigem.getIndice() == origem.getIndice() and auxDestino.getIndice() == destino.getIndice():
                return i
            
        return None
    
    def imprimirGrafo(self):
        for i in range(len(self.arestas)):
            print(self.arestas[i].getOrigem().getIndice() + " " + self.arestas[i].getDestino().getIndice())
   
grafo = Grafo()         
arquivo = open('grafo.txt', 'r')

for linha in arquivo:
    grafo.criarNo(str(linha[0]))
    grafo.criarNo(str(linha[2]))
    grafo.criarAresta(str(linha[0]), str(linha[2]))
    
grafo.imprimirGrafo()