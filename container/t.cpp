// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
int main()
{
    string test;  // auto var
    cin >> test;
    cin.ignore();
    if (test == "coucou")
    {
        cout << "input == coucou" << endl;
    }
    else
    {
        cout << "input != coucou" << endl;
    }
}