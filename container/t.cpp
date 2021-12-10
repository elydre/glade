// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
int main()
{
    long int max;  // auto var
    long int f;  // auto var
    string m;  // auto var
    string m1;  // auto var
    string m2;  // auto var
    string m3;  // auto var
    long int ia;  // auto var
    long int ajout;  // auto var
    string caractere;  // auto var
    string code;  // auto var
    string n1;  // auto var
    string n2;  // auto var
    string n3;  // auto var
    max = 11;
    f = 0;
    cout << "" << endl;
    cout << "~} ";
    cin >> m;
    cin.ignore();
    try
    {
        long int m1[] = {0};
    }
    catch(...)
    {
        m1 = ' ';
    }
    try
    {
        long int m2[] = {1};
    }
    catch(...)
    {
        m2 = ' ';
    }
    try
    {
        long int m3[] = {2};
    }
    catch(...)
    {
        m3 = ' ';
    }
    f = 1;
    for (long int idd = 0 ; idd < 6 ; idd = idd  + 1)
    {
        for (long int ida = 0 ; ida < 6 ; ida = ida  + 1)
        {
            ia = ida;
            ajout = idd;
            caractere = m1;
            code = caractere;
            code = ajout + ajout;
            n1 = code;
            ajout = ia;
            ajout = min(ajout, max);
            caractere = m2;
            code = caractere;
            n2 = code;
            ajout = ia;
            ajout = min(ajout, max);
            caractere = m3;
            code = caractere;
            n3 = code;
            ajout = ia;
            ajout = min(ajout, max);
            cout << f << "";
            cout << ":" << "idd=" << idd << "ida=" << ia << n1 << "";
            cout << n2 << "";
            cout << n3 << endl;
        }
    }
}
