#include <iostream>
#include <list>

int main ()
{
	int myints[] = {16,2,77,29};
	std::list<int> maliste (myints, myints + sizeof(myints) / sizeof(int) );

	while (0 == 0)
	{
		int x = 0;
		std::cout << "taper un nombre" << std::endl;
		std::cout << "~} ";
		std::cin >> x;
		std::cin.ignore();
		std::cout << "" << std::endl;

		maliste.emplace_back(x); 

		for (std::list<int>::iterator it = maliste.begin(); it != maliste.end(); it++)
		{
			std::cout << *it << std::endl;
		}
	}
	
	return 0;
}