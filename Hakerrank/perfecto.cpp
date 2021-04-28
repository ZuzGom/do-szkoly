#include <bits/stdc++.h>
#include <cmath>
using namespace std;

vector<string> split_string(string);


vector<int> dziel(int a){
    vector<int> D;
    for (int i=1;i<=a;i++) if (a%i==0) D.push_back(i);
    return D;
}
vector<int> rozk(int a){
    int k =2;
    vector<int> R;
    float p = sqrt(a);
    while (a>1&&k<=p){
        while (a%k==0){
            R.push_back(k);
            a/=k;
            }
        ++k;
    }
    return R;
}
// Complete the reverseArray function below.
string Perfect(vector<int> a, int n) {
    vector<long long int> ilo(n);
    int back = 1;
    for (int i=0; i<n;i++) {
        ilo[i]=back*a[i];
        //cout<<ilo[i]<<endl;
        vector<int> dz = dziel(a[i]);
        if (a[i]/dz[dz.size()/2]!=dz[dz.size()/2]) {
            return "YES";
        }
        vector<int> dz2 = dziel(ilo[i]);
        if (ilo[i]/dz2[dz2.size()/2]!=dz2[dz2.size()/2]) {
            return "YES";
        }
        back = ilo[i];
    }
    
    return "NO";
    
}

int main()
{
    vector<int> d = rozk(36);
    for (int i = 0; i < d.size(); i++) {
        cout << d[i];

        if (i != d.size() - 1) {
            cout << " ";
        }
    }
    cout<<"\n";
    int test;
    cin >> test;
    for (int t=0;t<test;t++){

    int arr_count;
    cin >> arr_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);
    //cout<<"go"<<endl;
    
    vector<int> arr(arr_count);

    for (int i = 0; i < arr_count; i++) {
        int arr_item = stoi(arr_temp[i]);
        arr[i] = arr_item;

    }

    string wyn = Perfect(arr, arr_count);

    cout << wyn << endl;
    }
    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
