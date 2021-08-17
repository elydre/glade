#include <iostream>

int main()
{
    int age = 0;
    std::cout << "tappe ton age: " << std::endl;
    std::cin >> age;
    std::cin.ignore();


    // if and else en une ligne

    std::cout << "vous etes " << (age < 18 ? "mineur" : "majeur") << std::endl;
    
    std::cin.ignore(); //on dit posse au programme pour voir la sortie

    return 0;
}