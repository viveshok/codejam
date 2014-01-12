
#include<stdio.h>
#include<string.h>

int main(int argc, char * argv[]){
    if(argc != 2){
        printf( "    usage: %s filename\n\n", argv[0] );
    } else {
        FILE * fp = fopen(argv[1], "r");
        int num_cases;
        fscanf(fp, "%d\n", &num_cases);

        int i;
        for(i=0; i<num_cases; ++i){
            char input1[10];
            char input2[10];
            fscanf(fp, "%s\n%s\n\n", input1, input2);
            printf("input 1: %s\ninput 2: %s\n\n", input1, input2);
        }

        fclose(fp);
    }
}

