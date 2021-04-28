#include<iostream>
#include<algorithm>
#include<string>

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


int main(){

    int cases;
    std::cin>>cases;

    for(int q=0; q<cases; q++){

    int size;
    std::cin>>size;

    int *tab = new int[size];

    int read;
    for(int i=0; i<size; i++){

        std::cin>>read;
        tab[i]=read;

    }

    std::qsort(tab,size,sizeof(int), compare);

    int pom;
    pom=tab[0];
    std::cout<<tab[0]<<" ";
    std::string a="";
    for(int i=1; i<size; i++){

        if(tab[i]==pom){
           a+=std::to_string(tab[i])+" ";
            continue;
        }
        else{
            pom=tab[i];
            std::cout<<tab[i]<<" ";
        }
    }std::cout<<a<<std::endl;
    delete[] tab;
    }
}
