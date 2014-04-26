
#include <stdio.h>
#include <stdlib.h>
 
#define MODULO 1000000007

int main()
{
    int i, j, k, N, hMax = 0, wMax = 0;
 
    scanf("%i\n", &N);

    int * vH = (int *) malloc(N*sizeof(int));
    int * vW = (int *) malloc(N*sizeof(int));
 
    for(i = 0; i < N; ++i){
        scanf("%i %i\n", &vH[i], &vW[i]);

        if(vH[i] > hMax)
            hMax = vH[i];
 
        if(vW[i] > wMax)
            wMax = vW[i];
    }

    if(hMax < 4)
        hMax = 4;
    if(wMax < 4)
        wMax = 4;
 
    int * rNumb = (int *) malloc((wMax+1) * sizeof(int));

    int ** rNumbPwh = (int **) malloc((hMax+1) * sizeof(int *));
    for(i=0; i<=hMax; ++i)
        rNumbPwh[i] = (int *) malloc((wMax+1) * sizeof(int));

    int ** rt = (int **) malloc((hMax+1) * sizeof(int *));
    for(i=0; i<=hMax; ++i)
        rt[i] = (int *) malloc((wMax+1) * sizeof(int *));

    int * hNumb = (int *) malloc((hMax+1) * sizeof(int));
 
    for(i = 0; i < N; ++i)
         hNumb[vH[i]] = ( vW[i]>hNumb[vH[i]] ? vW[i] : hNumb[vH[i]] );
    
    rNumb[0] = 1;
    rNumb[1] = 1;
    rNumb[2] = 2;
    rNumb[3] = 4;
    rNumb[4] = 8;
 
    for(i = 5; i <= wMax; ++i){
        rNumb[i] += rNumb[i-4];
        rNumb[i] %= MODULO;
        rNumb[i] += rNumb[i-3];
        rNumb[i] %= MODULO;
        rNumb[i] += rNumb[i-2];
        rNumb[i] %= MODULO;
        rNumb[i] += rNumb[i-1];
        rNumb[i] %= MODULO;
    }
 
    for(i = 1; i <= wMax; ++i){
        long long rNumbTimes = rNumb[i];
        for(j = 1; j <= hMax; ++j){
            rNumbPwh[j][i] = rNumbTimes;
            rNumbTimes *= rNumb[i];
            rNumbTimes %= MODULO;
        }
    }

    free(rNumb);
 
    rt[1][1] = 1;
    rt[1][2] = 1;
    rt[1][3] = 1;
    rt[1][4] = 1;
 
    for(i = 2; i <= hMax; ++i)
        rt[i][1] = 1;
 
    for(j = 2; j <= hMax; ++j){
        for(i = 2; i <= hNumb[j]; ++i){
            long long rTemp = rNumbPwh[j][i];
            for(k = 1; k < i; ++k){
                long long rTemp2 = ((long long) rt[j][k]) * ((long long) rNumbPwh[j][i-k]);
                rTemp2 %= MODULO;
 
                if(rTemp2 > rTemp)
                    rTemp = rTemp + 1000000007 - rTemp2;
                else
                    rTemp -= rTemp2;
            }
            rt[j][i] = rTemp;
        }
    }
 
    free(hNumb);

    for(i = 0; i < N; ++i)
//        printf("N: %i, M: %i, result: %i\n", vH[i], vW[i], rt[vH[i]][vW[i]]);
        printf("%i\n", rt[vH[i]][vW[i]]);
 
    free(vH);
    free(vW);

    for(i = 0; i<=hMax; ++i){
        free(rNumbPwh[i]);
        free(rt[i]);
    }

    free(rNumbPwh);
    free(rt);

    return 0;
}

