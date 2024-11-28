# Examen Final Software

## Parte I
Desde el root `./app`, ejecutar en el siguiente orden:

1. Eliminar pruebas antiguas (si existen) `rm -rf ./app/tests/out/*`
2. Ejecutar JMeter (genera results) `jmeter -n -t app/tests/jmeter/test_plan.jmx -l app/tests/out/results.jtl`
3. Ejecutar pruebas de covertura `python3 ./app/test_coverage.py`
4. Ejecutar pruebas de métricas `python3 ./app/test_calculate_metrics.py`

## Parte II
Desde el root `./app`, ejecutar en el siguiente orden:

1. Ejecutar Locust para testing `locust -f locustfile.py --headless -H http://localhost:8000 -u 30 -r 1 --run-time 180s --csv=./locust/stats`
2. Ejecutar JMeter para probar endpoint `jmeter -n -t app/tests/jmeter/test_plan_2.jmx -l app/tests/out2/results.jtl`
3. Ejecutar script logs `python3 scripts/search_logs.py`