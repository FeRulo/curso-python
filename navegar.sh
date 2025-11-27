#!/bin/bash
# 🎓 CURSO TDD - NAVEGACIÓN RÁPIDA
# ================================

echo "🎓 CURSO TDD FRAMEWORK - NAVEGACIÓN RÁPIDA"
echo "=========================================="
echo ""

PS3="Selecciona un nivel (o 'q' para salir): "

options=(
    "🟢 Nivel Básico (50 ejercicios)"
    "🟡 Nivel Intermedio (63 ejercicios)" 
    "🔴 Nivel Avanzado (82 ejercicios)"
    "📋 Ver estructura completa"
    "📚 Leer documentación"
    "❌ Salir"
)

select opt in "${options[@]}"; do
    case $opt in
        "🟢 Nivel Básico (50 ejercicios)")
            echo "Navegando a nivel básico..."
            cd nivel_basico
            echo "Ejecuta: python3 test_runner.py --list"
            exec bash
            ;;
        "🟡 Nivel Intermedio (63 ejercicios)")
            echo "Navegando a nivel intermedio..."
            cd nivel_intermedio  
            echo "Ejecuta: python3 test_runner_intermedio.py --list"
            exec bash
            ;;
        "🔴 Nivel Avanzado (82 ejercicios)")
            echo "Navegando a nivel avanzado..."
            cd nivel_avanzado
            echo "Ejecuta: python3 test_runner_avanzado.py --list" 
            exec bash
            ;;
        "📋 Ver estructura completa")
            echo "Mostrando estructura..."
            python3 coordinador.py
            ;;
        "📚 Leer documentación")
            echo "Abriendo documentación..."
            cat README_CURSO.md | head -50
            echo ""
            echo "Para ver completa: cat README_CURSO.md"
            ;;
        "❌ Salir")
            echo "¡Hasta pronto! 👋"
            break
            ;;
        *) 
            echo "Opción inválida $REPLY"
            ;;
    esac
done