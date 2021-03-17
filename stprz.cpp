#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float liczba, suma = 0; 
    int b=0;
    cout<<"Liczba: ";
    cin>>liczba;
    do{
        cout<<"Liczba bitow (ale dobra): ";
        cin>>b;
    }
    while (pow(2,(b/2 - 1))<=liczba);
    int p = b/2 - 1;
    float wg[b];
    for (int i=0;i<b;i++){
        wg[i]=pow(2,p);
        p -= 1;
        //cout<<wg[i]<<endl;
    }
    string wynik="";
    for (int i =0;i<b;i++){
        if (suma + wg[i]<=liczba){
            suma += wg[i];
            wynik += '1';
        }else wynik += '0';
    }
    cout<<wynik;
    return 0;

}