
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    string liczba;
    float mantysa=0,wgf[23];
    int cecha=0, wgint[8], suma,b;
    cout<<"Podaj liczbe IEEE754: "<<endl;
    cin>>liczba;
    b = liczba[0]-'0';
    
    for(int i=0;i<8;i++) wgint[i]=pow(2,7-i);
    
    for(int i=0;i<4;i++) wgf[i]=pow(2,-i-1);
    
    for (int i=1;i<9;i++) if (liczba[i]=='1') cecha += wgint[i-1];
    
    for (int i=9;i<24;i++) if (liczba[i]=='1') mantysa += wgf[i-9];
    
    cout<<pow(1,b)*(1+mantysa)*pow(2,cecha-127);
    return 0;
}
