#include <bits/stdc++.h>



int main()
{
    long test;
    std::cin >> test;
    for (long t=0;t<test;t++){
    long x,y,p1,p2;
    std::cin>>x>>y;
    std::string lin;
    vector <std::string> board;
    vectot <int> wynik;
    for(int i=0;i<y;i++){      
        std::cin>>lin;
        board.push_back(lin);
    }
    int a=0,b=0;
    while (a<x&&b<y){
        if (board[a][b]=='1'){
            
        }
        else a++;
        if (a>=y){
            a=0;
            b++;
        }
        
    }

    }
    return 0;
}

