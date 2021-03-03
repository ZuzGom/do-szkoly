#include <iostream>

using namespace std;

int main()
{
    int miasta;
    long zysk, z_miasta, max;

    scanf("%i", &miasta);
    zysk = 0;
    max = 0;

    for(int i=0; i<miasta; i++)
    {
        scanf("%ld", &z_miasta);
        zysk += z_miasta;
        if (zysk<0)
            zysk =0;
        if (max < zysk)
            max = zysk;
    }

    printf("%ld", max);
    return 0;
}
