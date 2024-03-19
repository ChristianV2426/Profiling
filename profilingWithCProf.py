import ctypes
import cProfile as profile
import pstats
import numpy as np

VECTORSIZE = 10000000

def python_execution():
    # Initialization
    vector = [i+1 for i in range(VECTORSIZE)]
    scalar = 2

    # Execution 
    result = [i * scalar for i in vector]

    return result

def numpy_execution():
    # Initialization
    vector = np.array([i+1 for i in range(VECTORSIZE)])
    scalar = 2

    # Execution
    result = vector * scalar

    return result


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

    # Conection with C function
    function.vectorScalarMultiply(c_vector, c_scalar, c_result, c_VECTORSIZE)

    return result


if __name__ == '__main__':

    #Profiling
    profile1 = profile.Profile()
    profile1.enable()
    python_time = python_execution()
    profile1.disable()

    profile2 = profile.Profile()
    profile2.enable()
    numpy_time = numpy_execution()
    profile2.disable()

    profile3 = profile.Profile()
    profile3.enable()
    shared_c_time = shared_c_execution()
    profile3.disable()

    print(f"Python execution time: ")
    stats1 = pstats.Stats(profile1).sort_stats('cumulative')
    stats1.print_stats()

    print(f"Numpy execution time: ")
    stats2 = pstats.Stats(profile2).sort_stats('cumulative')
    stats2.print_stats()

    print(f"shared_c_execution time: ")
    stats3 = pstats.Stats(profile3).sort_stats('cumulative')
    stats3.print_stats()


