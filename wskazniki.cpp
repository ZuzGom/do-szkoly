#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int losuj(int &a, int &b)
{
    srand(time(NULL));
    if (a<b)
        return a+rand()%(a-b-1);
    else
        return b+rand()%(b-a-1);
}
long silnia(int a) //rekurencja
{
    long s=1;
    if (a==0||a==1)
        return 1;
    else 
        s*=silnia(a-1)*a;
    return s;
}
float w(int &x, int &y)
{
    int mianownik=0;
    for(int i=1; i<=y;i++)
        mianownik+=i;
    return 1.0*(silnia(x)+silnia(y))/mianownik;
}
int main()
{
    int a,b,x,y;
    cout<<"podaj granice przedzialu: ";
    cin>>a>>b;
    x=losuj(a,b);
    do
    {
        cout << "Podaj naturalne y: ";
        cin>>y;
    }while(y<0);
    
    cout<<w(x,y);
    return 0;
}
