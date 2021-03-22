
#include <iostream>
#include <cmath>

int main()
{
    char liczba[32];
    float mantysa=0, wgf[23];
    int cecha=0, wgint[8],b;
    printf("%s\n","Podaj liczbe IEEE754: ");
    scanf("%31s", liczba);
    b = liczba[0]-'0';

    
    for(int i=0;i<8;i++) wgint[i]=pow(2,7-i);
    
    for(int i=0;i<24;i++) wgf[i]=pow(2,-i-1);
    
    for (int i=1;i<9;i++) if (liczba[i]=='1') cecha += wgint[i-1];
    
    for (int i=9;i<32;i++) if (liczba[i]=='1') mantysa += wgf[i-9];
  

    printf("%s\n","Liczba w dziesietnym:");
    if (cecha==255 && mantysa==0 && b==0) printf("%s\n", "inf");
    else if (cecha==255 && mantysa==0 && b==1) printf("%s\n", "-inf");
    else if (cecha==0 && mantysa==0) printf("%s\n","0");
    else if (cecha==0 && mantysa!=0) printf("%s\n", "Liczba nienormalna");
    else if (cecha==255 && mantysa!=0) printf("%s\n", "Liczba to nawet nie jest ona");
    else printf("%g\n", pow(-1,b)*(1+mantysa)*pow(2,cecha-127));
    return 0;
}
