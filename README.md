# Tarea Profiling - Infraestructuras Paralelas y Distribuidas

## Autores
- [Samuel Galindo Cuevas](https://github.com/SakyJoestar) - 2177491
- [Nicolás Herrera Marulanda](https://github.com/Herreran903) - 2182551
- [Christian David Vargas Gutiérrez](https://github.com/ChristianV2426) - 2179172

## Profesor
- John Alexander Sanabria PhD

# Descripción

Este repositorio contiene implementaciones para realizar una multiplicación escalar de un vector en Python puro, NumPy y en C compartido utilizando SIMD (Single Instruction, Multiple Data). El propósito principal es comparar el rendimiento de las implementaciones mediante el uso de `timeit` y `cProfile`.

## multescalar.c

El código en C implementa una función llamada `vectorScalarMultiply` que realiza la multiplicación escalar de un vector utilizando instrucciones de AVX (Advanced Vector Extensions). Esta función carga el vector en bloques de 4 elementos para aprovechar las capacidades de paralelización de AVX y utiliza operaciones vectoriales para realizar la multiplicación escalar de manera eficiente.

### Compilación del código

El comando de compilación es el siguiente:

```bash
gcc -mavx -fPIC -shared -o multescalar.so multescalar.c
```

Este comando compila el código en C y genera una biblioteca compartida llamada `multescalar.so`. A continuación, se explican las opciones utilizadas en el comando:

- `-mavx`: Habilita el conjunto de instrucciones AVX para aprovechar las capacidades de procesamiento vectorial de la CPU.
- `-fPIC`: Genera código objeto independiente de la posición de memoria, lo que permite cargar la biblioteca compartida en cualquier dirección de memoria.
- `-shared`: Indica al compilador que debe generar una biblioteca compartida en lugar de un ejecutable. Por ello la terminacion del archivo en .so (Shared Object).
- `-o multescalar.so`: Especifica el nombre del archivo de salida, que en este caso es `multescalar.so`.

## profiling.py

Este archivo Python, `profiling.py`, contiene tres funciones que implementan la multiplicación escalar utilizando diferentes enfoques: `python_execution`, que utiliza Python puro y listas para la operación; `numpy_execution`, que aprovecha la eficiencia de la biblioteca NumPy; y `shared_c_execution`, que utiliza una biblioteca compartida en C, `multescalar.so`, para realizar la operación de manera eficiente mediante instrucciones SIMD. Utilizando `timeit` para medir el tiempo de ejecución de cada función y comparar su rendimiento.

Para ejecutar este archivo, puedes usar el siguiente comando en la consola:

```bash
python profiling.py
```

Asegúrate de tener instalado `timeit`. Alternativamente, si estás utilizando un IDE que lo permita, también puedes ejecutar el codigo utilizando el botón de ejecución de código integrado, si está disponible en tu entorno de desarrollo.

## profilingWithCProf.py

Este archivo Python, `profiling.py`, contiene tres funciones que implementan la multiplicación escalar utilizando diferentes enfoques: `python_execution`, que utiliza Python puro y listas para la operación; `numpy_execution`, que aprovecha la eficiencia de la biblioteca NumPy; y `shared_c_execution`, que utiliza una biblioteca compartida en C, `multescalar.so`, para realizar la operación de manera eficiente mediante instrucciones SIMD. Utilizando `cProfile` para realizar un análisis detallado del rendimiento de cada función y comparar su eficacia.

Para ejecutar este archivo, puedes usar el siguiente comando en la consola:

```bash
python profilingWithCProf.py
```

Asegúrate de tener instalado `cProfile` y `pstats`. Alternativamente, si estás utilizando un IDE que lo permita, también puedes ejecutar el codigo utilizando el botón de ejecución de código integrado, si está disponible en tu entorno de desarrollo.