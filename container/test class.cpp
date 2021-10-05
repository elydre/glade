// interpreted and compiled by GLADE
#include <iostream>


using namespace std;
class test{
    private:
        long int b=4;
    public:
        long int a=b*2;  // auto var
};

int main()
{
    test coucou;
    cout << coucou.a << endl;
    return 0;
};