
#include <iostream>
#include <cmath>

float f(float x){
    return 6.67*pow(10,-11)*6*pow(10,24)*4725/pow(x,2);
}
float przy(float x){
    x = (x<0)?-x:x;
    return x;
}
int main()
{
    float beg, end, d=0.1, suma = 0.0;
    printf("Poczatek i koniec przedzialu oraz przyblizenie: \n");
    scanf("%g %g %g", &beg, &end, &d);
    int i = 0;
    while (beg + d*i <= end){
        suma+=przy(0.5*(f(beg + d*i) + f(beg + d*(i+1)))*d);
        i++;
    }
    printf("Wynik: %g\n", suma);
    //Wynik: 1.43538e+10
    return 0;
}
