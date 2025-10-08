from src.calculadora import soma, subtracao, multiplicacao

def test_soma():
  assert soma(2, 3) == 5

def test_subtracao():
  assert subtracao(5, 2) == 3

def test_multiplicacao():
  assert multiplicacao(5, 2) == 10