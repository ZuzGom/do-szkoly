#include <iostream>
#include <string>

using namespace std;


int main()
{
    string data;
    int n, y, m, d, check;
    cin>>n;
    
    string miesiac = {"stycznia", "lutego", "marca",
               "kwietnia", "maja", "czerwca",
               "lipca", "sierpnia", "wrzesnia",
               "pazdziernika", "listopada", "grudnia"}
    int dni = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    
    for (int i=0; i<n;i++)
    {
        check=0;
        cin>>data;
        if (data.length()!=8) cout<<"niepoprawny format daty"<<endl;
        else
        {
            for (int i=0; i<data.length(); i++)
            {
                if (data[i]-'0'>9 || data[i]-'0'<1)
                {
                    //cout<<i<<endl;
                    //cout<<data[i]-'0'<<endl;
                    check++;
                    break;
                }
                  
            }
                
            if (check == 0)
            {
                d = (data[0]-'0')*10+data[1]-'0';
                m = (data[2]-'0')*10+data[3]-'0';
                y = (data[4]-'0')*1000+(data[5]-'0')*100 + (data[6]-'0')*10+data[7]-'0';
                cout<<d<<endl<<m<<endl<<y;
                if (m > 12 || d < 1 || m < 1 || 1000 > rok|| rok > 2200) cout<<"niepoprawny format daty"<<endl;
                else
                {
                    if((rok%4==0 && rok%100!=0) || rok%400==0)
                    {
                        dni[1] += 1
                        if (dni[int(m - 1)] < d)
                            cout<<"niepoprawny format daty"<<endl;
                        else:
                            cout<<d<<" "<<miesiac[m-1]<<" "<<rok<<endl;
                        dni[1] -= 1
                    }
                    else
                    {
                        if (dni[int(m - 1)] < d)
                            cout<<"niepoprawny format daty"<<endl;
                        else:
                            cout<<d<<" "<<miesiac[m-1]<<" "<<rok<<endl;
                    }
                }
                
            }
            
            else cout<<"niepoprawny format daty"<<endl;
        }
        
        
    }

    return 0;
}
