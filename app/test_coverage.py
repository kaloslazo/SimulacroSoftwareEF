import coverage
import pytest
import os

def run_tests_with_coverage():
    # Crear directorio coverage si no existe
    if not os.path.exists('coverage'):
        os.makedirs('coverage')

    # Configurar coverage
    cov = coverage.Coverage(
        source=['app'],
        omit=[
            '*/app/setup.py',
            '*/app/test_calculate_metrics.py',
            '*/app/test_coverage.py',
            '*/app/test_performance.py',
            '*/app/__pycache__/*',
            '*/app/tests/*'
        ],
        branch=True
    )

    # Iniciar coverage
    cov.start()

    # Ejecutar tests
    test_files = [
        'app/test_api.py',
        'app/test_database.py',
        'app/test_endpoints.py',
        'app/test_health.py',
        'app/test_monitor.py',
        'app/test_recommendation.py',
        'app/tests_database_conn.py'
    ]
    
    pytest.main(['-v'] + test_files)

    # Detener coverage
    cov.stop()
    
    # Guardar reporte
    cov.save()
    
    # Generar reporte HTML
    cov.html_report(directory='coverage/html')
    
    # Mostrar reporte en consola
    percentage = cov.report()
    
    # Guardar porcentaje en archivo
    with open('coverage/coverage.txt', 'w') as f:
        f.write(str(percentage))

    print(f"Code coverage: {percentage}%")
    return percentage

if __name__ == '__main__':
    run_tests_with_coverage()