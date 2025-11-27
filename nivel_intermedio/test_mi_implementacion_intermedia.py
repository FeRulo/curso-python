import unittest
import math
from MiImplementacionIntermedia import MiImplementacionIntermedia


class TestMiImplementacionIntermedia(unittest.TestCase):
    """
    Suite de tests unitarios para MiImplementacionIntermedia
    Incluye casos normales, casos edge y casos límite para cada función intermedia
    """
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.impl = MiImplementacionIntermedia()
    
    # ========== TESTS MANIPULACIÓN DE DÍGITOS ==========
    
    def test_contar_digitos(self):
        """Test para contar dígitos de un número"""
        # Casos normales
        self.assertEqual(self.impl.contar_digitos(123), 3)
        self.assertEqual(self.impl.contar_digitos(5678), 4)
        
        # Casos edge
        self.assertEqual(self.impl.contar_digitos(0), 1)
        self.assertEqual(self.impl.contar_digitos(7), 1)
        self.assertEqual(self.impl.contar_digitos(-123), 3)
        self.assertEqual(self.impl.contar_digitos(-7), 1)
        
        # Números grandes
        self.assertEqual(self.impl.contar_digitos(1000000), 7)
        self.assertEqual(self.impl.contar_digitos(-999999), 6)
    
    def test_suma_digitos(self):
        """Test para sumar los dígitos de un número"""
        # Casos normales
        self.assertEqual(self.impl.suma_digitos(123), 6)  # 1+2+3
        self.assertEqual(self.impl.suma_digitos(456), 15)  # 4+5+6
        
        # Casos edge
        self.assertEqual(self.impl.suma_digitos(0), 0)
        self.assertEqual(self.impl.suma_digitos(7), 7)
        self.assertEqual(self.impl.suma_digitos(-123), 6)
        
        # Números con ceros
        self.assertEqual(self.impl.suma_digitos(105), 6)  # 1+0+5
        self.assertEqual(self.impl.suma_digitos(1000), 1)  # 1+0+0+0
    
    def test_invertir_numero(self):
        """Test para invertir un número"""
        # Casos normales
        self.assertEqual(self.impl.invertir_numero(123), 321)
        self.assertEqual(self.impl.invertir_numero(456), 654)
        
        # Casos edge
        self.assertEqual(self.impl.invertir_numero(0), 0)
        self.assertEqual(self.impl.invertir_numero(7), 7)
        self.assertEqual(self.impl.invertir_numero(-123), -321)
        
        # Números con ceros finales
        self.assertEqual(self.impl.invertir_numero(120), 21)
        self.assertEqual(self.impl.invertir_numero(1000), 1)
    
    def test_es_palindromo_numero(self):
        """Test para verificar si un número es palíndromo"""
        # Casos normales
        self.assertTrue(self.impl.es_palindromo_numero(121))
        self.assertTrue(self.impl.es_palindromo_numero(1331))
        self.assertFalse(self.impl.es_palindromo_numero(123))
        
        # Casos edge
        self.assertTrue(self.impl.es_palindromo_numero(0))
        self.assertTrue(self.impl.es_palindromo_numero(7))
        self.assertFalse(self.impl.es_palindromo_numero(-121))  # Números negativos no son palíndromos
        
        # Casos especiales
        self.assertTrue(self.impl.es_palindromo_numero(12321))
        self.assertFalse(self.impl.es_palindromo_numero(12345))
    
    def test_digito_en_posicion(self):
        """Test para obtener el dígito en una posición específica"""
        # Casos normales
        self.assertEqual(self.impl.digito_en_posicion(12345, 0), 5)  # Posición 0: último dígito
        self.assertEqual(self.impl.digito_en_posicion(12345, 2), 3)  # Posición 2
        self.assertEqual(self.impl.digito_en_posicion(12345, 4), 1)  # Posición 4: primer dígito
        
        # Casos edge
        self.assertEqual(self.impl.digito_en_posicion(7, 0), 7)
        self.assertEqual(self.impl.digito_en_posicion(0, 0), 0)
        
        # Posiciones inválidas
        with self.assertRaises((IndexError, ValueError)):
            self.impl.digito_en_posicion(123, 5)  # Posición mayor que el número de dígitos
        with self.assertRaises((IndexError, ValueError)):
            self.impl.digito_en_posicion(123, -1)  # Posición negativa
    
    # ========== TESTS BUCLES Y SECUENCIAS ==========
    
    def test_factorial(self):
        """Test para calcular factorial de un número"""
        # Casos normales
        self.assertEqual(self.impl.factorial(5), 120)
        self.assertEqual(self.impl.factorial(4), 24)
        self.assertEqual(self.impl.factorial(3), 6)
        
        # Casos edge
        self.assertEqual(self.impl.factorial(0), 1)
        self.assertEqual(self.impl.factorial(1), 1)
        
        # Números negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.factorial(-5)
        
        # Números grandes (opcional, dependiendo de la implementación)
        self.assertEqual(self.impl.factorial(10), 3628800)
    
    def test_fibonacci(self):
        """Test para calcular números de Fibonacci"""
        # Casos normales
        self.assertEqual(self.impl.fibonacci(0), 0)
        self.assertEqual(self.impl.fibonacci(1), 1)
        self.assertEqual(self.impl.fibonacci(5), 5)
        self.assertEqual(self.impl.fibonacci(8), 21)
        
        # Casos edge
        self.assertEqual(self.impl.fibonacci(2), 1)
        self.assertEqual(self.impl.fibonacci(10), 55)
        
        # Números negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.fibonacci(-1)
    
    def test_suma_hasta_n(self):
        """Test para sumar números del 1 hasta n"""
        # Casos normales
        self.assertEqual(self.impl.suma_hasta_n(5), 15)  # 1+2+3+4+5
        self.assertEqual(self.impl.suma_hasta_n(10), 55)  # 1+2+...+10
        
        # Casos edge
        self.assertEqual(self.impl.suma_hasta_n(1), 1)
        self.assertEqual(self.impl.suma_hasta_n(0), 0)
        
        # Números negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.suma_hasta_n(-5)
    
    def test_tabla_multiplicar(self):
        """Test para generar tabla de multiplicar"""
        # Casos normales
        tabla_5 = self.impl.tabla_multiplicar(5)
        expected_5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        self.assertEqual(tabla_5, expected_5)
        
        tabla_3 = self.impl.tabla_multiplicar(3)
        expected_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        self.assertEqual(tabla_3, expected_3)
        
        # Casos edge
        tabla_0 = self.impl.tabla_multiplicar(0)
        expected_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(tabla_0, expected_0)
        
        tabla_1 = self.impl.tabla_multiplicar(1)
        expected_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(tabla_1, expected_1)
    
    def test_es_primo(self):
        """Test para verificar si un número es primo"""
        # Números primos
        self.assertTrue(self.impl.es_primo(2))
        self.assertTrue(self.impl.es_primo(3))
        self.assertTrue(self.impl.es_primo(5))
        self.assertTrue(self.impl.es_primo(7))
        self.assertTrue(self.impl.es_primo(11))
        self.assertTrue(self.impl.es_primo(13))
        
        # Números no primos
        self.assertFalse(self.impl.es_primo(1))
        self.assertFalse(self.impl.es_primo(4))
        self.assertFalse(self.impl.es_primo(6))
        self.assertFalse(self.impl.es_primo(8))
        self.assertFalse(self.impl.es_primo(9))
        self.assertFalse(self.impl.es_primo(10))
        
        # Casos edge
        self.assertFalse(self.impl.es_primo(0))
        self.assertFalse(self.impl.es_primo(-5))
        
        # Números grandes
        self.assertTrue(self.impl.es_primo(17))
        self.assertFalse(self.impl.es_primo(15))
    
    # ========== TESTS MANIPULACIÓN DE LISTAS ==========
    
    def test_suma_lista(self):
        """Test para sumar elementos de una lista"""
        # Casos normales
        self.assertEqual(self.impl.suma_lista([1, 2, 3, 4, 5]), 15)
        self.assertEqual(self.impl.suma_lista([10, 20, 30]), 60)
        
        # Casos edge
        self.assertEqual(self.impl.suma_lista([]), 0)
        self.assertEqual(self.impl.suma_lista([5]), 5)
        self.assertEqual(self.impl.suma_lista([-1, 1]), 0)
        
        # Números negativos y decimales
        self.assertEqual(self.impl.suma_lista([-5, -10, -15]), -30)
        self.assertAlmostEqual(self.impl.suma_lista([1.5, 2.5, 3.0]), 7.0, places=1)
    
    def test_promedio_lista(self):
        """Test para calcular promedio de una lista"""
        # Casos normales
        self.assertEqual(self.impl.promedio_lista([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(self.impl.promedio_lista([10, 20, 30]), 20.0)
        
        # Casos edge
        self.assertEqual(self.impl.promedio_lista([5]), 5.0)
        self.assertEqual(self.impl.promedio_lista([-2, 2]), 0.0)
        
        # Lista vacía
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.impl.promedio_lista([])
        
        # Decimales
        self.assertAlmostEqual(self.impl.promedio_lista([1.5, 2.5]), 2.0, places=1)
    
    def test_maximo_lista(self):
        """Test para encontrar el máximo de una lista"""
        # Casos normales
        self.assertEqual(self.impl.maximo_lista([1, 5, 3, 9, 2]), 9)
        self.assertEqual(self.impl.maximo_lista([10, 20, 5, 15]), 20)
        
        # Casos edge
        self.assertEqual(self.impl.maximo_lista([7]), 7)
        self.assertEqual(self.impl.maximo_lista([-5, -2, -10]), -2)
        
        # Lista vacía
        with self.assertRaises((ValueError, IndexError)):
            self.impl.maximo_lista([])
        
        # Con duplicados
        self.assertEqual(self.impl.maximo_lista([5, 5, 5]), 5)
    
    def test_minimo_lista(self):
        """Test para encontrar el mínimo de una lista"""
        # Casos normales
        self.assertEqual(self.impl.minimo_lista([1, 5, 3, 9, 2]), 1)
        self.assertEqual(self.impl.minimo_lista([10, 20, 5, 15]), 5)
        
        # Casos edge
        self.assertEqual(self.impl.minimo_lista([7]), 7)
        self.assertEqual(self.impl.minimo_lista([-5, -2, -10]), -10)
        
        # Lista vacía
        with self.assertRaises((ValueError, IndexError)):
            self.impl.minimo_lista([])
        
        # Con duplicados
        self.assertEqual(self.impl.minimo_lista([5, 5, 5]), 5)
    
    def test_contar_elemento(self):
        """Test para contar ocurrencias de un elemento en una lista"""
        # Casos normales
        self.assertEqual(self.impl.contar_elemento([1, 2, 3, 2, 4, 2], 2), 3)
        self.assertEqual(self.impl.contar_elemento([5, 5, 5, 5], 5), 4)
        
        # Casos edge
        self.assertEqual(self.impl.contar_elemento([1, 2, 3], 4), 0)
        self.assertEqual(self.impl.contar_elemento([], 5), 0)
        self.assertEqual(self.impl.contar_elemento([7], 7), 1)
        
        # Con strings
        self.assertEqual(self.impl.contar_elemento(['a', 'b', 'a', 'c'], 'a'), 2)
    
    def test_invertir_lista(self):
        """Test para invertir una lista"""
        # Casos normales
        self.assertEqual(self.impl.invertir_lista([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(self.impl.invertir_lista(['a', 'b', 'c']), ['c', 'b', 'a'])
        
        # Casos edge
        self.assertEqual(self.impl.invertir_lista([]), [])
        self.assertEqual(self.impl.invertir_lista([7]), [7])
        self.assertEqual(self.impl.invertir_lista([1, 2]), [2, 1])
        
        # Lista con elementos duplicados
        self.assertEqual(self.impl.invertir_lista([1, 1, 2, 2]), [2, 2, 1, 1])
    
    def test_filtrar_pares(self):
        """Test para filtrar números pares de una lista"""
        # Casos normales
        self.assertEqual(self.impl.filtrar_pares([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(self.impl.filtrar_pares([1, 3, 5, 7]), [])
        
        # Casos edge
        self.assertEqual(self.impl.filtrar_pares([]), [])
        self.assertEqual(self.impl.filtrar_pares([2]), [2])
        self.assertEqual(self.impl.filtrar_pares([0, 2, 4]), [0, 2, 4])
        
        # Números negativos
        self.assertEqual(self.impl.filtrar_pares([-4, -3, -2, -1, 0, 1, 2]), [-4, -2, 0, 2])
    
    def test_filtrar_impares(self):
        """Test para filtrar números impares de una lista"""
        # Casos normales
        self.assertEqual(self.impl.filtrar_impares([1, 2, 3, 4, 5, 6]), [1, 3, 5])
        self.assertEqual(self.impl.filtrar_impares([2, 4, 6, 8]), [])
        
        # Casos edge
        self.assertEqual(self.impl.filtrar_impares([]), [])
        self.assertEqual(self.impl.filtrar_impares([3]), [3])
        self.assertEqual(self.impl.filtrar_impares([1, 3, 5]), [1, 3, 5])
        
        # Números negativos
        self.assertEqual(self.impl.filtrar_impares([-5, -4, -3, -2, -1, 0, 1]), [-5, -3, -1, 1])
    
    # ========== TESTS MANIPULACIÓN DE STRINGS AVANZADA ==========
    
    def test_es_palindromo_texto(self):
        """Test para verificar si un texto es palíndromo"""
        # Casos normales
        self.assertTrue(self.impl.es_palindromo_texto("ana"))
        self.assertTrue(self.impl.es_palindromo_texto("oso"))
        self.assertFalse(self.impl.es_palindromo_texto("casa"))
        
        # Casos con mayúsculas y minúsculas
        self.assertTrue(self.impl.es_palindromo_texto("Ana"))
        self.assertTrue(self.impl.es_palindromo_texto("OSO"))
        
        # Casos edge
        self.assertTrue(self.impl.es_palindromo_texto("a"))
        self.assertTrue(self.impl.es_palindromo_texto(""))
        
        # Frases (dependiendo de la implementación, puede ignorar espacios)
        # self.assertTrue(self.impl.es_palindromo_texto("a man a plan a canal panama"))
    
    def test_contar_vocales(self):
        """Test para contar vocales en un texto"""
        # Casos normales
        self.assertEqual(self.impl.contar_vocales("hola"), 2)  # o, a
        self.assertEqual(self.impl.contar_vocales("murcielago"), 5)  # u, i, e, a, o
        
        # Casos edge
        self.assertEqual(self.impl.contar_vocales(""), 0)
        self.assertEqual(self.impl.contar_vocales("bcdfg"), 0)
        self.assertEqual(self.impl.contar_vocales("aeiou"), 5)
        
        # Con mayúsculas
        self.assertEqual(self.impl.contar_vocales("HOLA"), 2)
        self.assertEqual(self.impl.contar_vocales("AeIoU"), 5)
        
        # Con espacios y números
        self.assertEqual(self.impl.contar_vocales("hola mundo"), 4)
        self.assertEqual(self.impl.contar_vocales("casa123"), 2)
    
    def test_contar_consonantes(self):
        """Test para contar consonantes en un texto"""
        # Casos normales
        self.assertEqual(self.impl.contar_consonantes("hola"), 2)  # h, l
        self.assertEqual(self.impl.contar_consonantes("python"), 4)  # p, t, h, n
        
        # Casos edge
        self.assertEqual(self.impl.contar_consonantes(""), 0)
        self.assertEqual(self.impl.contar_consonantes("aeiou"), 0)
        self.assertEqual(self.impl.contar_consonantes("bcdfg"), 5)
        
        # Con mayúsculas
        self.assertEqual(self.impl.contar_consonantes("HOLA"), 2)
        
        # Con espacios y números
        self.assertEqual(self.impl.contar_consonantes("hola mundo"), 6)
        self.assertEqual(self.impl.contar_consonantes("casa123"), 2)
    
    def test_eliminar_espacios(self):
        """Test para eliminar espacios de un texto"""
        # Casos normales
        self.assertEqual(self.impl.eliminar_espacios("hola mundo"), "holamundo")
        self.assertEqual(self.impl.eliminar_espacios("  python  es  genial  "), "pythonensgenial")
        
        # Casos edge
        self.assertEqual(self.impl.eliminar_espacios(""), "")
        self.assertEqual(self.impl.eliminar_espacios("python"), "python")
        self.assertEqual(self.impl.eliminar_espacios("   "), "")
        
        # Solo espacios al inicio/final
        self.assertEqual(self.impl.eliminar_espacios(" hola "), "hola")
    
    def test_reemplazar_caracter(self):
        """Test para reemplazar un carácter por otro en un texto"""
        # Casos normales
        self.assertEqual(self.impl.reemplazar_caracter("hola", "o", "e"), "hela")
        self.assertEqual(self.impl.reemplazar_caracter("python", "p", "j"), "jython")
        
        # Casos edge
        self.assertEqual(self.impl.reemplazar_caracter("", "a", "b"), "")
        self.assertEqual(self.impl.reemplazar_caracter("hola", "x", "y"), "hola")
        self.assertEqual(self.impl.reemplazar_caracter("aaaa", "a", "b"), "bbbb")
        
        # Mayúsculas y minúsculas
        self.assertEqual(self.impl.reemplazar_caracter("Hola", "H", "h"), "hola")
        
        # Reemplazar con espacios
        self.assertEqual(self.impl.reemplazar_caracter("hola", "o", " "), "h la")
    
    # ========== TESTS CÁLCULOS MATEMÁTICOS AVANZADOS ==========
    
    def test_mcd(self):
        """Test para calcular máximo común divisor"""
        # Casos normales
        self.assertEqual(self.impl.mcd(12, 18), 6)
        self.assertEqual(self.impl.mcd(15, 25), 5)
        self.assertEqual(self.impl.mcd(17, 19), 1)  # Números primos
        
        # Casos edge
        self.assertEqual(self.impl.mcd(0, 5), 5)
        self.assertEqual(self.impl.mcd(5, 0), 5)
        self.assertEqual(self.impl.mcd(7, 7), 7)
        
        # Números negativos
        self.assertEqual(self.impl.mcd(-12, 18), 6)
        self.assertEqual(self.impl.mcd(12, -18), 6)
        
        # Casos especiales
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.impl.mcd(0, 0)
    
    def test_mcm(self):
        """Test para calcular mínimo común múltiplo"""
        # Casos normales
        self.assertEqual(self.impl.mcm(4, 6), 12)
        self.assertEqual(self.impl.mcm(15, 20), 60)
        self.assertEqual(self.impl.mcm(7, 11), 77)  # Números primos
        
        # Casos edge
        self.assertEqual(self.impl.mcm(1, 5), 5)
        self.assertEqual(self.impl.mcm(5, 5), 5)
        
        # Con ceros
        self.assertEqual(self.impl.mcm(0, 5), 0)
        self.assertEqual(self.impl.mcm(5, 0), 0)
        
        # Números negativos (dependiendo de la implementación)
        self.assertEqual(self.impl.mcm(-4, 6), 12)
    
    def test_potencia_entera(self):
        """Test para calcular potencia con exponente entero"""
        # Casos normales
        self.assertEqual(self.impl.potencia_entera(2, 3), 8)
        self.assertEqual(self.impl.potencia_entera(5, 2), 25)
        self.assertEqual(self.impl.potencia_entera(3, 4), 81)
        
        # Casos edge
        self.assertEqual(self.impl.potencia_entera(5, 0), 1)
        self.assertEqual(self.impl.potencia_entera(1, 100), 1)
        self.assertEqual(self.impl.potencia_entera(0, 5), 0)
        
        # Exponentes negativos
        self.assertAlmostEqual(self.impl.potencia_entera(2, -3), 0.125, places=3)
        self.assertAlmostEqual(self.impl.potencia_entera(4, -2), 0.0625, places=4)
        
        # Casos especiales
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.impl.potencia_entera(0, 0)
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.impl.potencia_entera(0, -1)
    
    def test_raiz_n(self):
        """Test para calcular raíz n-ésima"""
        # Casos normales
        self.assertAlmostEqual(self.impl.raiz_n(8, 3), 2.0, places=1)  # Raíz cúbica de 8
        self.assertAlmostEqual(self.impl.raiz_n(16, 4), 2.0, places=1)  # Raíz cuarta de 16
        self.assertAlmostEqual(self.impl.raiz_n(9, 2), 3.0, places=1)  # Raíz cuadrada de 9
        
        # Casos edge
        self.assertEqual(self.impl.raiz_n(1, 5), 1.0)
        self.assertEqual(self.impl.raiz_n(0, 3), 0.0)
        
        # Índices especiales
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.impl.raiz_n(8, 0)  # División por cero
        
        # Números negativos (dependiendo de la implementación)
        # self.assertAlmostEqual(self.impl.raiz_n(-8, 3), -2.0, places=1)


if __name__ == '__main__':
    # Ejecutar todos los tests
    unittest.main(verbosity=2)