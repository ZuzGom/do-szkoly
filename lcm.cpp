#include<iostream>


using namespace std;
int NWD(int a, int b)
{
    while(a!=b)
       if(a>b)
           a-=b; //lub a = a - b;
       else
           b-=a; //lub b = b-a
    return a; // lub b - obie zmienne przechowują wynik NWD(a,b)
}
int main(){
    int  k, t;
    float n;
    bool a = true;
    cin>>t;
    for (int i=0; i < t;i++){
        cin>>n>>k;
        int tab[3]={n-k+1,1,1};
        while (true){
            int lcm = 1;
            if (tab[0] == 0) break;
            for (int i =0; i<k;i++){
                if (tab[i] != 0) lcm = lcm*tab[i]/NWD(lcm,tab[i]);
            } 
            if (lcm <= n/2) break;
            
            if (a == true){
                tab[0] --;
                tab[1] ++;
            }
            else{
                tab[0] --;
                tab[2] ++;
            }
        a = !a;
        }
        for (int i =0; i<k;i++){
            cout<<tab[i]<<" ";
        }
        cout<<endl;;
    }
    return 0;
}