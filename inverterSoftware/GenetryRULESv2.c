#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>
#include <winsock2.h>
#include <filter.h>

#define PI 3.14159265
#define OVER_CURRENT_LIMIT 50 // Over current protection limit in amps
#define OVER_VOLTAGE_LIMIT 120 // Over voltage protection limit in volts
#define OVER_FREQUENCY_LIMIT 65 // Over frequency protection limit in Hz
#define MAX_TEMPERATURE 80 // Maximum allowed temperature in degrees Celsius
#define MAINS_VOLTAGE_LIMIT 220 // Limit for mains voltage in volts
#define BATTERY_VOLTAGE_LIMIT 10 // Limit for battery voltage in volts
#define BATTERY_LOW_LEVEL_LIMIT 20 // Limit for battery low level in percentage
#define PORT 1234 // Port for wifi communication

int input_source = 0; // 0 = mains, 1 = inverter, 2 = battery
int over_current_count = 0; // Counter for over current events
int over_voltage_count = 0; // Counter for over voltage events
int over_frequency_count = 0; // Counter for over frequency events
int temperature = 0; // Current temperature of the inverter
int mains_voltage = 0; // Current mains voltage
int battery_voltage = 0; // Current battery voltage
int battery_level = 0; // Current battery level in percentage
int frequency = 60; // Frequency of the inverter in Hz
int amplitude = 100; // Amplitude of the inverter in V
int phase = 0; // Phase shift of the inverter in degrees

void *monitor_input_source(void *arg) {
    while (1) {
        // Check for mains voltage
        mains_voltage = readMainsVoltage(); // Read mains voltage from a sensor
        if (mains_voltage < MAINS_VOLTAGE_LIMIT) {
            printf("Mains voltage too low\n");
            // Switch to inverter power
            input_source = 1;
        } else {
            // Switch back to mains power
            input_source = 0;
        }

        // Check for battery voltage
        battery_voltage = readBatteryVoltage(); // Read battery voltage from a sensor
        if (battery_voltage < BATTERY_VOLTAGE_LIMIT) {
            printf("Battery voltage too low\n");
            // Switch to battery power
            input_source = 2;
        }

        // Check for battery level
        battery_level = readBatteryLevel(); // Read battery level from a sensor
        if (battery_level < BATTERY_LOW_LEVEL_LIMIT) {
            printf("Battery level too low\n");
            // Send warning message
        }

        sleep(1); // Sleep for 1 second
    }
}

void *wifi_communication(void *arg) {
    WSADATA wsa;
    SOCKET s, new_socket;
    struct sockaddr_in server, client;
    int c;
    char *message;

    printf("Initialising Winsock...\n");
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed. Error Code : %d", WSAGetLastError());
        return 1;
    }

    printf("Creating socket...\n");
    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s == INVALID_SOCKET) {
        printf("Could not create socket : %d", WSAGetLastError());
    }

    printf("Preparing sockaddr_in...\n");
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(PORT);

    printf("Binding...\n");
    if (bind(s, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
        printf("Bind failed with error code : %d", WSAGetLastError());
    }

    listen(s, 3);

    printf("Waiting for incoming connections...\n");
    c = sizeof(struct sockaddr_in);
    while ((new_socket = accept(s, (struct sockaddr *)&client, &c)) != INVALID_SOCKET) {
        printf("Connection accepted from %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));

        message = "Welcome to the inverter server.\nEnter 'status' to see the current status of the inverter.\nEnter 'set frequency [value]' to set the frequency of the inverter.\nEnter 'set amplitude [value]' to set the amplitude of the inverter.\nEnter 'set phase [value]' to set the phase shift of the inverter.\nEnter 'exit' to close the connection.\n";
        send(new_socket, message, strlen(message), 0);

        while (1) {
            char client_message[2000];
            int read_size;

            if ((read_size = recv(new_socket, client_message, 2000, 0)) > 0) {
                client_message[read_size] = '\0';
                printf("Received: %s\n", client_message);

                if (strcmp(client_message, "exit\n") == 0) {
                    break;
                } else if (strcmp(client_message, "status\n") == 0) {
                    char status_message[1000];
                    sprintf(status_message, "Input source: %d\nFrequency: %d\nAmplitude: %d\nPhase: %d\nTemperature: %d\nMains voltage: %d\nBattery voltage: %d\nBattery level: %d%%\n", input_source, frequency, amplitude, phase, temperature, mains_voltage, battery_voltage, battery_level);
                    send(new_socket, status_message, strlen(status_message), 0);
                } else if (strncmp(client_message, "set frequency ", 14) == 0) {
                    int new_frequency = atoi(client_message + 14);
                    if (new_frequency > 0) {
                        frequency = new_frequency;
                        send(new_socket, "Frequency set\n", 13, 0);
                    } else {
                        send(new_socket, "Invalid frequency\n", 18, 0);
                    }
                } else if (strncmp(client_message, "set amplitude ", 13) == 0) {
                    int new_amplitude = atoi(client_message + 13);
                    if (new_amplitude > 0) {
                        amplitude = new_amplitude;
                        send(new_socket, "Amplitude set\n", 14, 0);
                    } else {
                        send(new_socket, "Invalid amplitude\n", 17, 0);
                    }
                } else if (strncmp(client_message, "set phase ", 10) == 0) {
                    int new_phase = atoi(client_message + 10);
                    phase = new_phase;
                    send(new_socket, "Phase set\n", 10, 0);
                } else {
                    send(new_socket, "Invalid command\n", 15, 0);
                }
            }
        }

        closesocket(new_socket);
    }

    closesocket(s);
    WSACleanup();
}

int main() {
    int time_step = 0.01; // Time step for the inverter in seconds
    
    pthread_t monitor_thread, wifi_thread;
    pthread_create(&monitor_thread, NULL, monitor_input_source, NULL);
    pthread_create(&wifi_thread, NULL, wifi_communication, NULL);
    
    for (double t = 0; t < 10; t += time_step) {
        double output = amplitude * sin(2 * PI * frequency * t + phase);

        // Check for over current
        if (output > OVER_CURRENT_LIMIT) {
            printf("Over current detected at time %.2f\n", t);
            over_current_count++;
            // Take appropriate action (e.g. shut down the inverter)
        }

        // Check for over voltage
        if (output > OVER_VOLTAGE_LIMIT) {
            printf("Over voltage detected at time %.2f\n", t);
            over_voltage_count++;
            // Take appropriate action (e.g. shut down the inverter)
        }

        // Check for over frequency
        if (frequency > OVER_FREQUENCY_LIMIT) {
            printf("Over frequency detected at time %.2f\n", t);
            over_frequency_count++;
            // Take appropriate action (e.g. shut down the inverter)
        }

      // Check for temperature
    temperature = readTemperature(); // Read temperature from a sensor
    if (temperature > MAX_TEMPERATURE) {
        printf("Temperature too high at time %.2f\n", t);
        // Take appropriate action (e.g. shut down the inverter)
    }

    // Check if output is a pure sine wave
    double THRESHOLD = 0.1; // The threshold for the difference between the output and the sine wave
    double sine_wave;
    sine_wave = amplitude * sin(2 * PI * frequency * t + phase);
    double difference = fabs(output - sine_wave);
    if (difference > THRESHOLD) {
        // adjust the sine wave by adding or subtracting the difference incrementally to the sine wave value until the difference is less than the threshold
        while (difference > THRESHOLD) {
            sine_wave += difference;
            difference = fabs(output - sine_wave);
        }
    }
    // Check for input source change
    if (input_source != previous_input_source) {
        printf("Input source changed from %d to %d at time %.2f\n", previous_input_source, input_source, t);
        sleep(delay); // Wait for the inverter to stabilize before switching
        previous_input_source = input_source;

    }
}

    pthread_join(monitor_thread, NULL);
    pthread_join(wifi_thread, NULL);
    printf("Over current events: %d\n", over_current_count);
    printf("Over voltage events: %d\n", over_voltage_count);
    printf("Over frequency events: %d\n", over_frequency_count);
    printf("Temperature: %d\n", temperature);
    printf("Mains voltage: %d\n", mains_voltage);
    printf("Battery voltage: %d\n", battery_voltage);
    printf("Battery level: %d%%\n", battery_level);
    printf("Input source: %d\n", input_source);
    return 0;
}
