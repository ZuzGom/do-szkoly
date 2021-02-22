#include <iostream>

using namespace std;

int main()
{
    unsigned int miasta;
    int zysk, z_miasta, max;

    cin >> miasta;
    zysk = 0;
    max = 0;

    for(int i=0; i<miasta; i++)
    {
        cin >> z_miasta;
        zysk += z_miasta;
        if (zysk<0)
            zysk =0;
        if (max < zysk)
            max = zysk;
    }

    cout << max;
    return 0;
}