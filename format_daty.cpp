#include <iostream>
#include <string>

using namespace std;


int main()
{
    string data;
    int n, y, m, d, check;
    cin>>n;
    
    string miesiac[12] = {"stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "wrzesnia", "pazdziernika", "listopada", "grudnia"};
    int dni[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    for (int i=0; i<n;i++)
    {
        check=0;
        cin>>data;
        if (data.length()!=8) cout<<"niepoprawny format daty"<<endl;
        else
        {
            for (int i=0; i<data.length(); i++)
            {
                if (data[i]-'0'>9 || data[i]-'0'<0)
                {
                    check++;
                    break;
                }
                  
            }
                
            if (check == 0)
            {
                d = (data[0]-'0')*10+data[1]-'0';
                m = (data[2]-'0')*10+data[3]-'0';
                y = (data[4]-'0')*1000+(data[5]-'0')*100 + (data[6]-'0')*10+data[7]-'0';
                if (m > 12 || d < 1 || m < 1 || 1000 > y|| y > 2200) cout<<"niepoprawny format daty"<<endl;
                else
                {
                    
                    if((y%4==0 && y%100!=0) || y%400==0)
                    {
                        dni[1] += 1;
                        if (dni[int(m - 1)] < d)
                            cout<<"niepoprawny format daty"<<endl;
                        else
                            cout<<d<<" "<<miesiac[m-1]<<" "<<y<<endl;
                        dni[1] -= 1;
                    }
                    else
                    {
                        if (dni[int(m - 1)] < d)
                            cout<<"niepoprawny format daty"<<endl;
                        else
                            cout<<d<<" "<<miesiac[m-1]<<" "<<y<<endl;
                    }
                }
                
            }
            
            else cout<<"niepoprawny format daty"<<endl;
        }
        
        
    }

    return 0;
}
