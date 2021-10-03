#include <iostream>
#include <string>
using namespace std;

class test
{
    string name;

public:
    test(string name)
    {
        this->name = name;
    }
    string return_name()
    {
        return name;
    }
};

int main()
{
    test *a = new test("hello");
    cout << a->return_name()
         << endl;
    // system("pause");
    return 0;
}