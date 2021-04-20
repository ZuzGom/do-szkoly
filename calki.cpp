#UWAGA NIEGRZECZNY KOD
#include <iostream>

float f(float x){
    return 2*x + 8;
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

    return 0;
}
