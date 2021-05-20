
#include <bits/stdc++.h>

class Ksiazki
{
public:
    std::string tytul, autor;
    int ilosc_stron;

    Ksiazki(std::string atytul, std::string aautor, int ailosc_stron){
     tytul = atytul;
     autor =aautor;
     ilosc_stron=ailosc_stron;
    };



};

int main()
{
    int n;
    std::cin>>n;
    std::string tytul, autor;
    int ilosc_stron;
    std::vector<Ksiazki*> biblioteka;
for (int i=0;i<n;i++){
    std::cin>>tytul;
    std::cin>>autor;
    std::cin>>ilosc_stron;
Ksiazki *temp = new Ksiazki(tytul,autor,ilosc_stron);
biblioteka.push_back(temp);
}
printf("%i",biblioteka[0]->ilosc_stron);
    return 0;
}
