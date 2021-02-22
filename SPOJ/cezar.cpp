#include <iostream>
using namespace std;

bool cezar(string napis){
    //char alfa[32] ={'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż'}
    string fraktal = "FRAKTAL";
    int a = napis[0], b = fraktal[0];
    int c = a - b;
    if (napis.length()!=fraktal.length()) return false;
    for (int i = 1; i < napis.length(); i++)
        {
            a = napis[i];
            b = fraktal[i];
            if (a<65||a>90) return false;
            if (a - b != c)
                return false;
        }
        return true;
}


int main()
{
    int c = 164;
    char ch = c;
    cout<<ch<<endl;
    int t;
    string test;
    
    cin>>t;
    for (int i=0; i<t; i++){
        cin>>test;
        if (cezar(test)) cout<<"tak"<<endl;
        else cout<<"nie"<<endl;

    }

    return 0;
}
