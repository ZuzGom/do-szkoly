/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <math.h>

using namespace std;
int main() 
{
    int ile = 3;
    int x, i=0;
    char a = 'A', b = 'B', c = 'C', p1, p2;
    cout<<"Podaj ilosc krazkow: ";
    cin>>ile;
    
    x = pow(2,ile) - 1;
 
    if (ile%2 == 1)
    {
        while (x>0){
        
        if (x%4==0) cout<<"Wykonaj przeniesienie "<<b<<" - "<<a<<endl;
        else cout<<"Wykonaj przeniesienie "<<a<<" - "<<b<<endl;
        x--;
        p1 = b;
        b = c;
        c = p1;
        if (x<1) break;
        if (x%4==0) cout<<"Wykonaj przeniesienie "<<b<<" - "<<a<<endl;
        else cout<<"Wykonaj przeniesienie "<<a<<" - "<<b<<endl;
        x--;
        
        p1 = c;
        c = a;
        a = p1;
        }
    }
    else
    {
        while (x>0){
        if (x%4==0) cout<<"Wykonaj przeniesienie "<<c<<" - "<<a<<endl;
        else cout<<"Wykonaj przeniesienie "<<a<<" - "<<c<<endl;
        x--;
        p1 = b;
        b = c;
        c = p1;
        
        if (x<1) break;
        if (x%4==0) cout<<"Wykonaj przeniesienie "<<c<<" - "<<a<<endl;
        else cout<<"Wykonaj przeniesienie "<<a<<" - "<<c<<endl;
        x--;
        p1 = b;
        b = a;
        a = p1;
        }
    }
    
    
    
    return 0;
}
