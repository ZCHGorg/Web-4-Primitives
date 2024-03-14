#define LOWPASS_TRIM 0.3
#define HIGHPASS_TRIM 0.4
#define BANDPASS_TRIM 0.3

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

    // Adjust trim accordingly
    output = lowpass_output * LOWPASS_TRIM + highpass_output * HIGHPASS_TRIM + bandpass_output * BANDPASS_TRIM;

    return output;
}

// By Josef Kulovany, ZCHG.org, Copyright 2023 - Present, All Rights Reserved