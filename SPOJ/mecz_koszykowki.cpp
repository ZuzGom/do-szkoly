#include <iostream>

int main()
{
    int tab[26]={1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757};
    
    //for (int i=3; i<25;i++)
    //    tab[i]=tab[i-1]+tab[i-2]+tab[i-3];
    int n;
    int p1,p2,p3,p4;
    long long m;
    
    std::cin>>n;
    for (int i=0;i<n;i++)
    {
        m=1;
        std::cin>>p1>>p2>>p3>>p4;
        m = (m*tab[p1]) % 1000000007;
        m = (m*tab[p2]) % 1000000007;
        m = (m*tab[p3]) % 1000000007;
        m = (m*tab[p4]) % 1000000007;
        std::cout<<m<<std::endl;
    }

    return 0;
}
