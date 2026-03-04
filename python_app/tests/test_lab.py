
# TODO: Escribe pruebas unitarias para es_palindromo y suma.
# Sugerencias:
# - "radar" -> True, "anita lava la tina" -> True, "python" -> False, "" -> True, "Radar" -> True
# - suma(2,3) -> 5; suma(0,5) -> 5; suma(-2,3) -> 1

from palindromo import es_palindromo
from utils import suma


def test_ejemplo_siembra():
    assert True

def test_es_palindromo_radar():
    assert es_palindromo("radar") == True

def test_es_palindromo_anita_lava_la_tina():
    assert es_palindromo("anita lava la tina") == True

def test_es_palindromo_python():
    assert es_palindromo("python") == False

def test_es_palindromo_vacio():
    assert es_palindromo("") == True

def test_es_palindromo_Radar():
    assert es_palindromo("Radar") == True

def test_suma_numeros_aleatorios():
    assert suma(2, 3) == 5

def test_suma_cero_y_numero():
    assert suma(0, 5) == 5

def test_suma_numeros_negativos():
    assert suma(-2, 3) == 1