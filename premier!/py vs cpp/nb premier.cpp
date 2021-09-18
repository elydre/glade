# include <iostream>
#include <cmath>

int main()
{
    std::cout << "runing" << std::endl;
    for(long long int i = 0; i <= 4000000; ++i)
    {
        long long int max = pow(i,0.5) + 1;

        if(i%2 != 0)
        {
            
            for (long long int x = 2; x <= max; x++)
            {
                if (i%x == 0)
                {
                    break;
                }
                    
                if (x == max)
                {
                    //std::cout << i << std::endl;
                }
                    
            }
        }
    }
    return 0;
}