#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
double total = 0;
class product
{
public:
    string PLU_code;
    string name;
    string type;
    string price;
    string inventory;

    product(string line)
    {
        // cout << line << endl;
        vector<string> info = split(line);
        int counter = 0;
        string temp[5];
        for (string in : info)
        {
            temp[counter] = in;
            counter++;
            // cout << temp[counter] << endl;
        }
        this->PLU_code = temp[0];
        this->name = temp[1];
        this->type = temp[2];
        this->price = temp[3];
        this->inventory = temp[4];
    }
    void get_PLU()
    {
        cout << name.size() << endl;
        if (name.size() > 7)
        {
            cout << this->PLU_code << "\t";
        }
        else
        {
            if (name.size() > 16)
            {
                cout << this->PLU_code;
            }
            else
            {
                cout << this->PLU_code << "\t\t";
            }
        }
    }
    void get_name()
    {
        cout << this->name << "\t\t";
    }
    void get_type()
    {
        cout << this->type << "\t\t";
    }
    void get_price()
    {
        cout << this->price << "\t\t";
    }
    void get_inventory()
    {
        cout << this->inventory << "\t\t";
    }
    void purchase(int amount)
    {
        if ((amount <= stoi(inventory)) & (inventory != "0"))
        {
            total = total + amount * stod(price);
            int temp_inventory = stoi(inventory) - amount;
            cout << temp_inventory << endl;
            set_inventory(temp_inventory);
            cout << "total price:" << total << endl;
        }
        else
        {
            cout << "no enough items left!" << endl;
        }
    }
    void set_inventory(int i)
    {
        inventory = to_string(i);
    }
    void get_info()
    {
        get_PLU();
        get_name();
        get_type();
        get_price();
        get_inventory();
        cout << endl;
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
void title()
{
    cout << "PUL\t\t"
         << "Name\t\t"
         << "Type\t\t"
         << "Price\t\t"
         << "inventory\t\t" << endl;
}
string get_input()
{
    char input[128];
    cin.getline(input, sizeof(input), '\n');
    cout << " "
         << endl;
    return input;
}
int main()
{
    cout << "please select productdata" << endl;
    // string user_input = get_input();
    string user_input;
    vector<product> products_info;
    // ifstream infomation(user_input);
    ifstream infomation("productData1.txt");
    string line;
    // cout << "loading..." << user_input << endl;
    title();
    while (getline(infomation, line))
    {
        // cout << line << endl;
        product *products = new product(line);
        products_info.push_back(*products);
        // products->get_info();
        // products->get_PLU();
    }
    cout << "finished loading" << endl;
    title();
    for (product i : products_info)
    {
        i.get_info();
    }
    while (true)
    {
        cout << "1 - Checkout\n2 - Print current inventory\n3 – Quit" << endl;
        user_input = get_input();
        if (user_input == "1")
        {
            cout << "enter the PUL number to continus" << endl;
            user_input = get_input();
            int counter = 0;
            for (product i : products_info)
            {
                if (i.PLU_code == user_input)
                {
                    cout << "remains:" << i.inventory << endl;
                    cout << "enter the number you need" << endl;
                    user_input = get_input();
                    i.purchase(stoi(user_input));
                    products_info[counter] = i;
                }
                counter++;
            }
        }
        if (user_input == "2")
        {
        }
        else
        {
        }
    }
    system("pause");
    return 0;
}
