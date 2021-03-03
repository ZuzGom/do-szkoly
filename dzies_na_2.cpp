#include <iostream>
using namespace std;
int main() 
{
  int n,i=0;
  string tab="";
  cout<<"Podaj liczbę : ";
 cin>>n;
 while(n>0)
 {
   tab+=(n%2==0)?'0':'1';
   n=n/2;
   i++;
 }
for (int k=i-1;k>=0;k--)
  cout<<tab[k];

return 0;
}
