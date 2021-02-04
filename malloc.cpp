#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    int c, n;
    float suma = 0;
	int *ptr;
	cout<<"Ile ocen: ";
    cin>> n;
    ptr = (int*) malloc(n+1);
	if(!ptr)
		exit(1);

	cout << "Prosze podac: " << endl;

	for (int i=0; i<n; i++)
	    cin >>ptr[i];
	
	cout << "Średnia" << endl;
	for (int i=0; i<n; i++)
		suma += *(ptr+i);
    cout<<1.0*suma/n<<endl;

	free(ptr);
	return 0;
}
