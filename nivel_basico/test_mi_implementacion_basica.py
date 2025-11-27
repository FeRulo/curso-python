import unittest
import math
from MiImplementacionBasica import MiImplementacionBasica


class TestMiImplementacionBasica(unittest.TestCase):
    """
    Suite de tests unitarios para MiImplementacionBasica
    Incluye casos normales, casos edge y casos límite para cada función
    """
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.impl = MiImplementacionBasica()
    
    # ========== TESTS OPERACIONES MATEMÁTICAS SIMPLES ==========
    
    def test_sumar_dos_numeros(self):
        """Test para suma de dos números"""
        # Casos normales
        self.assertEqual(self.impl.sumar_dos_numeros(5, 3), 8)
        self.assertEqual(self.impl.sumar_dos_numeros(10, 20), 30)
        
        # Casos edge
        self.assertEqual(self.impl.sumar_dos_numeros(0, 0), 0)
        self.assertEqual(self.impl.sumar_dos_numeros(-5, 5), 0)
        self.assertEqual(self.impl.sumar_dos_numeros(-10, -5), -15)
        
        # Números grandes
        self.assertEqual(self.impl.sumar_dos_numeros(999999, 1), 1000000)
        
        # Decimales
        self.assertAlmostEqual(self.impl.sumar_dos_numeros(1.5, 2.7), 4.2, places=1)
    
    def test_restar_dos_numeros(self):
        """Test para resta de dos números"""
        # Casos normales
        self.assertEqual(self.impl.restar_dos_numeros(10, 3), 7)
        self.assertEqual(self.impl.restar_dos_numeros(5, 2), 3)
        
        # Casos edge
        self.assertEqual(self.impl.restar_dos_numeros(0, 0), 0)
        self.assertEqual(self.impl.restar_dos_numeros(5, 5), 0)
        self.assertEqual(self.impl.restar_dos_numeros(-5, -3), -2)
        self.assertEqual(self.impl.restar_dos_numeros(3, 5), -2)
        
        # Decimales
        self.assertAlmostEqual(self.impl.restar_dos_numeros(5.7, 2.3), 3.4, places=1)
    
    def test_multiplicar_dos_numeros(self):
        """Test para multiplicación de dos números"""
        # Casos normales
        self.assertEqual(self.impl.multiplicar_dos_numeros(4, 5), 20)
        self.assertEqual(self.impl.multiplicar_dos_numeros(7, 8), 56)
        
        # Casos edge
        self.assertEqual(self.impl.multiplicar_dos_numeros(0, 100), 0)
        self.assertEqual(self.impl.multiplicar_dos_numeros(100, 0), 0)
        self.assertEqual(self.impl.multiplicar_dos_numeros(1, 50), 50)
        self.assertEqual(self.impl.multiplicar_dos_numeros(-3, 4), -12)
        self.assertEqual(self.impl.multiplicar_dos_numeros(-5, -6), 30)
        
        # Decimales
        self.assertAlmostEqual(self.impl.multiplicar_dos_numeros(2.5, 4), 10.0, places=1)
    
    def test_dividir_dos_numeros(self):
        """Test para división de dos números"""
        # Casos normales
        self.assertEqual(self.impl.dividir_dos_numeros(10, 2), 5)
        self.assertEqual(self.impl.dividir_dos_numeros(15, 3), 5)
        
        # Casos edge
        self.assertEqual(self.impl.dividir_dos_numeros(0, 5), 0)
        self.assertEqual(self.impl.dividir_dos_numeros(7, 1), 7)
        self.assertEqual(self.impl.dividir_dos_numeros(-10, 2), -5)
        self.assertEqual(self.impl.dividir_dos_numeros(-12, -3), 4)
        
        # División por cero (debería manejar la excepción)
        with self.assertRaises((ZeroDivisionError, ValueError)):
            self.impl.dividir_dos_numeros(10, 0)
        
        # Decimales
        self.assertAlmostEqual(self.impl.dividir_dos_numeros(7, 2), 3.5, places=1)
    
    def test_resto_division(self):
        """Test para resto de división"""
        # Casos normales
        self.assertEqual(self.impl.resto_division(10, 3), 1)
        self.assertEqual(self.impl.resto_division(17, 5), 2)
        
        # Casos edge
        self.assertEqual(self.impl.resto_division(10, 10), 0)
        self.assertEqual(self.impl.resto_division(0, 5), 0)
        self.assertEqual(self.impl.resto_division(5, 7), 5)
        
        # División por cero
        with self.assertRaises((ZeroDivisionError, ValueError)):
            self.impl.resto_division(10, 0)
    
    def test_f(self):
        """Test para función f(x) = x²"""
        # Casos normales
        self.assertEqual(self.impl.f(3), 9)
        self.assertEqual(self.impl.f(5), 25)
        
        # Casos edge
        self.assertEqual(self.impl.f(0), 0)
        self.assertEqual(self.impl.f(1), 1)
        self.assertEqual(self.impl.f(-3), 9)
        self.assertEqual(self.impl.f(-5), 25)
        
        # Decimales
        self.assertAlmostEqual(self.impl.f(2.5), 6.25, places=2)
    
    def test_g(self):
        """Test para función g(x) = 2x"""
        # Casos normales
        self.assertEqual(self.impl.g(5), 10)
        self.assertEqual(self.impl.g(7), 14)
        
        # Casos edge
        self.assertEqual(self.impl.g(0), 0)
        self.assertEqual(self.impl.g(-3), -6)
        self.assertEqual(self.impl.g(1), 2)
        
        # Decimales
        self.assertAlmostEqual(self.impl.g(2.5), 5.0, places=1)
    
    def test_valor_absoluto(self):
        """Test para valor absoluto"""
        # Casos normales
        self.assertEqual(self.impl.valor_absoluto(5), 5)
        self.assertEqual(self.impl.valor_absoluto(-8), 8)
        
        # Casos edge
        self.assertEqual(self.impl.valor_absoluto(0), 0)
        self.assertEqual(self.impl.valor_absoluto(-0), 0)
        
        # Decimales
        self.assertAlmostEqual(self.impl.valor_absoluto(-3.7), 3.7, places=1)
        self.assertAlmostEqual(self.impl.valor_absoluto(2.5), 2.5, places=1)
    
    def test_potencia(self):
        """Test para potencia"""
        # Casos normales
        self.assertEqual(self.impl.potencia(2, 3), 8)
        self.assertEqual(self.impl.potencia(5, 2), 25)
        
        # Casos edge
        self.assertEqual(self.impl.potencia(10, 0), 1)
        self.assertEqual(self.impl.potencia(0, 5), 0)
        self.assertEqual(self.impl.potencia(1, 100), 1)
        self.assertEqual(self.impl.potencia(-2, 2), 4)
        self.assertEqual(self.impl.potencia(-2, 3), -8)
        
        # Casos especiales
        with self.assertRaises((ZeroDivisionError, ValueError)):
            self.impl.potencia(0, 0)  # Indeterminado
    
    def test_raiz_cuadrada(self):
        """Test para raíz cuadrada"""
        # Casos normales
        self.assertEqual(self.impl.raiz_cuadrada(9), 3)
        self.assertEqual(self.impl.raiz_cuadrada(16), 4)
        self.assertAlmostEqual(self.impl.raiz_cuadrada(2), 1.414, places=3)
        
        # Casos edge
        self.assertEqual(self.impl.raiz_cuadrada(0), 0)
        self.assertEqual(self.impl.raiz_cuadrada(1), 1)
        
        # Números negativos (debería manejar la excepción)
        with self.assertRaises((ValueError, TypeError)):
            self.impl.raiz_cuadrada(-4)
    
    # ========== TESTS VERIFICACIONES SIMPLES ==========
    
    def test_es_par(self):
        """Test para verificar si un número es par"""
        # Casos normales
        self.assertTrue(self.impl.es_par(4))
        self.assertTrue(self.impl.es_par(10))
        self.assertFalse(self.impl.es_par(7))
        self.assertFalse(self.impl.es_par(15))
        
        # Casos edge
        self.assertTrue(self.impl.es_par(0))
        self.assertTrue(self.impl.es_par(-4))
        self.assertFalse(self.impl.es_par(-7))
        self.assertTrue(self.impl.es_par(2))
    
    def test_es_impar(self):
        """Test para verificar si un número es impar"""
        # Casos normales
        self.assertTrue(self.impl.es_impar(5))
        self.assertTrue(self.impl.es_impar(13))
        self.assertFalse(self.impl.es_impar(8))
        self.assertFalse(self.impl.es_impar(20))
        
        # Casos edge
        self.assertFalse(self.impl.es_impar(0))
        self.assertTrue(self.impl.es_impar(-5))
        self.assertFalse(self.impl.es_impar(-8))
        self.assertTrue(self.impl.es_impar(1))
    
    def test_es_positivo(self):
        """Test para verificar si un número es positivo"""
        # Casos normales
        self.assertTrue(self.impl.es_positivo(5))
        self.assertTrue(self.impl.es_positivo(100))
        self.assertFalse(self.impl.es_positivo(-5))
        
        # Casos edge
        self.assertFalse(self.impl.es_positivo(0))  # El 0 no es positivo
        self.assertTrue(self.impl.es_positivo(0.1))
        self.assertFalse(self.impl.es_positivo(-0.1))
    
    def test_es_negativo(self):
        """Test para verificar si un número es negativo"""
        # Casos normales
        self.assertTrue(self.impl.es_negativo(-5))
        self.assertTrue(self.impl.es_negativo(-100))
        self.assertFalse(self.impl.es_negativo(5))
        
        # Casos edge
        self.assertFalse(self.impl.es_negativo(0))  # El 0 no es negativo
        self.assertTrue(self.impl.es_negativo(-0.1))
        self.assertFalse(self.impl.es_negativo(0.1))
    
    def test_es_cero(self):
        """Test para verificar si un número es cero"""
        # Casos normales
        self.assertTrue(self.impl.es_cero(0))
        self.assertFalse(self.impl.es_cero(5))
        self.assertFalse(self.impl.es_cero(-3))
        
        # Casos edge
        self.assertTrue(self.impl.es_cero(0.0))
        self.assertTrue(self.impl.es_cero(-0))
        self.assertFalse(self.impl.es_cero(0.1))
        self.assertFalse(self.impl.es_cero(-0.1))
    
    def test_signo(self):
        """Test para obtener el signo de un número"""
        # Casos normales
        self.assertEqual(self.impl.signo(5), 1)
        self.assertEqual(self.impl.signo(-8), -1)
        
        # Casos edge
        self.assertEqual(self.impl.signo(0), 0)
        self.assertEqual(self.impl.signo(0.1), 1)
        self.assertEqual(self.impl.signo(-0.1), -1)
    
    def test_es_mayor(self):
        """Test para verificar si a > b"""
        # Casos normales
        self.assertTrue(self.impl.es_mayor(10, 5))
        self.assertFalse(self.impl.es_mayor(3, 7))
        
        # Casos edge
        self.assertFalse(self.impl.es_mayor(5, 5))
        self.assertTrue(self.impl.es_mayor(0, -1))
        self.assertFalse(self.impl.es_mayor(-5, -3))
        self.assertTrue(self.impl.es_mayor(-3, -5))
    
    def test_es_menor(self):
        """Test para verificar si a < b"""
        # Casos normales
        self.assertTrue(self.impl.es_menor(3, 7))
        self.assertFalse(self.impl.es_menor(10, 5))
        
        # Casos edge
        self.assertFalse(self.impl.es_menor(5, 5))
        self.assertFalse(self.impl.es_menor(0, -1))
        self.assertTrue(self.impl.es_menor(-5, -3))
        self.assertFalse(self.impl.es_menor(-3, -5))
    
    def test_es_igual(self):
        """Test para verificar si a == b"""
        # Casos normales
        self.assertTrue(self.impl.es_igual(5, 5))
        self.assertFalse(self.impl.es_igual(3, 7))
        
        # Casos edge
        self.assertTrue(self.impl.es_igual(0, 0))
        self.assertTrue(self.impl.es_igual(-5, -5))
        self.assertFalse(self.impl.es_igual(0, -0))  # Dependiendo de la implementación
    
    def test_mayor_de_dos(self):
        """Test para obtener el mayor de dos números"""
        # Casos normales
        self.assertEqual(self.impl.mayor_de_dos(10, 5), 10)
        self.assertEqual(self.impl.mayor_de_dos(3, 7), 7)
        
        # Casos edge
        self.assertEqual(self.impl.mayor_de_dos(5, 5), 5)
        self.assertEqual(self.impl.mayor_de_dos(0, -1), 0)
        self.assertEqual(self.impl.mayor_de_dos(-3, -5), -3)
    
    def test_menor_de_dos(self):
        """Test para obtener el menor de dos números"""
        # Casos normales
        self.assertEqual(self.impl.menor_de_dos(10, 5), 5)
        self.assertEqual(self.impl.menor_de_dos(3, 7), 3)
        
        # Casos edge
        self.assertEqual(self.impl.menor_de_dos(5, 5), 5)
        self.assertEqual(self.impl.menor_de_dos(0, -1), -1)
        self.assertEqual(self.impl.menor_de_dos(-3, -5), -5)
    
    def test_mayor_de_tres(self):
        """Test para obtener el mayor de tres números"""
        # Casos normales
        self.assertEqual(self.impl.mayor_de_tres(5, 10, 3), 10)
        self.assertEqual(self.impl.mayor_de_tres(15, 8, 12), 15)
        
        # Casos edge
        self.assertEqual(self.impl.mayor_de_tres(5, 5, 5), 5)
        self.assertEqual(self.impl.mayor_de_tres(-1, -5, -3), -1)
        self.assertEqual(self.impl.mayor_de_tres(0, -1, 1), 1)
    
    def test_menor_de_tres(self):
        """Test para obtener el menor de tres números"""
        # Casos normales
        self.assertEqual(self.impl.menor_de_tres(5, 10, 3), 3)
        self.assertEqual(self.impl.menor_de_tres(15, 8, 12), 8)
        
        # Casos edge
        self.assertEqual(self.impl.menor_de_tres(5, 5, 5), 5)
        self.assertEqual(self.impl.menor_de_tres(-1, -5, -3), -5)
        self.assertEqual(self.impl.menor_de_tres(0, -1, 1), -1)
    
    # ========== TESTS OPERACIONES BÁSICAS CON TEXTO ==========
    
    def test_contar_caracteres(self):
        """Test para contar caracteres en un texto"""
        # Casos normales
        self.assertEqual(self.impl.contar_caracteres("Hola"), 4)
        self.assertEqual(self.impl.contar_caracteres("Python"), 6)
        
        # Casos edge
        self.assertEqual(self.impl.contar_caracteres(""), 0)
        self.assertEqual(self.impl.contar_caracteres(" "), 1)
        self.assertEqual(self.impl.contar_caracteres("   "), 3)
        self.assertEqual(self.impl.contar_caracteres("a"), 1)
        self.assertEqual(self.impl.contar_caracteres("¡Hola!"), 6)
    
    def test_mayusculas(self):
        """Test para convertir texto a mayúsculas"""
        # Casos normales
        self.assertEqual(self.impl.mayusculas("hola"), "HOLA")
        self.assertEqual(self.impl.mayusculas("Python"), "PYTHON")
        
        # Casos edge
        self.assertEqual(self.impl.mayusculas(""), "")
        self.assertEqual(self.impl.mayusculas("HOLA"), "HOLA")
        self.assertEqual(self.impl.mayusculas("123"), "123")
        self.assertEqual(self.impl.mayusculas("¡hola!"), "¡HOLA!")
        self.assertEqual(self.impl.mayusculas(" "), " ")
    
    def test_minusculas(self):
        """Test para convertir texto a minúsculas"""
        # Casos normales
        self.assertEqual(self.impl.minusculas("HOLA"), "hola")
        self.assertEqual(self.impl.minusculas("Python"), "python")
        
        # Casos edge
        self.assertEqual(self.impl.minusculas(""), "")
        self.assertEqual(self.impl.minusculas("hola"), "hola")
        self.assertEqual(self.impl.minusculas("123"), "123")
        self.assertEqual(self.impl.minusculas("¡HOLA!"), "¡hola!")
        self.assertEqual(self.impl.minusculas(" "), " ")
    
    def test_primera_letra(self):
        """Test para obtener la primera letra"""
        # Casos normales
        self.assertEqual(self.impl.primera_letra("Hola"), "H")
        self.assertEqual(self.impl.primera_letra("python"), "p")
        
        # Casos edge
        self.assertEqual(self.impl.primera_letra("a"), "a")
        self.assertEqual(self.impl.primera_letra(" Hola"), " ")
        self.assertEqual(self.impl.primera_letra("123"), "1")
        
        # Cadena vacía
        with self.assertRaises((IndexError, ValueError)):
            self.impl.primera_letra("")
    
    def test_ultima_letra(self):
        """Test para obtener la última letra"""
        # Casos normales
        self.assertEqual(self.impl.ultima_letra("Hola"), "a")
        self.assertEqual(self.impl.ultima_letra("python"), "n")
        
        # Casos edge
        self.assertEqual(self.impl.ultima_letra("a"), "a")
        self.assertEqual(self.impl.ultima_letra("Hola "), " ")
        self.assertEqual(self.impl.ultima_letra("123"), "3")
        
        # Cadena vacía
        with self.assertRaises((IndexError, ValueError)):
            self.impl.ultima_letra("")
    
    def test_concatenar_textos(self):
        """Test para concatenar dos textos"""
        # Casos normales
        self.assertEqual(self.impl.concatenar_textos("Hola", "Mundo"), "HolaMundo")
        self.assertEqual(self.impl.concatenar_textos("Python", "123"), "Python123")
        
        # Casos edge
        self.assertEqual(self.impl.concatenar_textos("", "Hola"), "Hola")
        self.assertEqual(self.impl.concatenar_textos("Hola", ""), "Hola")
        self.assertEqual(self.impl.concatenar_textos("", ""), "")
        self.assertEqual(self.impl.concatenar_textos("Hola ", "Mundo"), "Hola Mundo")
    
    def test_repetir_texto(self):
        """Test para repetir un texto n veces"""
        # Casos normales
        self.assertEqual(self.impl.repetir_texto("Hola", 3), "HolaHolaHola")
        self.assertEqual(self.impl.repetir_texto("A", 5), "AAAAA")
        
        # Casos edge
        self.assertEqual(self.impl.repetir_texto("Hola", 0), "")
        self.assertEqual(self.impl.repetir_texto("", 5), "")
        self.assertEqual(self.impl.repetir_texto("Hola", 1), "Hola")
        
        # Casos límite
        with self.assertRaises((ValueError, TypeError)):
            self.impl.repetir_texto("Hola", -1)
    
    # ========== TESTS CONVERSIONES SIMPLES ==========
    
    def test_celsius_a_fahrenheit(self):
        """Test para conversión Celsius a Fahrenheit"""
        # Casos normales
        self.assertAlmostEqual(self.impl.celsius_a_fahrenheit(0), 32, places=1)
        self.assertAlmostEqual(self.impl.celsius_a_fahrenheit(100), 212, places=1)
        self.assertAlmostEqual(self.impl.celsius_a_fahrenheit(25), 77, places=1)
        
        # Casos edge
        self.assertAlmostEqual(self.impl.celsius_a_fahrenheit(-40), -40, places=1)
        self.assertAlmostEqual(self.impl.celsius_a_fahrenheit(-273.15), -459.67, places=1)
    
    def test_fahrenheit_a_celsius(self):
        """Test para conversión Fahrenheit a Celsius"""
        # Casos normales
        self.assertAlmostEqual(self.impl.fahrenheit_a_celsius(32), 0, places=1)
        self.assertAlmostEqual(self.impl.fahrenheit_a_celsius(212), 100, places=1)
        self.assertAlmostEqual(self.impl.fahrenheit_a_celsius(77), 25, places=1)
        
        # Casos edge
        self.assertAlmostEqual(self.impl.fahrenheit_a_celsius(-40), -40, places=1)
    
    def test_metros_a_centimetros(self):
        """Test para conversión metros a centímetros"""
        # Casos normales
        self.assertEqual(self.impl.metros_a_centimetros(1), 100)
        self.assertEqual(self.impl.metros_a_centimetros(2.5), 250)
        
        # Casos edge
        self.assertEqual(self.impl.metros_a_centimetros(0), 0)
        self.assertEqual(self.impl.metros_a_centimetros(0.01), 1)
    
    def test_centimetros_a_metros(self):
        """Test para conversión centímetros a metros"""
        # Casos normales
        self.assertEqual(self.impl.centimetros_a_metros(100), 1)
        self.assertEqual(self.impl.centimetros_a_metros(250), 2.5)
        
        # Casos edge
        self.assertEqual(self.impl.centimetros_a_metros(0), 0)
        self.assertEqual(self.impl.centimetros_a_metros(1), 0.01)
    
    def test_minutos_a_segundos(self):
        """Test para conversión minutos a segundos"""
        # Casos normales
        self.assertEqual(self.impl.minutos_a_segundos(1), 60)
        self.assertEqual(self.impl.minutos_a_segundos(2.5), 150)
        
        # Casos edge
        self.assertEqual(self.impl.minutos_a_segundos(0), 0)
        self.assertEqual(self.impl.minutos_a_segundos(0.5), 30)
    
    def test_segundos_a_minutos(self):
        """Test para conversión segundos a minutos"""
        # Casos normales
        self.assertEqual(self.impl.segundos_a_minutos(60), 1)
        self.assertEqual(self.impl.segundos_a_minutos(150), 2.5)
        
        # Casos edge
        self.assertEqual(self.impl.segundos_a_minutos(0), 0)
        self.assertEqual(self.impl.segundos_a_minutos(30), 0.5)
    
    def test_horas_a_segundos(self):
        """Test para conversión horas a segundos"""
        # Casos normales
        self.assertEqual(self.impl.horas_a_segundos(1), 3600)
        self.assertEqual(self.impl.horas_a_segundos(2), 7200)
        
        # Casos edge
        self.assertEqual(self.impl.horas_a_segundos(0), 0)
        self.assertEqual(self.impl.horas_a_segundos(0.5), 1800)
    
    def test_segundos_a_horas(self):
        """Test para conversión segundos a horas"""
        # Casos normales
        self.assertEqual(self.impl.segundos_a_horas(3600), 1)
        self.assertEqual(self.impl.segundos_a_horas(7200), 2)
        
        # Casos edge
        self.assertEqual(self.impl.segundos_a_horas(0), 0)
        self.assertEqual(self.impl.segundos_a_horas(1800), 0.5)
    
    # ========== TESTS GEOMETRÍA BÁSICA ==========
    
    def test_area_rectangulo(self):
        """Test para área de rectángulo"""
        # Casos normales
        self.assertEqual(self.impl.area_rectangulo(5, 3), 15)
        self.assertEqual(self.impl.area_rectangulo(10, 7), 70)
        
        # Casos edge
        self.assertEqual(self.impl.area_rectangulo(0, 5), 0)
        self.assertEqual(self.impl.area_rectangulo(5, 0), 0)
        self.assertEqual(self.impl.area_rectangulo(1, 1), 1)
        
        # Valores negativos (dependiendo de la implementación)
        with self.assertRaises((ValueError, TypeError)):
            self.impl.area_rectangulo(-5, 3)
    
    def test_area_triangulo(self):
        """Test para área de triángulo"""
        # Casos normales
        self.assertEqual(self.impl.area_triangulo(6, 4), 12)
        self.assertEqual(self.impl.area_triangulo(10, 5), 25)
        
        # Casos edge
        self.assertEqual(self.impl.area_triangulo(0, 5), 0)
        self.assertEqual(self.impl.area_triangulo(5, 0), 0)
        
        # Valores negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.area_triangulo(-5, 3)
    
    def test_area_cuadrado(self):
        """Test para área de cuadrado"""
        # Casos normales
        self.assertEqual(self.impl.area_cuadrado(5), 25)
        self.assertEqual(self.impl.area_cuadrado(7), 49)
        
        # Casos edge
        self.assertEqual(self.impl.area_cuadrado(0), 0)
        self.assertEqual(self.impl.area_cuadrado(1), 1)
        
        # Valores negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.area_cuadrado(-5)
    
    def test_area_circulo(self):
        """Test para área de círculo"""
        # Casos normales
        self.assertAlmostEqual(self.impl.area_circulo(1), math.pi, places=2)
        self.assertAlmostEqual(self.impl.area_circulo(2), 4 * math.pi, places=2)
        
        # Casos edge
        self.assertEqual(self.impl.area_circulo(0), 0)
        
        # Valores negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.area_circulo(-5)
    
    def test_perimetro_rectangulo(self):
        """Test para perímetro de rectángulo"""
        # Casos normales
        self.assertEqual(self.impl.perimetro_rectangulo(5, 3), 16)
        self.assertEqual(self.impl.perimetro_rectangulo(10, 7), 34)
        
        # Casos edge
        self.assertEqual(self.impl.perimetro_rectangulo(0, 5), 10)
        self.assertEqual(self.impl.perimetro_rectangulo(5, 0), 10)
        self.assertEqual(self.impl.perimetro_rectangulo(1, 1), 4)
    
    def test_perimetro_cuadrado(self):
        """Test para perímetro de cuadrado"""
        # Casos normales
        self.assertEqual(self.impl.perimetro_cuadrado(5), 20)
        self.assertEqual(self.impl.perimetro_cuadrado(7), 28)
        
        # Casos edge
        self.assertEqual(self.impl.perimetro_cuadrado(0), 0)
        self.assertEqual(self.impl.perimetro_cuadrado(1), 4)
    
    def test_perimetro_circulo(self):
        """Test para perímetro de círculo"""
        # Casos normales
        self.assertAlmostEqual(self.impl.perimetro_circulo(1), 2 * math.pi, places=2)
        self.assertAlmostEqual(self.impl.perimetro_circulo(2), 4 * math.pi, places=2)
        
        # Casos edge
        self.assertEqual(self.impl.perimetro_circulo(0), 0)
    
    def test_volumen_cubo(self):
        """Test para volumen de cubo"""
        # Casos normales
        self.assertEqual(self.impl.volumen_cubo(3), 27)
        self.assertEqual(self.impl.volumen_cubo(5), 125)
        
        # Casos edge
        self.assertEqual(self.impl.volumen_cubo(0), 0)
        self.assertEqual(self.impl.volumen_cubo(1), 1)
        
        # Valores negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.volumen_cubo(-3)
    
    def test_volumen_cilindro(self):
        """Test para volumen de cilindro"""
        # Casos normales
        self.assertAlmostEqual(self.impl.volumen_cilindro(1, 1), math.pi, places=2)
        self.assertAlmostEqual(self.impl.volumen_cilindro(2, 3), 12 * math.pi, places=2)
        
        # Casos edge
        self.assertEqual(self.impl.volumen_cilindro(0, 5), 0)
        self.assertEqual(self.impl.volumen_cilindro(5, 0), 0)
        
        # Valores negativos
        with self.assertRaises((ValueError, TypeError)):
            self.impl.volumen_cilindro(-1, 5)


if __name__ == '__main__':
    # Ejecutar todos los tests
    unittest.main(verbosity=2)