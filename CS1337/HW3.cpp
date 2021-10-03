#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
/*
read        ->          store           ->          check           ->          return          ->          result
ifstream                oop                         buildin function            bool                        cout
vector                  split,to string             check numbers/type          T?F                         print
*/
vector<string> read_file()
{
    ifstream file("NetId.txt");
    string line;
    vector<string> data;
    while (getline(file, line))
    {
        data.push_back(line);
    }
    return data;
}
string get_input()
{
    char input[128];
    cin.getline(input, sizeof(input), '\n');
    cout << " "
         << endl;
    return input;
}
bool check()
{
}
class product
{
    string PLU;
    string name;
    string type;
    string price;
    string inventory;
    bool vaild;
    product(string line)
    {
        this->vaild = true;
    }
    vector<string> split(string oringinal)
    {
        oringinal = oringinal + " ";
        string temp;
        vector<string> splited;
        const char space = ' ';
        for (int i = 0; i < oringinal.size(); i++)
        {
            if (oringinal[i] != space)
            {
                temp = temp + oringinal[i];
            }
            else
            {
                splited.push_back(temp);
                temp = "";
            }
        }
        return splited;
    }
};
int main()
{
    return 0;
}