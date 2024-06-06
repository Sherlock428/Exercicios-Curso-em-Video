"""Sorteio de Alunos"""
import random

def adicionar_alunos():
     while True:
             aluno1 = input("Digite O Nome do Primeiro Aluno: ")
             aluno2 = input("Digite O Nome do Segundo Aluno: ")
             aluno3 = input("Digite O Nome do Terceiro Aluno: ")
             aluno4 = input("Digite O Nome do Quarto Aluno: ")

             return aluno1, aluno2, aluno3, aluno4

def sorteio(al1, al2, al3, al4):
       sort = random.choice([al1, al2, al3, al4])
       return sort

def entrada():
      print("==========Bem-Vindo Ao Sistema de Sorteios==========\n")

def principal():
      while True:
            entrada()
            al1, al2, al3, al4 = adicionar_alunos()
            sort = sorteio(al1, al2, al3, al4)
            print(f"\nO Aluno Sorteado Que Apagará O Quadro É: {sort}\n")

            cont = input("Deseja Continuar com Sorteio S/N: ").upper()
            if cont != "S":
                  break



principal()

# #Melhorar esse código tentar usar if e else para criar um sistema que identifique o aluno




