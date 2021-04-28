#include <bits/stdc++.h>

int polis(int a, int b){
    int polis;
    if (a > b){
        polis += b;
        polis += a - b;
    }
    return polis;
}

int main()
{
    long test;
    std::cin >> test;
    for (long t=0;t<test;t++){
    long m,n,x,y,a,b;
    std::cin>>n>>m;
    std::cin>>x>>y;
    std::cin>>a>>b;
    int th = n - x + m - y;
    int polis = (a>b)?a:b;
    int poc;
    if((n-a)-(m-b)<0)
        poc=0;
    else
        poc=(n-a)-(m-b);
        
    int polic = poc + (m-b);

    
    if (polic<th) std::cout<<"NO"<<std::endl;
    else std::cout<<"YES"<<std::endl;
    }
    return 0;
}

