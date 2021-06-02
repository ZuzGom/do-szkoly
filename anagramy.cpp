#include <bits/stdc++.h>

bool czy_ana(std::string s1, std::string s2){
    sort(s1.begin(),s1.end());
    sort(s2.begin(),s2.end());
    if (s1==s2) return true;
    return false;
}

int main()
{
    std::string s1, s2;
    scanf("%s", &s1[0]);
    scanf("%s", &s2[0]);
    if (czy_ana(s1,s2)) printf("to anagramy");
    else printf("to nie anagramy");
    return 0;
}
