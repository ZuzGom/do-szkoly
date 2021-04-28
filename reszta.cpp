
#include <iostream>


void is_are(int n, int b){
    printf("\nW sumie ");
    if (n==1) printf("jest 1 moneta i ");
    else if (n<5&&n>1) printf("s\245 %i monety i ",n);
    else printf("jest %i monet i ",n);
    
    if (b==1) printf("1 banknot");
    else if (b<5&&b>1) printf("%i banknoty",n);
    else printf("%i banknot\242w",b);
}

void printuj(int n, float m){
    
    if (m>5){
    if (n==1) printf("Jest %i banknot %g z\210otowy\n",n,m);
    else if (n<5&&n>1) printf("S\245 %i banknoty %g z\210otowe\n",n,m);
    else printf("Jest %i banknot\242w %g z\210otowych\n",n,m);
    }
    else if (m < 1){
        if (n==1) printf("Jest %i moneta %g groszowa\n",n,m*100);
    else if (n<5&&n>1) printf("S\245 %i monety %g groszowe\n",n,m*100);
    else printf("Jest %i monet %g groszowych\n",n,m*100);
    }
    else{
    if (n==1) printf("Jest %i moneta %g z\210otowa\n",n,m);
    else if (n<5&&n>1) printf("S\245 %i monety %g z\210otowe\n",n,m);
    else printf("Jest %i monet %g z\210otowych\n",n,m);
    }
}


int main()
{
    float wejscie;
    const float monety[18]={50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 500, 200, 100, 50, 20, 10, 5, 2, 1};
    int nomi[18]={0};
    int liczba_monet=0, liczba_banknotow=0, reszta;


    printf("Podaj cen\251: ");
    scanf("%g",&wejscie);
    wejscie*=100;
    reszta=int(wejscie);

    while(reszta>0){
        for (int i=0;i<18;i++){
            if((reszta-monety[i])>=0){
            reszta-=monety[i];
            nomi[i]+=1;
            if (i>5) liczba_banknotow++;
            else liczba_monet++;
            break;
            }
        }
        }
    for (int i=0;i<18;i++) printuj(nomi[i],monety[i]/100);
    //for (int i=6;i<18;i++) printf("Jest %i monet %g zlotowych\n",nomi[i],monety[i]/100);
    is_are(liczba_monet, liczba_banknotow);

    //std::cin.get();
    //std::cin.get();
    return 0;
}
