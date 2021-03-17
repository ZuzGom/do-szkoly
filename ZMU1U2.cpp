#include <iostream>

std::string DecToBin(int, int);

std::string Negacja(std::string);

std::string ZmToU2(std::string);

void wypisz(std::string, std::string, std::string);

int main()
{
    std::string liczba_binarnie, u1, u2;

    int liczba;
    std::cout << "Podaj liczbe: \n";
    std::cin >> liczba;

    int bity;
    std::cout << "Podaj ilosc bitow: \n";
    std::cin >> bity;
    
    liczba_binarnie = DecToBin(liczba, bity);
    
   if (liczba_binarnie[0] == '0')
        wypisz(liczba_binarnie, liczba_binarnie, liczba_binarnie);
   else {

       u1 = Negacja(liczba_binarnie);
       u2 = ZmToU2(liczba_binarnie);
       std::cout <<liczba_binarnie<<" "<< u1 <<" "<< u2 << std::endl;

   }



}

void wypisz(std::string zm, std::string u1, std::string u2) {

    std::cout << "Liczba w ZM: " << zm << std::endl;
    std::cout << "Liczba w U1: " << u1 << std::endl;
    std::cout << "Liczba w U2: " << u2 << std::endl;

}

std::string DecToBin(int liczba, int bity) {

    bool bitZnaku=0;

    if (liczba < 0) {
        bitZnaku = 1;
        liczba *= -1;
    }

    std::string wynik="";

    wynik += bitZnaku+'0';

    for (int i = 0; i < bity-1; i++)
        wynik += '0';

    int pozycja=bity-1;
    while (liczba > 0) {

        if (pozycja < 1) {
            return "Za mala ilosc bitow!";
        }

        if (liczba % 2 != 0) 
            wynik[pozycja] = '1';

        liczba /= 2;
        pozycja--;
    }
    
    return wynik;
}

std::string Negacja(std::string liczba) {
    
    for (int i = 1; i < liczba.size(); i++) {

        if (liczba[i] == '0')
            liczba[i] = '1';
        else
            liczba[i] = '0';
    }
    return liczba;
}

std::string ZmToU2(std::string liczba) {

    std::string wynik;
    int pozycja = liczba.size();

    while (liczba[--pozycja] != '1');
    
    std::cout << pozycja << std::endl;

    wynik += liczba[0];

    for (int i = 1; i < liczba.size(); i++) {

        if (i < pozycja) {
            if (liczba[i] == '0')
                wynik += '1';
            else
                wynik += '0';
        }
        else
            wynik += liczba[i];
    }
    return wynik;
}