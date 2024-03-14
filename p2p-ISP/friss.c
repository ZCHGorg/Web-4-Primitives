#include <math.h>

// Define antenna parameters
double antenna_gain = 6.0; // dBi
double wavelength;

// Define function to calculate wavelength based on operating frequency
double calculate_wavelength(double operating_frequency) {
    return 3e8/operating_frequency;
}

// Define function to calculate maximum range based on the Friis equation
double calculate_max_range(double operating_frequency) {
    wavelength = calculate_wavelength(operating_frequency);
    return wavelength/(4*M_PI*antenna_gain);
}

// Example usage of the above function
int main() {
    double operating_frequency = 880; // MHz
    double max_range = calculate_max_range(operating_frequency);
    printf("Operating frequency: %f MHz\n", operating_frequency);
    printf("Maximum range: %f km\n", max_range);
    return 0;
}
