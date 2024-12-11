# README - Ejecución de Ejercicios con Hadoop MapReduce

Este documento describe cómo realizar el procesamiento de datos utilizando Hadoop y el modelo MapReduce para resolver una serie de ejercicios. Se parte de un archivo de datos (`purchases.txt`) que contiene registros de compras, y se aplican diferentes funciones Mapper y Reducer para extraer información relevante.

Hadoop permite procesar grandes volúmenes de datos distribuidos en múltiples nodos, aprovechando su sistema de archivos distribuido (HDFS) y la ejecución paralela.

---

## Ejecución en el clúster de Hadoop

### 1. Subir el archivo de datos al sistema HDFS
Asegúrate de que el archivo `purchases.txt` esté disponible en HDFS antes de ejecutar los ejercicios:
```bash
hdfs dfs -put purchases.txt PURCHASES
```

### 2. Subir los scripts Mapper y Reducer a HDFS
Los scripts necesarios para cada ejercicio deben estar disponibles en el clúster. Sube `mapper.py` y `reducer.py` con:
```bash
hdfs dfs -put mapper.py reducer.py
```

### 3. Ejecución de cada ejercicio
Para ejecutar el trabajo de MapReduce, utiliza el siguiente comando general, adaptando el directorio de salida y los scripts según el ejercicio:
```bash
mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output <DIRECTORIO_DE_SALIDA> -mapper mapper.py -reducer reducer.py
```

---

## Ejercicios

### Ejercicio 1.1: Manejo de líneas con formato incorrecto
1. **Objetivo:** Modificar el Mapper para que descarte líneas mal formateadas y procese las demás.
2. **Ejecución en Hadoop:**
   ```bash
   mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA_1_1 -mapper mapper.py -reducer reducer.py
   ```

---

### Ejercicio 1.2: Total de ventas por categoría
1. **Objetivo:** Crear un Mapper y Reducer que calculen el total de ventas por categoría.
2. **Ejecución en Hadoop:**
   ```bash
   mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA_1_2 -mapper mapper.py -reducer reducer.py
   ```

---

### Ejercicio 1.3: Venta más alta por tipo de pago
1. **Objetivo:** Configurar el Mapper y Reducer para obtener la venta más alta registrada para cada tipo de pago.
2. **Ejecución en Hadoop:**
   ```bash
   mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA_1_3 -mapper mapper.py -reducer reducer.py
   ```

---

### Ejercicio 1.4: Venta máxima absoluta
1. **Objetivo:** Modificar los scripts para devolver únicamente la venta más alta de todas las registradas.
2. **Ejecución en Hadoop:**
   ```bash
   mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA_1_4 -mapper mapper.py -reducer reducer.py
   ```

---

### Ejercicio 1.5: Total de ventas
1. **Objetivo:** Configurar el Mapper y Reducer para calcular el total global de ventas.
2. **Ejecución en Hadoop:**
   ```bash
   mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA_1_5 -mapper mapper.py -reducer reducer.py
   ```

---

**Autor:** Alexia Caride Yáñez 
**Fecha:** 11/12/2024  
**Versión:** 1.0
