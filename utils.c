
#include "utils.h"

// Newton's square root approximation
double sqrt_tol_guess(double number, double tolerance, double x) {
    double xp;
    while(1) {
        xp = 0.5 * ( x + number / x );
        if(xp > x && xp - x < tolerance) {
            return xp;
        } else if (x > xp && x - xp < tolerance) {
            return xp;
        }
    }
}

double sqrt_tol(double number, double tolerance) {
    return sqrt_tol_guess(number, tolerance, 1);
}

double sqrt(double number) {
    return sqrt_tol_guess(number, 0.0001, 1);
}

