# Examen Final Software

## Parte I
Desde el root `./app`, ejecutar en el siguiente orden:

1. Eliminar pruebas antiguas (si existen) `rm -rf ./app/tests/out/*`
2. Ejecutar JMeter (genera results) `jmeter -n -t app/tests/jmeter/test_plan.jmx -l app/tests/out/results.jtl`
3. Ejecutar pruebas de covertura `python3 ./app/test_coverage.py`
4. Ejecutar pruebas de métricas `python3 ./app/test_calculate_metrics.py`

## Parte II
Desde el root `./app`, ejecutar en el siguiente orden:

1. Ejecutar Locust para testing