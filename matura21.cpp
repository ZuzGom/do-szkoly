#include <bits/stdc++.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
    vector<int> kubel(26,0);
    string wynik ="";
    fstream input;
    int max=0,licz=0;
    char last=' ';
    input.open("instrukcje.txt");
    while (!input.eof()){
        string akcja;
        char litera;

        getline(input,akcja);
        //input>>akcja>>litera;
        
        litera = akcja[akcja.length()-2];
        
        if (litera!='1') kubel[litera-'A']++;
        if (akcja[0]==last) licz++;
        else licz =0;
        if (licz>max)max=licz;
        last=akcja[0];
        switch (akcja[0]){
        case 'D':
            //cout<<wynik<<endl;
            wynik+=litera;
            break;
        case 'Z':
            wynik[wynik.length()-1]=litera;
            break;
        case 'U':
            wynik.pop_back();
            break;
        case 'P':
            for (char &ch:wynik){
                if (ch==litera){
                    if ((int)ch==90) ch='A';
                    else ch++;
                    break;
                }
            }
            break;

        }
        

    }
    int maxi=0;
    int j=0;
    for (int i=0;i<26;i++){
        //cout<<kubel[i]<<endl;
        if(kubel[i]>maxi){
            maxi=kubel[i];
            j=i;
        }
    } 
    
    cout <<"4.1 " <<wynik.length() << endl;
    cout <<"4.2 " << max+1 << endl;
    cout <<"4.3 " << (char)(j+'A') << endl;
    cout <<"4.4 " << wynik << endl;
    return 0;
}
