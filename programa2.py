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
              main()


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



def leGrafoEspecial():

  tipoDeGrafo = int(input("\nQue tipo de grafo especial voce quer ler?\nSelecipne uma das opcoes abaixo.\n\n1 - completo\n2 - Bipartido Completo\n3 - Estrela\n4 - Caminho\n5 - Ciclo\n6 - Roda\n7 - Cubo\n")) 
  
  if tipoDeGrafo == 1:
    completo()

  elif tipoDeGrafo == 2:
    bipartidoCompleto()

  elif tipoDeGrafo == 3:
    estrela()

  elif tipoDeGrafo == 4:
    caminho()

  elif tipoDeGrafo == 5:
    ciclo()

  elif tipoDeGrafo == 6:
    roda()
  
  elif tipoDeGrafo == 7:
    n_cubo()

  else:
    print("\n'" + tipoDeGrafo + "' nao e uma opcao valida. Tente de novo.\n")
    leGrafoEspecial()
    

def completo():            

  tamanho = int(input("digite o tamanho do grafo (n): "))
  grafo = []

  while tamanho < 1:
    tamanho = int (input("digite o tamanho do grafo (n > 0):"))

  for i in range(tamanho):
    grafo.append([0])
    for j in range(tamanho - i -1):
      grafo[i].append('1') 

  for i in range(tamanho):
    for j in range (tamanho):
      if len(grafo[i]) < tamanho:
        grafo[i].insert(j, str(grafo[j][i]))

  nomeGrafo = "completo_" + str(tamanho)
  print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

  try:
      grafosArmazenados = abreArquivo()
      grafosArmazenados[nomeGrafo] = grafo

  except:
      grafosArmazenados = {nomeGrafo:grafo}

  finally:
      armazenaGrafo(grafosArmazenados)
      imprimeMatrizAdj(grafo)
      main()

def bipartidoCompleto():

  grafo = []
  n1 = int(input("informe o valor da primeira particao (n1): "))
  n2 = int(input("informe o valor da segunda particao (n2): "))
  tamanho = n1 + n2

  while tamanho < 2:
    n1 = int(input("informe o valor da primeira particao (n1 > 0): "))
    n2 = int(input("informe o valor da segunda particao (n2 > 0): "))
    tamanho = n1 + n2

  for i in range(tamanho):
    grafo.append([0])
    for j in range(tamanho - i - 1):
      if (i < n1 and j >= n1 - i - 1):
        grafo[i].append('1')
      else:
        grafo[i].append(0)

  for i in range(tamanho):
    for j in range (tamanho):
      if len(grafo[i]) < tamanho:
        grafo[i].insert(j, str(grafo[j][i]))

  nomeGrafo = "bipartido_completo_" + str(n1) + str(n2)
  print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

  try:
      grafosArmazenados = abreArquivo()
      grafosArmazenados[nomeGrafo] = grafo

  except:
      grafosArmazenados = {nomeGrafo:grafo}

  finally:
      armazenaGrafo(grafosArmazenados)
      imprimeMatrizAdj(grafo)
      main()
    

def estrela(): ###################### aguardando resposta do monitor 

    tamanho = int(input("digite o tamanho do grafo (n > 0): ")) + 1
    grafo = []

    while tamanho < 2:    ########## aguardando resposta do monitor 
      tamanho = int(input("tamanho do grafo entre 1 e n:")) + 1

    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho - i - 1):
        if j==(tamanho - i - 2):
          grafo[i].append('1')
        else:
          grafo[i].append(0)

    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i]) < tamanho:
          grafo[i].insert(j, str(grafo[j][i]))

    nomeGrafo = "estrela_" + str(tamanho - 1) ############# aguardando resposta do monitor 
    print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

    try:
        grafosArmazenados = abreArquivo()
        grafosArmazenados[nomeGrafo] = grafo

    except:
        grafosArmazenados = {nomeGrafo:grafo}

    finally:
        armazenaGrafo(grafosArmazenados)
        imprimeMatrizAdj(grafo)
        main()

def caminho():
    
    tamanho = int(input("digite o tamanho do grafo (n >= 1): "))
    grafo = []

    while tamanho < 1: 
      tamanho = int(input("tamanho do grafo entre 1 e n:"))

    for i in range(tamanho):
      grafo.append([0])
      for j in range(tamanho - i - 1):
        if (j == 0):
          grafo[i].append('1')
        else:
          grafo[i].append(0)

    for i in range(tamanho):
      for j in range (tamanho):
        if len(grafo[i]) < tamanho:
          grafo[i].insert(j, str(grafo[j][i]))
    
    nomeGrafo = "caminho_" + str(tamanho)
    print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

    try:
        grafosArmazenados = abreArquivo()
        grafosArmazenados[nomeGrafo] = grafo

    except:
        grafosArmazenados = {nomeGrafo:grafo}

    finally:
        armazenaGrafo(grafosArmazenados)
        imprimeMatrizAdj(grafo)
        main()

def ciclo():
    
    tamanho = int(input("digite o tamanho do grafo(n > 2): "))

    while tamanho < 3:
      tamanho = int(input("tamanho do grafo entre 3 e n: "))

    grafo =  grafo = [[0] * tamanho for _ in range(tamanho)]  
  
    for i in range(0, tamanho): 
            for j in range (1, tamanho):
                if(j == (i + 1)):
                  grafo[i][j] = '1'
                  grafo[j][i] = '1'
                    
    #primeira linha
    grafo[0][tamanho - 1] = '1'
    #ultima linha
    grafo[tamanho - 1][0] = '1'

    nomeGrafo = "ciclo_" + str(tamanho)
    print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

    try:
        grafosArmazenados = abreArquivo()
        grafosArmazenados[nomeGrafo] = grafo

    except:
        grafosArmazenados = {nomeGrafo:grafo}

    finally:
        armazenaGrafo(grafosArmazenados)
        imprimeMatrizAdj(grafo)
        main()

def roda():  ###################### aguardando resposta do monitor 
    
    tamanho = int(input("digite o tamanho do grafo(n >= 3): ")) + 1

    while tamanho < 4:
      tamanho = int(input("tamanho do grafo entre 3 e n: ")) + 1

    grafo =  grafo = [[0] * tamanho for _ in range(tamanho)]

    for i in range(tamanho): 
        for j in range (tamanho):
            if(j == (i + 1)):
              grafo[i][j] = '1'
              grafo[j][i] = '1'
            if ( j == (tamanho - 1) or i == (tamanho - 1)):
                grafo[i][j] = '1'
            if( j == (tamanho - 1) and i == (tamanho - 1)):
                grafo[i][j] = 0
                
    #elementos pendentes
    grafo[0][tamanho - 2] = '1'
    grafo[tamanho - 2][0] = '1'

    nomeGrafo = "roda_" + str(tamanho - 1) ########## aguardando resposta do monitor 
    print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

    try:
        grafosArmazenados = abreArquivo()
        grafosArmazenados[nomeGrafo] = grafo

    except:
        grafosArmazenados = {nomeGrafo:grafo}

    finally:
        armazenaGrafo(grafosArmazenados)
        imprimeMatrizAdj(grafo)
        main()

def n_cubo():

  n = int(input("digite o tamanho do grafo (n) que sera o numero de dimensoes: "))

  tamanho = 2 ** n
  grafo = []

  while tamanho < 0:
    tamanho = 2 ** int(input("tamanho do grafo entre 0 e n: "))

  for i in range(tamanho):
    grafo.append([0])
    for j in range(tamanho - i - 1):
      x = str(abs(int(bin(i)[2:]) - int(bin((j + i + 1))[2:])))
      if (x.count("1") == 1 and set(x).issubset({"1", "0"})):
        grafo[i].append('1')
      else:
        grafo[i].append(0)

  for i in range(tamanho):
    for j in range (tamanho):
      if len(grafo[i]) < tamanho:
        grafo[i].insert(j, str(grafo[j][i]))

  nomeGrafo = "cubo_" + str(n)
  print("\nMatriz de Adjacencia do grafo " + nomeGrafo + ":\n")

  try:
      grafosArmazenados = abreArquivo()
      grafosArmazenados[nomeGrafo] = grafo

  except:
      grafosArmazenados = {nomeGrafo:grafo}

  finally:
      armazenaGrafo(grafosArmazenados)
      imprimeMatrizAdj(grafo)
      main()

def main():

    escolha = input("Escolha uma das opcoes:\na - Ler um grafo\nb - Carregar um grafo\nc - Produzir um grafo de uma classe especial\nd - Sair\n")

    if escolha == 'a':
        leGrafo()

    elif escolha == 'b':
        carregaGrafo()

    elif escolha == 'c':
        leGrafoEspecial()

    elif escolha == 'd':
        sys.exit()             

    else:
        print("\n'" + escolha + "' nao e uma opcao valida. Tente de novo.\n")
        main()

main()

#######################################################################################
#######################################################################################

# comparar o meu projeto do periodo passado com o do julio e ver qual dos dois está mais parecido 
# com o algoritmo de busca em largura do luerbio ( o algoritmo está no material dele e em foto no celular ).
# Condferir também se a saída está correta.

# no video de conectividade 2023-04-21 17-54-11.mp4  em 8min talvez tem um negocio que ele fala sobre o trab

#######################################################################################
#######################################################################################