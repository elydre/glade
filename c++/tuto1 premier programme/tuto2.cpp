#include <iostream>

int main()
{
    
    int an = 0;

    std::cout << "quand etes vous ne?" << std::endl;
    std::cout << "~} ";

    std::cin >> an;
    std::cin.ignore();

    std::cout << "vous avez " << 2020 - an << " ans" << std::endl;
    std::cin.ignore();

    return 0;
}