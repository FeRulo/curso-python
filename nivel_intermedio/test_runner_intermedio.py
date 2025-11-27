#!/usr/bin/env python3
"""
Runner específico para ejecutar tests individuales de la implementación intermedia.

Uso:
    python3 test_runner_intermedio.py test_contar_digitos
    python3 test_runner_intermedio.py 15    # Por número
    python3 test_runner_intermedio.py --list  # Ver todos los tests
"""

import unittest
import sys
from test_mi_implementacion_intermedia import TestMiImplementacionIntermedia


def run_single_test(test_name):
    """
    Ejecuta un test específico de la clase TestMiImplementacionIntermedia
    
    Args:
        test_name (str): Nombre del método de test a ejecutar
    """
    # Crear una suite de test
    suite = unittest.TestSuite()
    
    # Agregar el test específico
    try:
        suite.addTest(TestMiImplementacionIntermedia(test_name))
    except ValueError as e:
        print(f"Error: Test '{test_name}' no encontrado.")
        print(f"Detalles: {e}")
        return False
    
    # Crear el runner con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Ejecutar el test
    result = runner.run(suite)
    
    # Retornar si fue exitoso
    return result.wasSuccessful()


def list_available_tests():
    """Lista todos los tests disponibles con números"""
    print("Tests disponibles (Implementación Intermedia):")
    print("=" * 50)
    
    # Obtener todos los métodos que empiecen con 'test_' y ordenar
    test_methods = [method for method in dir(TestMiImplementacionIntermedia) 
                   if method.startswith('test_')]
    test_methods.sort()  # Ordenar alfabéticamente
    
    for i, test_method in enumerate(test_methods, 1):
        print(f"{i:2d}. {test_method}")
    
    print(f"\nTotal: {len(test_methods)} tests disponibles")
    print("\nEjemplos de uso:")
    print("  python3 test_runner_intermedio.py 1          # Ejecutar primer test")
    print("  python3 test_runner_intermedio.py 25         # Ejecutar test #25")
    print("  python3 test_runner_intermedio.py factorial  # Ejecutar por nombre")


def get_test_by_number(number):
    """
    Obtiene el nombre del test por su número en la lista
    
    Args:
        number (int): Número del test
        
    Returns:
        str: Nombre del test o None si no existe
    """
    test_methods = [method for method in dir(TestMiImplementacionIntermedia) 
                   if method.startswith('test_')]
    test_methods.sort()  # Ordenar alfabéticamente para consistencia
    
    if 1 <= number <= len(test_methods):
        return test_methods[number - 1]
    return None


def main():
    """Función principal del runner"""
    if len(sys.argv) != 2:
        print("Uso: python3 test_runner_intermedio.py <nombre_del_test_o_número>")
        print("     python3 test_runner_intermedio.py --list  (para ver tests disponibles)")
        print("\nEjemplos:")
        print("  python3 test_runner_intermedio.py test_contar_digitos")
        print("  python3 test_runner_intermedio.py contar_digitos")
        print("  python3 test_runner_intermedio.py 15    # Por número")
        sys.exit(1)
    
    test_input = sys.argv[1]
    
    # Si pide listar los tests
    if test_input in ['--list', '-l', 'list']:
        list_available_tests()
        return
    
    test_name = None
    
    # Verificar si es un número
    if test_input.isdigit():
        number = int(test_input)
        test_name = get_test_by_number(number)
        if test_name is None:
            print(f"❌ Error: Número de test inválido '{number}'")
            print("   Usa 'python3 test_runner_intermedio.py --list' para ver los números válidos")
            sys.exit(1)
        print(f"Ejecutando test #{number}: {test_name}")
    else:
        # Es un nombre de test
        test_name = test_input
        # Agregar prefijo 'test_' si no lo tiene
        if not test_name.startswith('test_'):
            test_name = 'test_' + test_name
        print(f"Ejecutando test: {test_name}")
    
    print("=" * 50)
    
    # Ejecutar el test
    success = run_single_test(test_name)
    
    # Resultado final
    if success:
        print(f"\n✅ Test '{test_name}' PASÓ exitosamente!")
        sys.exit(0)
    else:
        print(f"\n❌ Test '{test_name}' FALLÓ!")
        sys.exit(1)


if __name__ == '__main__':
    main()