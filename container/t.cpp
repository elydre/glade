// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
int main()
{
    for (long int a = 0; a <= 100; a = a + 1)
    {
        for (long int b = 0; b <= a; b = b + 1)
        {
            cout << b+a << endl;
        }
    }
}
