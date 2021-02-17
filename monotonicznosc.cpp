#include <iostream>
using namespace std;


string check(string liczby){
    
    int a = liczby[0], b = liczby[2];
    
    if (a<b){
        for (int i = 4; i < liczby.length(); i += 2)
        {
            a = liczby[i];
            if (a < b)
                return "Zadna z nich";
            b = a;
        }
        return "Rosnaca";
    }
    if (a>b){
        for (int i = 4; i < liczby.length(); i += 2)
        {
            a = liczby[i];
            if (a > b)
                return "Zadna z nich";
            b = a;
        }
        return "Malejaca";
    }
    if (a==b){
        for (int i = 4; i < liczby.length(); i += 2)
        {
            a = liczby[i];
            if (a != b)
                return "Zadna z nich";
            b = a;
        }
        return "Stala";
    }
    
}


int main()
{
    string liczby;
    
    getline(cin, liczby);
    
    cout<<check(liczby);
    

    return 0;
}
