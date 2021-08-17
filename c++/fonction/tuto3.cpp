#include <iostream>
using namespace std;

int ajouteDeux(int nombreRecu)
{
    int valeur(nombreRecu + 2);

    return valeur;
}

int main()
{
    int a(2),b(2);
    cout << "Valeur de a : " << a << endl;
    cout << "Valeur de b : " << b << endl;
    b = ajouteDeux(b); //Appel de la fonction
    cout << "Valeur de a : " << a << endl;
    cout << "Valeur de b : " << b << endl;

    return 0;
}