c
    #include <stdio.h>
    #include <omp.h>

    int main() {
        int i;
        int a[100], b[100], c[100];

        // Initialize arrays
        for (i = 0; i < 100; i++) {
            a[i] = i;
            b[i] = 100 - i;
        }

        // Parallel region: divides the loop iterations among available threads
        #pragma omp parallel for
        for (i = 0; i < 100; i++) {
            c[i] = a[i] + b[i];
        }

        printf("c[0] = %d, c[99] = %d\n", c[0], c[99]);
        return 0;
    }