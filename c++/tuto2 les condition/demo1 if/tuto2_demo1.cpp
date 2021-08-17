#include <iostream>

int main()
{
    int hp = 0;

    if(hp <= 0) // <= / >= / == / != / < / > / comme en python / && → si les 2 sont replie / || si une des 2 est remplie
    {
        std::cout << "le joueur est mort" << std::endl;
    }
    else
    {
        std::cout << "le joueur est vivant" << std::endl;
    }
    
    std::cin.ignore(); //on dit posse au programme pour voir la sortie

    return 0;
}