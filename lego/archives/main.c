
#include <stdio.h>
#include <stdlib.h>

#define MODULO 1000000007

unsigned int powmod(unsigned int b, unsigned int e, unsigned int m){

    int remainder;
    int x = 1;

    while (e != 0){
        remainder = e % 2;
        e /= 2;

        if (remainder == 1)
            x = (x * b) % m;

        b = (b * b) % m; // New base equal b^2 % m
    }
    return x;
}

void single_layer(unsigned int * sl) {

    sl[1] = 1;
    sl[2] = 2;
    sl[3] = 4;
    sl[4] = 8;

    int i;
    for(i=5; i<1001; ++i)
        sl[i] = (sl[i-4] + sl[i-3] + sl[i-2] + sl[i-1])%MODULO;
}

int main(){

    unsigned int i, j, n, N, height, width, soft_walls;
    unsigned int * sl = (unsigned int*) malloc(1001 * sizeof(unsigned int));
    unsigned int * solid_walls = (unsigned int*) malloc(1001 * sizeof(unsigned int));
    solid_walls[1] = 1;

    single_layer(sl);

//    printf("powmod(2,3,888888) = %u, powmod(3,3,99999) = %u\n", powmod(2,3,99999), powmod(3,3,99999));
    scanf("%u\n", &N);

    for(n = 0; n<N;++n) {
        scanf("%u %u\n", &height, &width);

        for(i = 2; i<=width; ++i){
            soft_walls = 0;
            for(j = 1; j < i; ++j) {
                soft_walls += solid_walls[j]%MODULO * powmod(sl[i-j], height, MODULO);
                soft_walls %= MODULO;
            }
            solid_walls[i] = (powmod(sl[i], height, MODULO) - soft_walls)%MODULO;
        }

        printf("N: %u, M: %u, result: %u\n", height, width, solid_walls[width]);
    }

    free(sl);
    free(solid_walls);
    return 0;
}

