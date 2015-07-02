
#include<stdio.h>

int main(int argc, char * argv[]){

    unsigned int num_cases;
    scanf("%u\n", &num_cases);

    unsigned int i;
    for(i=0; i<num_cases; ++i){
        unsigned int foo;
        scanf("%u\n", &foo);
        printf("%u\n", ~foo);
    }

    return 0;
}

