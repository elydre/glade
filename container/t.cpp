// interpreted and compiled by GLADE
#include <iostream>
using namespace std;
#include <list>
int main()
{
    string a;  // auto var
    string d;  // auto var
    a = "z";
    string pre_b[] = {a};
    list<string> b (pre_b, pre_b + sizeof(pre_b) / sizeof(string));
    d = a;
}
