import ctypes
import timeit
import numpy as np

VECTORSIZE = 10000000

def python_execution():
    # Initialization
    vector = [i+1 for i in range(VECTORSIZE)]
    scalar = 2

    # Execution and profiling
    initial_time = timeit.default_timer()
    result = [i * scalar for i in vector]
    final_time = timeit.default_timer()

    return final_time - initial_time

def numpy_execution():
    # Initialization
    vector = np.array([i+1 for i in range(VECTORSIZE)])
    scalar = 2

    # Execution and profiling
    initial_time = timeit.default_timer()
    result = vector * scalar
    final_time = timeit.default_timer()

    # Checking results
    assert((result == [i * scalar for i in vector]).all())

    return final_time - initial_time


def shared_c_execution():
    function = ctypes.CDLL('./multescalar.so')

    # Python initialization
    vector = [i+1 for i in range(VECTORSIZE)]
    scalar = 2
    result = [0] * VECTORSIZE

    # C translation
    c_VECTORSIZE = ctypes.c_int(VECTORSIZE)
    c_vector = (ctypes.c_double * VECTORSIZE)(*vector)
    c_scalar = ctypes.c_double(scalar)
    c_result = (ctypes.c_double * VECTORSIZE)(*result)

    # Conection with C function and profiling
    initial_time = timeit.default_timer()
    function.vectorScalarMultiply(c_vector, c_scalar, c_result, c_VECTORSIZE)
    final_time = timeit.default_timer()

    # Checking results
    python_result = [c_result[i] for i in range(VECTORSIZE)]
    assert(python_result[:] == [i * scalar for i in vector[:]])

    return final_time - initial_time


if __name__ == '__main__':
    python_time = python_execution()
    numpy_time = numpy_execution()
    shared_c_time = shared_c_execution()

    print(f'Python execution time: {python_time:.5f}\n'
          f'Numpy execution time: {numpy_time:.5f}\n'
          f'Shared C execution time: {shared_c_time:.5f}\n')

    print(f'Numpy speedup: {python_time / numpy_time:.2f}\n'
          f'Shared C speedup: {python_time / shared_c_time:.2f}\n') 
