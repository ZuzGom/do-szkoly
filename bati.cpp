#include <iostream>

int main()
{
    int i=0;
    float a, p, E, L, roz;

    scanf("%g %g %g",&p,&E,&L);

    a=p;
    roz=(a-p/a<0)?a-p/-a:a-p/a;

    while(roz>E && i<L)
    {
        a=(a+p/a)/2;
        roz=(a-p/a<0)?a-p/-a:a-p/a;
        i++;
    }

    printf("Oto pierwiastek: %g",a);

    return 0;
}