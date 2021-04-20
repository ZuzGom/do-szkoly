#include <iostream>
#include <cmath>
float f(float x){
    return x*x + 4;
}
using namespace std;
int main()
{
    float p, k, d, pole = 0.0;
    cout<<"Podaj poczatek: ";
    cin>>p;
    cout<<"Podaj koniec: ";
    cin>>k;
    cout<<"Podaj przyblizenie: ";
    cin>>d;
    int i = 0;
    while (p + d*i < k){
        pole+=abs(0.5*(f(p + d*i) + f(p + d*(i+1)))*d);
        i++;
    }
    cout<<"Wynik: "<<pole<<endl;

    return 0;
}
