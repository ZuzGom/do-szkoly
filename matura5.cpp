#include <bits/stdc++.h>
#include <fstream>
#include <string>
using namespace std;

string buildPalindrome(string st) {

int e =st.length()-1,i=0;
while (i<st.length()-1){
    if (st[i]==st[e]) i++;
    else e = st.length()-1;      
    e--; 
}
if (st[st.length()-1]==st[st.length()-3]&&e>st.length()-3) e = st.length()-3;
cout<<e;
e--;
while (e>=0){
    st+=st[e];
    e--;
}
return st;

}
int main()
{
    cout<<buildPalindrome("kominiain");
    
    return 0;
}
