#include <bits/stdc++.h>
using namespace std;

string buildPalindrome(string st) {
int e =st.length()-1,i=0;
while (e>=0){
    if (st[i]==st[e]) i++;
    else i=0;      
    e--; 
}
string wyn="";
int j = st.length() -1;
while (j>=i){
    wyn+=st[j];
    j--;
}
st=wyn+st;
return st;
}

int main()
{
    cout<<"5.1"<<endl;
    int suma=0,ma=0,mi=0;
    string maxi,mini;
    fstream input;
    input.open("slowa.txt");
    while (!input.eof()){
    string wyraz,wynik;
    input>>wyraz;
    wynik=buildPalindrome(wyraz);
    int l= wynik.length();
    if(mi==0)mi=l;
    if (l==12) cout<<wynik<<endl;
    suma+=l;
    if (l>ma){
        ma=l;
        maxi=wynik;
    }
    if(l<mi){
        mi=l;
        mini=wynik;
    }
    }
    cout<<"5.2"<<endl;
    cout<<maxi<<endl;
    cout<<mini<<endl;
    cout<<"5.3"<<endl;
    cout<<suma<<endl;
    return 0;
}
/*wynik
5.1
BDJBFBBFBJDB
DFDAHEEHADFD
IHBIBCCBIBHI
FABBEAAEBBAF
5.2
AJBEIKKFIIGIIJBAHADIBCIDHDICBIDAHABJIIGIIFKKIEBJA
OKOOKO
5.3
27751*/
