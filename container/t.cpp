// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
int main()
{
    long int a;  // auto var
    cout << "entrez un nombre:";
    cin >> a;
    cin.ignore();
    for (long int x = 0; x < a; x = x + 1)
    {
        cout << "Boujour!" << endl;
    }
}
