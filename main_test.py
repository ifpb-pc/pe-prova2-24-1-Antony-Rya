import pytest
from main import q1a, q1b, q2, q3, q4

#########################
# Teste Q1a
@pytest.mark.parametrize("entrada, esperado", [
    ( [1,2,3,1], True),
])
def test_q1a(entrada, esperado):
    resultado = q1a(entrada)
    assert resultado == esperado

#########################
# Teste Q1b
@pytest.mark.parametrize("entrada, esperado", [
    ( [1,2,3,1], True),
])
def test_q1b(entrada, esperado):
    resultado = q1b(entrada)
    assert resultado == esperado

#########################
# Teste Q2
@pytest.mark.parametrize("entrada1,entrada2, esperado", [
    ( "anagram", "nagaram", True),
    ("rat", "car", False),
    ("aabb", "babaa", False),
])
def test_q2(entrada1, entrada2, esperado):
    resultado = q2(entrada1, entrada2)
    assert resultado == esperado


def test_q3():
    esperado = 1213
    assert esperado == q3()


# @pytest.mark.parametrize("entrada, esperado_pares, esperado_impares", [
#     ([2, 4, 6, 8, 10, 12, 14, 0], [12, 14, 6, 8, 10], []),
#     ([1, 3, 5, 7, 9, 11, 0], [], [11, 3, 5, 7, 9]),
#     ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 0], [22, 14, 16, 18, 20], []),
#     ([2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0], [12, 4, 6, 8, 10], [11, 3, 5, 7, 9])
# ])
# # def test_q4(entrada, esperado_pares, esperado_impares):
# #     resultado_pares, resultado_impares = q4(entrada)
# #     assert resultado_pares == esperado_pares
# #     assert resultado_impares == esperado_impares