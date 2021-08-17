# include <iostream>

int main()
{
    int n = 0;
    std::cout << "quelle table?" << std::endl;
    std::cin >> n;
    std::cin.ignore();

    for(int i = 0; i <= 10; ++i)
    {
        std::cout << n << "x" << i << " = " << i*n << std::endl;
    }
    std::cin.ignore();
    return 0;
}