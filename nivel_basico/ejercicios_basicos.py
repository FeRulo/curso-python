from abc import ABC, abstractmethod

class EjerciciosBasicos(ABC):
    """
    NIVEL 1: BÁSICO - Operaciones simples y conceptos fundamentales
    50 ejercicios para principiantes en programación
    """
    
    # Operaciones matemáticas simples
    
    @abstractmethod
    def sumar_dos_numeros(self, a, b):
        """Suma dos números"""
        pass
    
    @abstractmethod
    def restar_dos_numeros(self, a, b):
        """Resta dos números"""
        pass
    
    @abstractmethod
    def multiplicar_dos_numeros(self, a, b):
        """Multiplica dos números"""
        pass
    
    @abstractmethod
    def dividir_dos_numeros(self, a, b):
        """Divide dos números"""
        pass
    
    @abstractmethod
    def resto_division(self, a, b):
        """Calcula el resto de una división"""
        pass
    
    @abstractmethod
    def f(self, x):
        """Función matemática f(x) = x²"""
        pass
    
    @abstractmethod
    def g(self, x):
        """Función matemática g(x) = 2x"""
        pass
    
    @abstractmethod
    def valor_absoluto(self, numero):
        """Calcula el valor absoluto de un número"""
        pass
    
    @abstractmethod
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        pass
    
    @abstractmethod
    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        pass
    
    # Verificaciones simples
    
    @abstractmethod
    def es_par(self, numero):
        """Verifica si un número es par"""
        pass
    
    @abstractmethod
    def es_impar(self, numero):
        """Verifica si un número es impar"""
        pass
    
    @abstractmethod
    def es_positivo(self, numero):
        """Verifica si un número es positivo"""
        pass
    
    @abstractmethod
    def es_negativo(self, numero):
        """Verifica si un número es negativo"""
        pass
    
    @abstractmethod
    def es_cero(self, numero):
        """Verifica si un número es cero"""
        pass
    
    @abstractmethod
    def signo(self, numero):
        """Devuelve el signo de un número (1, -1, 0)"""
        pass
    
    @abstractmethod
    def es_mayor(self, a, b):
        """Verifica si a es mayor que b"""
        pass
    
    @abstractmethod
    def es_menor(self, a, b):
        """Verifica si a es menor que b"""
        pass
    
    @abstractmethod
    def es_igual(self, a, b):
        """Verifica si a es igual a b"""
        pass
    
    @abstractmethod
    def mayor_de_dos(self, a, b):
        """Devuelve el mayor de dos números"""
        pass
    
    @abstractmethod
    def menor_de_dos(self, a, b):
        """Devuelve el menor de dos números"""
        pass
    
    @abstractmethod
    def mayor_de_tres(self, a, b, c):
        """Devuelve el mayor de tres números"""
        pass
    
    @abstractmethod
    def menor_de_tres(self, a, b, c):
        """Devuelve el menor de tres números"""
        pass
    
    # Operaciones básicas con texto
    
    @abstractmethod
    def contar_caracteres(self, texto):
        """Cuenta los caracteres en un texto"""
        pass
    
    @abstractmethod
    def mayusculas(self, texto):
        """Convierte un texto a mayúsculas"""
        pass
    
    @abstractmethod
    def minusculas(self, texto):
        """Convierte un texto a minúsculas"""
        pass
    
    @abstractmethod
    def primera_letra(self, texto):
        """Devuelve la primera letra de un texto"""
        pass
    
    @abstractmethod
    def ultima_letra(self, texto):
        """Devuelve la última letra de un texto"""
        pass
    
    @abstractmethod
    def concatenar_textos(self, texto1, texto2):
        """Concatena dos textos"""
        pass
    
    @abstractmethod
    def repetir_texto(self, texto, veces):
        """Repite un texto n veces"""
        pass
    
    # Conversiones simples
    
    @abstractmethod
    def celsius_a_fahrenheit(self, celsius):
        """Convierte grados Celsius a Fahrenheit"""
        pass
    
    @abstractmethod
    def fahrenheit_a_celsius(self, fahrenheit):
        """Convierte grados Fahrenheit a Celsius"""
        pass
    
    @abstractmethod
    def metros_a_centimetros(self, metros):
        """Convierte metros a centímetros"""
        pass
    
    @abstractmethod
    def centimetros_a_metros(self, centimetros):
        """Convierte centímetros a metros"""
        pass
    
    @abstractmethod
    def minutos_a_segundos(self, minutos):
        """Convierte minutos a segundos"""
        pass
    
    @abstractmethod
    def segundos_a_minutos(self, segundos):
        """Convierte segundos a minutos"""
        pass
    
    @abstractmethod
    def horas_a_segundos(self, horas):
        """Convierte horas a segundos"""
        pass
    
    @abstractmethod
    def segundos_a_horas(self, segundos):
        """Convierte segundos a horas"""
        pass
    
    # Geometría básica
    
    @abstractmethod
    def area_rectangulo(self, base, altura):
        """Calcula el área de un rectángulo"""
        pass
    
    @abstractmethod
    def area_triangulo(self, base, altura):
        """Calcula el área de un triángulo"""
        pass
    
    @abstractmethod
    def area_cuadrado(self, lado):
        """Calcula el área de un cuadrado"""
        pass
    
    @abstractmethod
    def area_circulo(self, radio):
        """Calcula el área de un círculo"""
        pass
    
    @abstractmethod
    def perimetro_rectangulo(self, base, altura):
        """Calcula el perímetro de un rectángulo"""
        pass
    
    @abstractmethod
    def perimetro_cuadrado(self, lado):
        """Calcula el perímetro de un cuadrado"""
        pass
    
    @abstractmethod
    def perimetro_circulo(self, radio):
        """Calcula el perímetro de un círculo"""
        pass
    
    @abstractmethod
    def volumen_cubo(self, lado):
        """Calcula el volumen de un cubo"""
        pass
    
    @abstractmethod
    def volumen_cilindro(self, radio, altura):
        """Calcula el volumen de un cilindro"""
        pass