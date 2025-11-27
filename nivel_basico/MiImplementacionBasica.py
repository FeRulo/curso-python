from ejercicios_basicos import EjerciciosBasicos

class MiImplementacionBasica(EjerciciosBasicos):
    """
    Implementación concreta de la clase abstracta EjerciciosBasicos.
    
    Esta clase implementa todos los métodos abstractos definidos en EjerciciosBasicos.
    Actualmente solo tiene implementaciones básicas, el resto está por implementar.
    """
    
    def sumar_dos_numeros(self, a, b):
        return a + b
    
    def restar_dos_numeros(self, a, b):
        return a - b
        
    def multiplicar_dos_numeros(self, a, b):
        return a * b
        
    def dividir_dos_numeros(self, a, b):
        return a / b 
        
    def resto_division(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def f(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def g(self, x):
        return 2 * x
        
    def valor_absoluto(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def potencia(self, base, exponente):
        raise NotImplementedError("Método no implementado aún")
        
    def raiz_cuadrada(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def es_par(self, n):
        raise NotImplementedError("Método no implementado aún")
        
    def es_impar(self, n):
        raise NotImplementedError("Método no implementado aún")
        
    def es_positivo(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def es_negativo(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def es_cero(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def signo(self, x):
        raise NotImplementedError("Método no implementado aún")
        
    def es_mayor(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def es_menor(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def es_igual(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def mayor_de_dos(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def menor_de_dos(self, a, b):
        raise NotImplementedError("Método no implementado aún")
        
    def mayor_de_tres(self, a, b, c):
        raise NotImplementedError("Método no implementado aún")
        
    def menor_de_tres(self, a, b, c):
        raise NotImplementedError("Método no implementado aún")
        
    def contar_caracteres(self, texto):
        raise NotImplementedError("Método no implementado aún")
        
    def mayusculas(self, texto):
        raise NotImplementedError("Método no implementado aún")
        
    def minusculas(self, texto):
        raise NotImplementedError("Método no implementado aún")
        
    def primera_letra(self, texto):
        raise NotImplementedError("Método no implementado aún")
        
    def ultima_letra(self, texto):
        raise NotImplementedError("Método no implementado aún")
        
    def concatenar_textos(self, texto1, texto2):
        raise NotImplementedError("Método no implementado aún")
        
    def repetir_texto(self, texto, n):
        raise NotImplementedError("Método no implementado aún")
        
    def celsius_a_fahrenheit(self, celsius):
        raise NotImplementedError("Método no implementado aún")
        
    def fahrenheit_a_celsius(self, fahrenheit):
        raise NotImplementedError("Método no implementado aún")
        
    def metros_a_centimetros(self, metros):
        raise NotImplementedError("Método no implementado aún")
        
    def centimetros_a_metros(self, centimetros):
        raise NotImplementedError("Método no implementado aún")
        
    def minutos_a_segundos(self, minutos):
        raise NotImplementedError("Método no implementado aún")
        
    def segundos_a_minutos(self, segundos):
        raise NotImplementedError("Método no implementado aún")
        
    def horas_a_segundos(self, horas):
        raise NotImplementedError("Método no implementado aún")
        
    def segundos_a_horas(self, segundos):
        raise NotImplementedError("Método no implementado aún")
        
    def area_rectangulo(self, largo, ancho):
        raise NotImplementedError("Método no implementado aún")
        
    def area_triangulo(self, base, altura):
        raise NotImplementedError("Método no implementado aún")
        
    def area_cuadrado(self, lado):
        raise NotImplementedError("Método no implementado aún")
        
    def area_circulo(self, radio):
        raise NotImplementedError("Método no implementado aún")
        
    def perimetro_rectangulo(self, largo, ancho):
        raise NotImplementedError("Método no implementado aún")
        
    def perimetro_cuadrado(self, lado):
        raise NotImplementedError("Método no implementado aún")
        
    def perimetro_circulo(self, radio):
        raise NotImplementedError("Método no implementado aún")
        
    def volumen_cubo(self, lado):
        raise NotImplementedError("Método no implementado aún")
        
    def volumen_cilindro(self, radio, altura):
        raise NotImplementedError("Método no implementado aún")
