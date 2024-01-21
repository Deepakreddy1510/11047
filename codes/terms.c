#include <stdio.h>

int main() {
    // Define the range
    int start_n = -2;
    int end_n = 12;

    // Calculate the values of x and y
    FILE *file = fopen("data.txt", "w");

    if (file != NULL) {
        for (int n = start_n; n <= end_n; n++) {
            double x = n;
            double y = (2 * x - 3) / 6;

            // Write x and y to the file
            fprintf(file, "%lf %lf\n", x, y);
        }

        // Close the file
        fclose(file);
    } else {
        printf("Error opening the file.\n");
    }

    return 0;
}
