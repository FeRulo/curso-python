#!/usr/bin/env python3
"""
🎓 CURSO TDD - COORDINADOR PRINCIPAL
===================================

Framework educativo completo de 3 niveles para aprender programación 
usando Test-Driven Development (TDD).

ESTRUCTURA DEL PROYECTO:
├── 🟢 nivel_basico/     (50 ejercicios)
├── 🟡 nivel_intermedio/ (63 ejercicios) 
├── 🔴 nivel_avanzado/   (82 ejercicios)
└── 📋 README_CURSO.md   (documentación)

TOTAL: 195 ejercicios únicos con TDD completo
"""

import os
import sys
from pathlib import Path

# Colores para output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def print_header():
    """Muestra el encabezado del coordinador"""
    print(f"{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("🎓 CURSO TDD FRAMEWORK - COORDINADOR PRINCIPAL")
    print("=" * 60)
    print(f"{Colors.ENDC}")

def show_project_structure():
    """Muestra la estructura organizada del proyecto"""
    print(f"{Colors.BOLD}📁 ESTRUCTURA DEL PROYECTO:{Colors.ENDC}")
    print()
    
    # Verificar y mostrar cada nivel
    levels = [
        ("🟢 nivel_basico", "50 ejercicios fundamentales", "nivel_basico"),
        ("🟡 nivel_intermedio", "63 ejercicios algoritmos", "nivel_intermedio"),
        ("🔴 nivel_avanzado", "82 ejercicios especialización", "nivel_avanzado")
    ]
    
    total_exercises = 0
    
    for emoji_name, description, folder in levels:
        folder_path = Path(folder)
        if folder_path.exists():
            files = list(folder_path.glob("*.py"))
            exercises = [f for f in files if f.name.startswith("ejercicios_")]
            implementations = [f for f in files if f.name.startswith("MiImplementacion")]
            test_files = [f for f in files if f.name.startswith("test_mi_")]
            runners = [f for f in files if f.name.startswith("test_runner")]
            
            status = "✅ Completo" if all([exercises, implementations, test_files, runners]) else "❌ Incompleto"
            
            print(f"├── {emoji_name}/")
            print(f"│   └── {description}")
            print(f"│   └── Estado: {status}")
            
            # Extraer número de ejercicios del nombre
            if "50" in description:
                total_exercises += 50
            elif "63" in description:
                total_exercises += 63
            elif "82" in description:
                total_exercises += 82
        else:
            print(f"├── {emoji_name}/ ❌ No encontrado")
        print()
    
    print(f"{Colors.BOLD}📊 RESUMEN:{Colors.ENDC}")
    print(f"   Total de ejercicios: {total_exercises}")
    print(f"   Metodología: Test-Driven Development")
    print(f"   Test runners con numeración intuitiva")
    print()

def show_quick_commands():
    """Muestra comandos rápidos para cada nivel"""
    print(f"{Colors.BOLD}🚀 COMANDOS RÁPIDOS:{Colors.ENDC}")
    print()
    
    commands = [
        ("🟢 Nivel Básico", "nivel_basico", "test_runner.py"),
        ("🟡 Nivel Intermedio", "nivel_intermedio", "test_runner_intermedio.py"),
        ("🔴 Nivel Avanzado", "nivel_avanzado", "test_runner_avanzado.py")
    ]
    
    for level_name, folder, runner in commands:
        print(f"{level_name}:")
        print(f"   cd {folder}")
        print(f"   python {runner} --list    # Ver tests disponibles")
        print(f"   python {runner} 15        # Ejecutar test #15")
        print()

def show_tdd_methodology():
    """Explica la metodología TDD"""
    print(f"{Colors.BOLD}🔄 METODOLOGÍA TDD:{Colors.ENDC}")
    print()
    print(f"1. {Colors.RED}🔴 RED{Colors.ENDC}:    Ejecutar test (debe fallar)")
    print(f"2. {Colors.GREEN}🟢 GREEN{Colors.ENDC}:  Implementar código mínimo")  
    print(f"3. {Colors.BLUE}🔧 REFACTOR{Colors.ENDC}: Mejorar manteniendo tests")
    print()

def main():
    """Función principal del coordinador"""
    print_header()
    show_project_structure()
    show_quick_commands()
    show_tdd_methodology()
    
    print(f"{Colors.BOLD}📚 PARA MÁS INFO:{Colors.ENDC}")
    print("   cat README_CURSO.md")
    print()
    print(f"{Colors.GREEN}¡Framework TDD listo para usar! 🚀{Colors.ENDC}")

if __name__ == "__main__":
    main()