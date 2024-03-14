#include <stdio.h>
#include <complex.h>
#include <math.h>

// Define the alphabet and modulo value
const char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
const int modulo_value = 1000000;

// Define the baseX encoding function
void encode_baseX(char* input_string, int base, char* encoded) {
    int i;
    int number = 0;
    for (i = 0; input_string[i] != '\0'; i++) {
        number += (input_string[i] - '0') * pow(base, i);
    }
    for (i = 0; number > 0; i++) {
        encoded[i] = alphabet[number % base];
        number /= base;
    }
    encoded[i] = '\0';
}

// Define the baseX decoding function
void decode_baseX(char* input_string, int base, char* decoded) {
    int i;
    int number = 0;
    int length = strlen(input_string);
    for (i = 0; i < length; i++) {
        number += (input_string[i] - '0') * pow(base, length - i - 1);
    }
    for (i = 0; number > 0; i++) {
        decoded[i] = alphabet[number % base];
        number /= base;
    }
    decoded[i] = '\0';
}

// Define the Fourier transformation function
void fourier_transform(complex double* input, complex double* output, int size) {
    int i, j;
    complex double sum;
    for (i = 0; i < size; i++) {
        sum = 0;
        for (j = 0; j < size; j++) {
            sum += input[j] * cexp(-2 * I * PI * j * i / size);
        }
        output[i] = sum;
    }
}
