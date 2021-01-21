#include <iostream>

using namespace std;


int main()
{
    int m;
    int wynik1=1;
    int wynik2=1;
    int wynik=1;

    cout << "Podaj ilosc miesiecy: ";
    cin >> m;

    int i=m;
    while (i>1&&m>2)
    {
        wynik = wynik2 + wynik1;
        wynik2 = wynik1;
        wynik1 = wynik;
        i--;

    }

    cout<<wynik;

    return 0;
}
