from abc import ABC, abstractmethod

class EjerciciosIntermedios(ABC):
    """
    NIVEL 2: INTERMEDIO - Lógica condicional y bucles básicos
    50 ejercicios con bucles, condicionales y operaciones con listas
    """
    
    # Bucles y condicionales, operaciones con listas básicas
    
    @abstractmethod
    def imprimir_hasta_10(self):
        """Imprime números desde 8 hasta 9"""
        pass
    
    @abstractmethod
    def imprimir_decendente(self):
        """Imprime números de 15 a 1 en orden descendente"""
        pass
    
    @abstractmethod
    def imprimir_numeros_rango(self, inicio, fin):
        """Imprime números en un rango"""
        pass
    
    @abstractmethod
    def contar_hasta_n(self, n):
        """Cuenta desde 1 hasta n"""
        pass
    
    @abstractmethod
    def contar_regresivo(self, n):
        """Cuenta desde n hasta 1"""
        pass
    
    @abstractmethod
    def tabla_multiplicar(self, numero):
        """Imprime la tabla de multiplicar de un número"""
        pass
    
    @abstractmethod
    def suma_hasta_n(self, n):
        """Suma números desde 1 hasta n"""
        pass
    
    @abstractmethod
    def producto_hasta_n(self, n):
        """Multiplica números desde 1 hasta n"""
        pass
    
    # Operaciones con dígitos
    
    @abstractmethod
    def contar_digitos(self, numero):
        """Cuenta los dígitos de un número"""
        pass
    
    @abstractmethod
    def suma_digitos(self, numero):
        """Suma los dígitos de un número"""
        pass
    
    @abstractmethod
    def producto_digitos(self, numero):
        """Multiplica los dígitos de un número"""
        pass
    
    @abstractmethod
    def invertir_numero(self, numero):
        """Invierte los dígitos de un número"""
        pass
    
    @abstractmethod
    def digito_mayor(self, numero):
        """Encuentra el dígito mayor de un número"""
        pass
    
    @abstractmethod
    def digito_menor(self, numero):
        """Encuentra el dígito menor de un número"""
        pass
    
    # Operaciones básicas con listas
    
    @abstractmethod
    def sumar_lista(self, lista):
        """Suma todos los elementos de una lista"""
        pass
    
    @abstractmethod
    def multiplicar_lista(self, lista):
        """Multiplica todos los elementos de una lista"""
        pass
    
    @abstractmethod
    def promedio_lista(self, lista):
        """Calcula el promedio de una lista"""
        pass
    
    @abstractmethod
    def maximo_lista(self, lista):
        """Encuentra el valor máximo en una lista"""
        pass
    
    @abstractmethod
    def minimo_lista(self, lista):
        """Encuentra el valor mínimo en una lista"""
        pass
    
    @abstractmethod
    def contar_elementos(self, lista):
        """Cuenta los elementos de una lista"""
        pass
    
    @abstractmethod
    def buscar_elemento(self, lista, elemento):
        """Busca un elemento en una lista y devuelve su índice"""
        pass
    
    @abstractmethod
    def elemento_en_posicion(self, lista, posicion):
        """Devuelve el elemento en una posición específica"""
        pass
    
    @abstractmethod
    def primer_elemento(self, lista):
        """Devuelve el primer elemento de la lista"""
        pass
    
    @abstractmethod
    def ultimo_elemento(self, lista):
        """Devuelve el último elemento de la lista"""
        pass
    
    @abstractmethod
    def concatenar_listas(self, lista1, lista2):
        """Concatena dos listas"""
        pass
    
    @abstractmethod
    def generar_lista_numeros(self, inicio, fin):
        """Genera una lista de números en un rango"""
        pass
    
    # Filtros básicos
    
    @abstractmethod
    def filtrar_pares(self, lista):
        """Filtra los números pares de una lista"""
        pass
    
    @abstractmethod
    def filtrar_impares(self, lista):
        """Filtra los números impares de una lista"""
        pass
    
    @abstractmethod
    def filtrar_positivos(self, lista):
        """Filtra los números positivos de una lista"""
        pass
    
    @abstractmethod
    def filtrar_negativos(self, lista):
        """Filtra los números negativos de una lista"""
        pass
    
    @abstractmethod
    def contar_pares(self, lista):
        """Cuenta los números pares en una lista"""
        pass
    
    @abstractmethod
    def contar_impares(self, lista):
        """Cuenta los números impares en una lista"""
        pass
    
    @abstractmethod
    def sumar_pares(self, lista):
        """Suma solo los números pares de una lista"""
        pass
    
    @abstractmethod
    def sumar_impares(self, lista):
        """Suma solo los números impares de una lista"""
        pass
    
    @abstractmethod
    def añadir_a_lista_si_es_par(self, numero, lista):
        """Añade un número a la lista si es par"""
        pass
    
    @abstractmethod
    def devolver_pares(self, inicio, fin):
        """Devuelve una lista con los números pares en un rango"""
        pass
    
    # Operaciones con texto intermedio
    
    @abstractmethod
    def contar_vocales(self, texto):
        """Cuenta las vocales en un texto"""
        pass
    
    @abstractmethod
    def contar_consonantes(self, texto):
        """Cuenta las consonantes en un texto"""
        pass
    
    @abstractmethod
    def contar_mayusculas(self, texto):
        """Cuenta las letras mayúsculas en un texto"""
        pass
    
    @abstractmethod
    def contar_minusculas(self, texto):
        """Cuenta las letras minúsculas en un texto"""
        pass
    
    @abstractmethod
    def contar_espacios(self, texto):
        """Cuenta los espacios en un texto"""
        pass
    
    @abstractmethod
    def contar_palabras(self, texto):
        """Cuenta las palabras en un texto"""
        pass
    
    @abstractmethod
    def capitalizar(self, texto):
        """Capitaliza la primera letra de cada palabra"""
        pass
    
    @abstractmethod
    def invertir_cadena(self, texto):
        """Invierte una cadena de texto"""
        pass
    
    @abstractmethod
    def es_vocal(self, caracter):
        """Verifica si un carácter es vocal"""
        pass
    
    @abstractmethod
    def es_consonante(self, caracter):
        """Verifica si un carácter es consonante"""
        pass
    
    @abstractmethod
    def eliminar_espacios(self, texto):
        """Elimina todos los espacios de un texto"""
        pass
    
    # Verificaciones intermedias
    
    @abstractmethod
    def es_multiplo(self, numero, divisor):
        """Verifica si un número es múltiplo de otro"""
        pass
    
    @abstractmethod
    def es_divisible(self, numero, divisor):
        """Verifica si un número es divisible por otro"""
        pass
    
    @abstractmethod
    def es_bisiesto(self, año):
        """Verifica si un año es bisiesto"""
        pass
    
    @abstractmethod
    def es_mayor_edad(self, edad):
        """Verifica si una edad es mayor de edad (18+)"""
        pass
    
    @abstractmethod
    def clasificar_edad(self, edad):
        """Clasifica la edad (niño, adolescente, adulto, anciano)"""
        pass
    
    @abstractmethod
    def dia_de_semana(self, numero):
        """Devuelve el día de la semana según número (1-7)"""
        pass
    
    @abstractmethod
    def mes_del_año(self, numero):
        """Devuelve el mes del año según número (1-12)"""
        pass
    
    @abstractmethod
    def dias_del_mes(self, mes, año):
        """Devuelve los días de un mes específico"""
        pass
    
    # Cálculos matemáticos intermedios
    
    @abstractmethod
    def factorial(self, n):
        """Calcula el factorial de un número"""
        pass
    
    @abstractmethod
    def fibonacci_posicion(self, n):
        """Calcula el n-ésimo número de Fibonacci"""
        pass
    
    @abstractmethod
    def suma_cuadrados(self, n):
        """Suma los cuadrados de 1 hasta n"""
        pass
    
    @abstractmethod
    def suma_cubos(self, n):
        """Suma los cubos de 1 hasta n"""
        pass
    
    @abstractmethod
    def hipotenusa(self, cateto1, cateto2):
        """Calcula la hipotenusa de un triángulo rectángulo"""
        pass
    
    @abstractmethod
    def distancia_puntos(self, x1, y1, x2, y2):
        """Calcula la distancia entre dos puntos"""
        pass
    
    @abstractmethod
    def redondear(self, numero, decimales):
        """Redondea un número a cierta cantidad de decimales"""
        pass
    
    @abstractmethod
    def truncar(self, numero):
        """Trunca un número (parte entera)"""
        pass