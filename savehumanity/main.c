
#include<stdio.h>

int main() {

    unsigned int i, j, k, num_cases, p_len, v_len, ptr, match, mismatch;
    char tmp;
    char patient [100001];
    char virus [100001];

    scanf ("%d\n",&num_cases);
    
    for(k=0; k<num_cases; ++k) {

        tmp = '\0';
        p_len = -1;
        while(tmp != '\n') {
            scanf("%c", &tmp);
            ++p_len;
            patient[p_len] = tmp;
        }
        patient[p_len] = '\0';

        tmp = '\0';
        v_len = -1;
        while(tmp != '\n') {
            scanf("%c", &tmp);
            ++v_len;
            virus[v_len] = tmp;
        }
        virus[v_len] = '\0';

        for(i=0; i <= p_len - v_len; ++i) {
            ptr = i;
            match = 1;
            mismatch = 1;
            for(j=0; j < v_len; ++j) {
                if(patient[ptr] != virus[j]) {
                    if(mismatch) {
                        --mismatch;
                    } else {
                        match = 0;
                        break;
                    }
                }
                ++ptr;;
            }
            if(match) printf("%u ", i);
        }

        printf("\n");

        if(k!=num_cases-1) scanf("\n");
    }

    return 0;
}

