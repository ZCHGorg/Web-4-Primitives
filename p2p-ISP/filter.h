#include <math.h>

// Add frequency modulation variables
double mod_frequency = 880e6; // Operating frequency in Hz
double mod_index = 0.5; // Modulation index (should be between 0 and 1)
double carrier_wave;

double filter(double input) {
    double output;
    double lowpass_output, highpass_output, bandpass_output;

    // Low-pass filter
    lowpass_output = 1 / (1 + pow(M_E, -CUTOFF_FREQUENCY_LOWPASS * input));

    // High-pass filter
    highpass_output = input - 1 / (1 + pow(M_E, -CUTOFF_FREQUENCY_HIGHPASS * input));

    // Band-pass filter
    bandpass_output = (1 / (1 + pow(M_E, -CUTOFF_FREQUENCY_BANDPASS_LOW * input))) - (1 / (1 + pow(M_E, -CUTOFF_FREQUENCY_BANDPASS_HIGH * input)));

    // Normalize output
    double max_output = fmax(fmax(lowpass_output, highpass_output), bandpass_output);
    lowpass_output /= max_output;
    highpass_output /= max_output;
    bandpass_output /= max_output;

    // Generate carrier wave
    carrier_wave = sin(2 * PI * mod_frequency * t);

    // Apply frequency modulation
    output = (1 + mod_index * carrier_wave) * lowpass_output * LOWPASS_TRIM + (1 + mod_index * carrier_wave) * highpass_output * HIGHPASS_TRIM + (1 + mod_index * carrier_wave) * bandpass_output * BANDPASS_TRIM;

    return output;
}
