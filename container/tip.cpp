// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
int main()
{
    string ipt;  // auto var
    bool True = true;
    for (long int x = 0; x < 50; x = x + 1)
    {
        cout << "" << endl;
    }
    cout << "   Bonjour et bienvenu sur TIP4" << endl;
    cout << "   le terminal d’interprétation personnalisé de pf4 -" << endl;
    while (True)
    {
        cout << "~} ";
        cin >> ipt;
        cin.ignore();
        //   INFO  
        if (ipt == "info" or ipt == "INFO")
        {
            cout << "   dev: PF4-" << endl;
            cout << "   run by PYTHON 3" << endl;
            cout << "" << endl;
        }
        if (ipt == "aide" or ipt == "AIDE")
        {
            cout << "   aide:         affiche l’aide" << endl;
            cout << "   info:         affiche des infos" << endl;
            cout << "   erreur_liste: affiche la liste d’erreur" << endl;
            cout << "" << endl;
        }
        if (ipt == "erreur_liste" or ipt == "ERREUR_LISTE")
        {
            cout << "   ERRUER 001 -> commande inconnu" << endl;
            cout << "" << endl;
        }
        else
        {
            cout << "-ERREUR 001" << endl;
            cout << "-commande inconnu" << endl;
        }
    }
}
