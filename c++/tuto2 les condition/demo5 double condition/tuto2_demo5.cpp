#include <iostream>

int main()
{
    int age = 5;
    bool avec_parent = true;

    if(age >= 16 || avec_parent == true && age > 4) // le || = or en py. // le == true n'est pas obligatoir // le && = and en py.
    {
        std::cout << "autorise" << std::endl;
    }
    else
    {
        std::cout << "non autorise" << std::endl;
    }

    std::cin.ignore(); //on dit posse au programme pour voir la sortie

    return 0;
}