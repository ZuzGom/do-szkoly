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
        p1 = b;
        b = c;
        c = p1;
    }

    while(x>=1){
    
        if(x<=0) break;
        else {
            cout<<"Wykonaj przeniesienie "<<a<<" - "<<c<<endl;
            --x;
        }
        if(x<=0)  break;
        else {
            cout<<"Wykonaj przeniesienie "<< a<<" - "<<b<<endl;;
            --x;
                }
        if(x<=0) break;
        else {
            cout<<"Wykonaj przeniesienie "<<c<<" - "<< b<<endl;
            --x;
            }
            
            
            
            
        if(x<=0)  break;
        else {
            cout<<"Wykonaj przeniesienie "<<a<<" - "<< c<<endl;
            --x;
        }
        
        
        
            
        if(x<=0)  break;
        else {
            cout<<"Wykonaj przeniesienie "<<b<<" - "<<a<<endl;
            --x;
        }
        if(x<=0)  break;
        else {
            cout<<"Wykonaj przeniesienie "<< b<<" - "<<c<<endl;;
            --x;
                }
        if(x<=0) break;
        else {
            cout<<"Wykonaj przeniesienie "<<a<<" - "<< c<<endl;
            --x;
            }
            
            
            
            
        if(x<=0)  break;
        else {
            cout<<"Wykonaj przeniesienie "<<c<<" - "<< a<<endl;
            --x;
        }
    }
    return 0;
}
