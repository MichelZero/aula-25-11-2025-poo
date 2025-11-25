# autor: Michel
# 25/11/2025

from ex01 import Pessoa

class Aluno(Pessoa):
  def __init__(self, nome, idade):
    super().__init__(nome)
    self.idade = idade