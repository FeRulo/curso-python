from abc import ABC, abstractmethod

class EjerciciosAvanzados(ABC):
    """
    NIVEL 3: AVANZADO - Algoritmos complejos y estructuras de datos
    50 ejercicios con algoritmos avanzados, estructuras de datos y optimización
    """
    
    # Algoritmos complejos, estructuras de datos avanzadas
    
    @abstractmethod
    def es_primo(self, numero):
        """Verifica si un número es primo"""
        pass
    
    @abstractmethod
    def numeros_primos_hasta(self, limite):
        """Encuentra todos los números primos hasta un límite"""
        pass
    
    @abstractmethod
    def suma_primos_hasta(self, limite):
        """Suma todos los números primos hasta un límite"""
        pass
    
    @abstractmethod
    def contar_primos_hasta(self, limite):
        """Cuenta números primos hasta un límite"""
        pass
    
    @abstractmethod
    def primo_siguiente(self, numero):
        """Encuentra el próximo número primo"""
        pass
    
    @abstractmethod
    def factorizacion_prima(self, numero):
        """Encuentra la factorización prima de un número"""
        pass
    
    @abstractmethod
    def es_perfecto(self, numero):
        """Verifica si un número es perfecto"""
        pass
    
    @abstractmethod
    def numeros_perfectos_hasta(self, limite):
        """Encuentra números perfectos hasta un límite"""
        pass
    
    @abstractmethod
    def es_abundante(self, numero):
        """Verifica si un número es abundante"""
        pass
    
    @abstractmethod
    def es_deficiente(self, numero):
        """Verifica si un número es deficiente"""
        pass
    
    @abstractmethod
    def mcd(self, a, b):
        """Calcula el máximo común divisor de dos números"""
        pass
    
    @abstractmethod
    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo de dos números"""
        pass
    
    @abstractmethod
    def divisores(self, numero):
        """Encuentra todos los divisores de un número"""
        pass
    
    @abstractmethod
    def contar_divisores(self, numero):
        """Cuenta los divisores de un número"""
        pass
    
    @abstractmethod
    def suma_divisores(self, numero):
        """Suma todos los divisores propios de un número"""
        pass
    
    # Operaciones avanzadas con listas
    
    @abstractmethod
    def ordenar_lista(self, lista):
        """Ordena una lista de manera ascendente"""
        pass
    
    @abstractmethod
    def ordenar_descendente(self, lista):
        """Ordena una lista de manera descendente"""
        pass
    
    @abstractmethod
    def eliminar_duplicados(self, lista):
        """Elimina elementos duplicados de una lista"""
        pass
    
    @abstractmethod
    def interseccion_listas(self, lista1, lista2):
        """Encuentra la intersección de dos listas"""
        pass
    
    @abstractmethod
    def diferencia_listas(self, lista1, lista2):
        """Encuentra la diferencia entre dos listas"""
        pass
    
    @abstractmethod
    def union_listas(self, lista1, lista2):
        """Encuentra la unión de dos listas"""
        pass
    
    @abstractmethod
    def rotar_lista(self, lista, posiciones):
        """Rota una lista cierta cantidad de posiciones"""
        pass
    
    @abstractmethod
    def sublista(self, lista, inicio, fin):
        """Extrae una sublista"""
        pass
    
    @abstractmethod
    def insertar_elemento(self, lista, elemento, posicion):
        """Inserta un elemento en una posición específica"""
        pass
    
    @abstractmethod
    def eliminar_elemento(self, lista, elemento):
        """Elimina un elemento de la lista"""
        pass
    
    @abstractmethod
    def reemplazar_elemento(self, lista, viejo, nuevo):
        """Reemplaza un elemento por otro en la lista"""
        pass
    
    @abstractmethod
    def frecuencia_elemento(self, lista, elemento):
        """Cuenta la frecuencia de un elemento en la lista"""
        pass
    
    @abstractmethod
    def elemento_mas_frecuente(self, lista):
        """Encuentra el elemento más frecuente en la lista"""
        pass
    
    @abstractmethod
    def segundo_mayor(self, lista):
        """Encuentra el segundo elemento mayor en la lista"""
        pass
    
    @abstractmethod
    def segundo_menor(self, lista):
        """Encuentra el segundo elemento menor en la lista"""
        pass
    
    @abstractmethod
    def busqueda_binaria(self, lista, elemento):
        """Busca un elemento usando búsqueda binaria"""
        pass
    
    @abstractmethod
    def mezclar_listas_ordenadas(self, lista1, lista2):
        """Mezcla dos listas ordenadas manteniendo el orden"""
        pass
    
    # Estadística
    
    @abstractmethod
    def mediana(self, lista):
        """Calcula la mediana de una lista"""
        pass
    
    @abstractmethod
    def moda(self, lista):
        """Calcula la moda de una lista"""
        pass
    
    @abstractmethod
    def rango_estadistico(self, lista):
        """Calcula el rango (max - min) de una lista"""
        pass
    
    @abstractmethod
    def cuartiles(self, lista):
        """Calcula los cuartiles de una lista"""
        pass
    
    @abstractmethod
    def percentil(self, lista, p):
        """Calcula un percentil específico"""
        pass
    
    @abstractmethod
    def varianza(self, lista):
        """Calcula la varianza de una lista"""
        pass
    
    @abstractmethod
    def desviacion_estandar(self, lista):
        """Calcula la desviación estándar de una lista"""
        pass
    
    @abstractmethod
    def coeficiente_variacion(self, lista):
        """Calcula el coeficiente de variación"""
        pass
    
    # Algoritmos de ordenamiento
    
    @abstractmethod
    def burbuja_sort(self, lista):
        """Implementa ordenamiento burbuja"""
        pass
    
    @abstractmethod
    def seleccion_sort(self, lista):
        """Implementa ordenamiento por selección"""
        pass
    
    @abstractmethod
    def insercion_sort(self, lista):
        """Implementa ordenamiento por inserción"""
        pass
    
    @abstractmethod
    def merge_sort(self, lista):
        """Implementa ordenamiento merge sort"""
        pass
    
    @abstractmethod
    def quick_sort(self, lista):
        """Implementa ordenamiento quick sort"""
        pass
    
    # Operaciones avanzadas con texto
    
    @abstractmethod
    def es_palindromo(self, texto):
        """Verifica si un texto es palíndromo"""
        pass
    
    @abstractmethod
    def es_anagrama(self, palabra1, palabra2):
        """Verifica si dos palabras son anagramas"""
        pass
    
    @abstractmethod
    def primer_caracter_no_repetido(self, texto):
        """Encuentra el primer carácter no repetido"""
        pass
    
    @abstractmethod
    def caracter_mas_frecuente(self, texto):
        """Encuentra el carácter más frecuente"""
        pass
    
    @abstractmethod
    def comprimir_cadena(self, texto):
        """Comprime una cadena (ej: 'aaa' -> 'a3')"""
        pass
    
    @abstractmethod
    def expandir_cadena(self, texto):
        """Expande una cadena comprimida (ej: 'a3' -> 'aaa')"""
        pass
    
    @abstractmethod
    def subsecuencia_comun_mas_larga(self, texto1, texto2):
        """Encuentra la subsecuencia común más larga"""
        pass
    
    @abstractmethod
    def subcadena_comun_mas_larga(self, texto1, texto2):
        """Encuentra la subcadena común más larga"""
        pass
    
    @abstractmethod
    def distancia_levenshtein(self, texto1, texto2):
        """Calcula la distancia de edición entre dos textos"""
        pass
    
    # Conversiones avanzadas
    
    @abstractmethod
    def numero_a_binario(self, numero):
        """Convierte un número decimal a binario"""
        pass
    
    @abstractmethod
    def binario_a_numero(self, binario):
        """Convierte un número binario a decimal"""
        pass
    
    @abstractmethod
    def numero_a_octal(self, numero):
        """Convierte un número decimal a octal"""
        pass
    
    @abstractmethod
    def octal_a_numero(self, octal):
        """Convierte un número octal a decimal"""
        pass
    
    @abstractmethod
    def numero_a_hexadecimal(self, numero):
        """Convierte un número decimal a hexadecimal"""
        pass
    
    @abstractmethod
    def hexadecimal_a_numero(self, hexadecimal):
        """Convierte un número hexadecimal a decimal"""
        pass
    
    @abstractmethod
    def numero_a_base(self, numero, base):
        """Convierte un número a cualquier base"""
        pass
    
    @abstractmethod
    def base_a_numero(self, numero_str, base):
        """Convierte un número de cualquier base a decimal"""
        pass
    
    # Operaciones con matrices
    
    @abstractmethod
    def crear_matriz(self, filas, columnas, valor_inicial):
        """Crea una matriz con un valor inicial"""
        pass
    
    @abstractmethod
    def sumar_matrices(self, matriz1, matriz2):
        """Suma dos matrices"""
        pass
    
    @abstractmethod
    def multiplicar_matrices(self, matriz1, matriz2):
        """Multiplica dos matrices"""
        pass
    
    @abstractmethod
    def transponer_matriz(self, matriz):
        """Transpone una matriz"""
        pass
    
    @abstractmethod
    def determinante_matriz(self, matriz):
        """Calcula el determinante de una matriz"""
        pass
    
    @abstractmethod
    def matriz_identidad(self, tamaño):
        """Crea una matriz identidad"""
        pass
    
    @abstractmethod
    def es_matriz_simetrica(self, matriz):
        """Verifica si una matriz es simétrica"""
        pass
    
    @abstractmethod
    def diagonal_principal(self, matriz):
        """Extrae la diagonal principal de una matriz"""
        pass
    
    # Validaciones y utilidades avanzadas
    
    @abstractmethod
    def validar_email(self, email):
        """Valida si un email tiene formato correcto"""
        pass
    
    @abstractmethod
    def extraer_dominio_email(self, email):
        """Extrae el dominio de un email"""
        pass
    
    @abstractmethod
    def validar_telefono(self, telefono):
        """Valida si un teléfono tiene formato correcto"""
        pass
    
    @abstractmethod
    def validar_fecha(self, dia, mes, año):
        """Valida si una fecha es correcta"""
        pass
    
    @abstractmethod
    def calcular_edad(self, fecha_nacimiento, fecha_actual):
        """Calcula la edad dada una fecha de nacimiento"""
        pass
    
    @abstractmethod
    def generar_password(self, longitud):
        """Genera una contraseña aleatoria"""
        pass
    
    @abstractmethod
    def fortaleza_password(self, password):
        """Evalúa la fortaleza de una contraseña"""
        pass
    
    @abstractmethod
    def es_numero(self, texto):
        """Verifica si una cadena representa un número"""
        pass
    
    @abstractmethod
    def extraer_numeros(self, texto):
        """Extrae todos los números de un texto"""
        pass
    
    @abstractmethod
    def calcular_imc(self, peso, altura):
        """Calcula el índice de masa corporal"""
        pass
    
    @abstractmethod
    def clasificar_imc(self, imc):
        """Clasifica el IMC (bajo peso, normal, sobrepeso, etc.)"""
        pass
    
    @abstractmethod
    def generar_fibonacci_hasta(self, limite):
        """Genera la secuencia de Fibonacci hasta un límite"""
        pass
    
    @abstractmethod
    def es_numero_armstrong(self, numero):
        """Verifica si un número es un número de Armstrong"""
        pass
    
    @abstractmethod
    def es_numero_feliz(self, numero):
        """Verifica si un número es un número feliz"""
        pass
    
    @abstractmethod
    def suma_naturales_formula(self, n):
        """Calcula suma de naturales usando fórmula"""
        pass
    
    @abstractmethod
    def combinaciones(self, n, r):
        """Calcula combinaciones C(n,r)"""
        pass
    
    @abstractmethod
    def permutaciones(self, n, r):
        """Calcula permutaciones P(n,r)"""
        pass