# Proyecto de Muestreo Aleatorio Simple

## Introducción al Muestreo Aleatorio Simple

El muestreo aleatorio simple es un tipo de muestreo probabilístico en el que todos los elementos de la población tienen la misma probabilidad de ser seleccionados. Para llevar a cabo este tipo de muestreo, los elementos son seleccionados al azar sin reemplazo, lo que garantiza la aleatoriedad del proceso.

### Ventajas:
- **Simplicidad**: Es fácil de entender y ejecutar.
- **Representatividad**: Si la muestra es lo suficientemente grande, puede ser representativa de la población total.
- **Menos sesgo**: Dado que todos los elementos tienen la misma probabilidad de ser seleccionados, se minimizan los sesgos de selección.

### Desventajas:
- **Dificultad para grandes poblaciones**: Puede ser complicado obtener una lista completa de todos los elementos de una población grande.
- **No considera subgrupos**: No es útil si se desea garantizar la inclusión de ciertos subgrupos dentro de la muestra.

## Objetivo del Proyecto

El objetivo de este proyecto es estimar el número de personas mayores de 15 años con primaria incompleta en las AGEBs de la alcaldía de Iztapalapa. Esta información será utilizada para diseñar un programa educativo que ayude a estas personas a obtener su certificado de primaria.

## Pasos del Proyecto

### 1. Prueba Piloto

Se realizó una prueba piloto con una muestra aleatoria de 12 observaciones de la población mayor de 15 años con primaria incompleta. Con base en esta muestra, se calculó el tamaño de muestra adecuado para un nivel de confianza del 95% y una precisión de 15 habitantes.

```python
# Selección de muestra piloto
tamano_muestra = 12
muestra_piloto = funcion.aleatorio_simple(data, tamano_muestra)
```

### 2. Cálculo del Tamaño de Muestra
Se determinó el tamaño de la muestra sin corrección por finitud utilizando la fórmula estándar, y posteriormente se aplicó la corrección para obtener el tamaño de muestra final.

```python
# Tamaño de muestra sin corrección
tamano_muestra_sin_correcion = funcion.media_sin_correcion(muestra_piloto, 'Población 15 años y más sin primaria', z=1.96, presicion=15)

# Tamaño de muestra con corrección
tamano_muestra_con_correccion = funcion.media_con_correcion(data, tamano_muestra_sin_correcion)
```

### 3. Cálculo de Intervalos de Confianza
Una vez determinada la muestra definitiva, se seleccionó aleatoriamente una muestra de 131 datos y se calcularon los intervalos de confianza para el promedio de personas mayores de 15 años con primaria incompleta, así como para el total estimado.

```python
# Cálculo del intervalo de confianza para el promedio
Limite_Inferior, Limite_Superior = funcion.intervalo_confianza(data, n, muestra_final['Población 15 años y más sin primaria'], z)
```

### 4. Estimación del Total de AGEBs con Más de 200 Habitantes
El programa se centrará en los AGEBs con al menos 200 habitantes mayores de 15 años sin primaria. Se estimó el número total de AGEBs que cumplen con este criterio.

```python
# Proporción de AGEBs con más de 200 habitantes
proporcion = funcion.proporcion_poblacion(a, n)
```

### 5. Comparación con los Valores Paramétricos
Finalmente, se compararon los resultados obtenidos en la muestra con los valores paramétricos de la población.

```python
# Comparación de resultados
resultados = pd.DataFrame({'Estimador': ['Media', 'Total', 'Proporción'],
                           'Población': [Media_pob, Suma_pob, Suma_Agebs_mayor_200],
                           'Muestra': [Media_muestra, total_estimado, total_estimado_proporcion],
                           'Error Parametra': [1-(Media_muestra/Media_pob), 1-(total_estimado/Suma_pob), 1-(total_estimado_proporcion/Suma_Agebs_mayor_200)]})

```

### Conclusiones
Este estudio ha permitido estimar de manera efectiva el número de personas mayores de 15 años sin primaria completa en la alcaldía de Iztapalapa. Además, se ha determinado el número máximo de AGEBs donde se podría implementar el programa educativo, basado en la población con al menos 200 habitantes

