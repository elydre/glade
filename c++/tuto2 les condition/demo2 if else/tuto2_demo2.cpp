#include <iostream>

int main()
{
    float moyenne = 0.0f;
    std::cout << "tappe ta moyenne: " << std::endl;
    std::cin >> moyenne;
    std::cin.ignore();

    if(moyenne == 20)
    {
        std::cout << "gg" << std::endl;
    }
    else if(moyenne >= 16)
    {
        std::cout << "tres bien" << std::endl;
    }
    else if(moyenne >= 14)
    {
        std::cout << "bien" << std::endl;
    }
    else if(moyenne >= 12)
    {
        std::cout << "assez bien" << std::endl;
    }
    else
    {
        std::cout << "nop" << std::endl;
    }
    
    std::cin.ignore(); //on dit posse au programme pour voir la sortie

    return 0;
}