#include <immintrin.h>
#include <stdio.h>
#include <assert.h>

// Function to perform vector-scalar multiplication
void vectorScalarMultiply(const double* vector, double scalar, double* result, int length) {

    for (int i = 0; i < length; i ++) {
      result[i] = vector[i] * scalar;
    }
}
