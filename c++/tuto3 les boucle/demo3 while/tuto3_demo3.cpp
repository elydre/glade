# include <iostream>

int main()
{
    int n = 5;

    while (true)
    {
        int n = 0;
        std::cin >> n;
        std::cin.ignore();

        if (n == 0)
        {
            break;
        }
    }
    std::cout << "sortie" << std::endl;
    std::cin.ignore();
    return 0;
}