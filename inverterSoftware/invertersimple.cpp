#define PI 3.14159265358979323846

#define SINE_TABLE_SIZE 100
const int16_t sine_table[SINE_TABLE_SIZE] = {
    0, // 0 degrees
    ... // Fill in the rest of the sine table
    32767 // 180 degrees
};

int16_t get_sine_value(uint16_t angle) {
    // Scale the angle to be between 0 and SINE_TABLE_SIZE-1
    angle = (angle % 360) * (SINE_TABLE_SIZE / 360);
    return sine_table[angle];
}

void main() {
    // Use the get_sine_value function to get the sine value for the current angle
    int16_t sine_value = get_sine_value(current_angle);
// Use the sine value to control the PWM output
    set_pwm_duty_cycle(sine_value);
// increase the angle by 54 degrees every iteration
    current_angle += 54;
}