// interpreted and compiled by GLADE
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
cout << "runing" << endl;
    long long int max = 0;
    for (long int i = 0; i <= 4000; i = i + 1)
    {
        max = pow(i,0.5) + 1;
        if (i%2 != 0)
        {
            for (long int x = 2; x <=  max; x = x + 1)
            {
                if (i%x == 0)
                {
                    break;
                }
                if (x == max)
                {
                    cout << i << endl;
}
}
}
}
}
