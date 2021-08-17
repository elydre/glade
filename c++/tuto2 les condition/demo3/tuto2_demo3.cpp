#include <iostream>

int main()
{
    int age = 0;
    std::cout << "tappe ton age: " << std::endl;
    std::cin >> age;
    std::cin.ignore();

    if(age >= 18)
    {
        std::cout << "majeur" << std::endl;
    }
    else
    {
        std::cout << "mineur" << std::endl;
    }
    
    std::cin.ignore(); //on dit posse au programme pour voir la sortie

    return 0;
}