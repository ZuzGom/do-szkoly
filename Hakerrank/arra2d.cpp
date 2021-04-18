#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int maxi = 0;
    int suma = 0;
    for (int x = 0; x <= arr.size()-3; x++){
        for (int y = 0; y <= arr[x].size()-3; y++){
            suma = arr[x][y] + arr[x][y+1] + arr[x][y+2]; 
            suma += arr[x+1][y+1];
            suma += arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2];
            if (suma >= maxi) maxi = suma;
            
        }
    }    
    return maxi;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
