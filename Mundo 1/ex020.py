"""Sequência aleatória"""
import random

""" def mostrar_alunos(numero, nome):
      print(f"{numero}: {nome}") """


def alunos():
    while True:
            aluno1 = input("Digite O Nome do Primeiro Aluno: ").capitalize()
            aluno2 = input("Digite O Nome do Segundo Aluno: ").capitalize()
            aluno3 = input("Digite O Nome do Terceiro Aluno: ").capitalize()
            aluno4 = input("Digite O Nome do Quarto Aluno: ").capitalize()

            return aluno1, aluno2, aluno3, aluno4

def sequencia(al1, al2, al3, al4):
      alunos = [al1, al2, al3, al4]
      random.shuffle(alunos)
      return alunos

def entrada():
      print("==========Seja-Vindo ao Embaralhador de Alunos==========\n")

def principal():
      while True:
            entrada()
            al1, al2, al3, al4 = alunos()
            ordem = sequencia(al1, al2, al3, al4)
            """ mostrar_alunos(1, al1)
            mostrar_alunos(2, al2)
            mostrar_alunos(3, al3)
            mostrar_alunos(4, al4) """

            print(f"\nA Ordem que Será ralizada as Apresentação Dos Trabalhos Será: {ordem}")
            cont = str(input("Deseja Continuar com EDA ? S/N")).upper()

            if cont != "S":
                  break
   
principal()