# -*- coding: utf-8 -*-
import sys

def leGrafo():

    n = int(input("\nDigite n (numero de vertices do grafo): ")) 

    if n > 0:

      grafo = []
      leituraInterrompida = False

      if n > 1:
        print("\nAgora voce ira entrar com as arestas ij do grafo (onde i>j).\nPara isso, preeencha a matriz de adjacencia dele.\n")
        print("Para esse exercicio, assumiremos que os vertices estao rotulados de 1 a n.\nDigite 1, se houver aresta entre os vertices e 0, caso nao haja.\n")

      for i in range(n):
          grafo.append([0])
          
          if not leituraInterrompida:
              for j in range(n - i - 1):                                      
                  elemento = input("insira o elemento linha " + str(i + 1 ) + " coluna " + str(j + i + 2 ) + ": ")
                  if elemento == '0' or elemento == '1':
                      grafo[i].append(elemento)
                  else:
                      print("\n'" + elemento + "' nao e uma entrada valida.\n")
                      print("Essa matriz e composta apenas por 0's e 1's. Tente novamente.\n")
                      leituraInterrompida = True
                      break
          else:
              break
                
      if leituraInterrompida:
          leGrafo()
          
      else:       
          for i in range(n):
              for j in range (n):
                  if len(grafo[i]) < n:
                      grafo[i].insert(j, grafo[j][i])

          nomeGrafo = input("De um nome para o seu grafo: ")
          print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

          try:
              grafosArmazenados = abreArquivo()
              grafosArmazenados[nomeGrafo] = grafo

          except:
              grafosArmazenados = {nomeGrafo:grafo}

          finally:
              armazenaGrafo(grafosArmazenados)
              imprimeMatrizAdj(grafo)


def abreArquivo():

        with open("grafosArmazenados.txt", "r") as arquivo:
            grafosArmazenados = arquivo.read()
            grafosArmazenados = eval(grafosArmazenados)

        return grafosArmazenados


def armazenaGrafo(grafosArmazenados):

    with open("grafosArmazenados.txt", "w") as arquivo:
        arquivo.write(str(grafosArmazenados))


def imprimeMatrizAdj(grafo):

    m = 0
    for linha in grafo:
        for elemento in linha:
            print(str(elemento) + " ", end="")
            if elemento == '1':
              m += 1
        print("\n")

    m = int(m / 2)
    print("m = |E| = " + str(m) + "\n")


def carregaGrafo():

    try:
        
        grafosArmazenados = abreArquivo()

        print("\n\nGrafos disponiveis: ")

        for grafo in grafosArmazenados:
            print(grafo)

        grafo = input("\nQue grafo voce quer carregar? ")

        if grafo in grafosArmazenados:
         print("\n\nMatriz de Adjacencia do grafo " + grafo + ':\n')
         imprimeMatrizAdj(grafosArmazenados[grafo])
         main()

        else:
          print("\nNao existe um grafo armazenado com este nome. Tente novamente.")
          carregaGrafo()

    except:
        print("\nAinda nao existe nenhum grafo armazenado.\nEscolha b para ler um.\n")
    
def main():

    escolha = input("Escolha uma das opcoes:\na - Ler um grafo\nb - Carregar um grafo\nc - Produzir um grafo de uma classe especial\nd - Sair\n")

    if escolha == 'a':
        leGrafo()

    elif escolha == 'b':
        carregaGrafo()

    elif escolha == 'c':
        Grafos()

    elif escolha == 'd':
        sys.exit()             

    else:
        print("\n'" + escolha + "' nao e uma opcao valida. Tente de novo.\n")
        main()

main()



class Grafos():
  def __init__(self):
    self.classes=["completo","bipartido","caminho","ciclo","roda","estrela","n_cubo"]
    self.opcao=self.selecionaClasseGrafo()-1
    self.grafo=self.criaClasse()
    self.armazenaGrafo()
  def selecionaClasseGrafo(self):
    opcao=input('''selecione uma classe de grafo para ser criada
    1-Grafo Completo
    2-Grafo Bipartido
    3-Grafo Caminho
    4-Grafo Ciclo
    5-Grafo Roda
    6-Grafo Estrela
    7-Grafo n-Cubo
    opcao:''')
    return int(opcao)
  def criaClasse(self):
    classe="self."+self.classes[self.opcao]+"()"
    return eval(classe)
  def armazenaGrafo(self):
    os.chdir("Classe de grafos__/")
    grafo=f"{self.classes[self.opcao]}$n{len(self.grafo)}$.txt"
    incluiGrafo(self.grafo,grafo)
    imprimeGrafo(self.grafo)
    os.chdir("../")
  def completo(self):
    tamanho=int(input("digite o tamanho do grafo:"))
    grafo=[]
    while tamanho < 2:
      tamanho=int(input("tamanho do grafo entre 2 e n:"))
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        grafo[i].append(1)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def bipartido(self):
    grafo=[]
    x=int(input("informe o valor da primeira particao:"))
    y=int(input("informe o valor da segunda particao:"))
    tamanho=x+y
    while tamanho < 2:
      x=int(input("tamanho do grafo entre 2 e n:"))
      y=int(input("tamanho do grafo entre 2 e n:"))
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        if (i<x and j>=x-i-1):
          grafo[i].append(1)
        else:
          grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def caminho(self):
    tamanho=int(input("digite o tamanho do grafo:"))
    grafo=[]
    while tamanho < 2:
      tamanho=int(input("tamanho do grafo entre 2 e n:"))
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        if (j==0):
          grafo[i].append(1)
        else:
          grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def ciclo(self):
    tamanho=int(input("digite o tamanho do grafo:"))
    grafo=[]
    while tamanho < 4:
      tamanho=int(input("tamanho do grafo entre 3 e n:"))
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        if (j==0 or (i==0 and j==tamanho-2)):
          grafo[i].append(1)
      else:
        grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def roda(self):
    tamanho=int(input("digite o tamanho do grafo:"))+1
    grafo=[]
    while tamanho < 4:
      tamanho=int(input("tamanho do grafo entre 3 e n:"))+1
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        if (j==0 or j==tamanho-i-2):
          grafo[i].append(1)
        else:
          grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def estrela(self):
    tamanho=int(input("digite o tamanho do grafo:"))+1
    grafo=[]
    while tamanho < 4:
      tamanho=int(input("tamanho do grafo entre 3 e n:"))+1
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        if j==(tamanho-i-2):
          grafo[i].append(1)
        else:
          grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    return grafo
  def n_cubo(self):
    tamanho=2**int(input("digite o tamanho do grafo:"))
    grafo=[]
    while tamanho < 0:
      tamanho=2**int(input("tamanho do grafo entre 0 e n:"))
    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho-i-1):
        x=str(abs(int(bin(i)[2:])-int(bin((j+i+1))[2:])))
        if (x.count("1") ==1 and set(x).issubset({"1","0"})):
          grafo[i].append(1)
        else:
          grafo[i].append(0)
    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i])<tamanho:
          grafo[i].insert(j,grafo[j][i])
    for i in range(len(grafo)):
      print(" "+str(bin(i)[2:]),end="")
    print("\n")
    for linha in grafo:
      print(str(bin(grafo.index(linha))[2:])+" ",end="")
      for item in linha:
        print(str(item)+" ",end=" ")
      print("\n")
    return grafo