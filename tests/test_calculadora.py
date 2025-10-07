from src.calculadora import soma

def test_soma():
  assert soma(2, 3) == 5
  assert soma(-1, 0) == 0
