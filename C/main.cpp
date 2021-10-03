#include <iostream>

using namespace std;
int a = 1;
int b = 2;
int *pointer_a = &a;
int *pointer_b = &b;
int temp;
int main()
{
   cout << "this is the value of a: " << a << endl;
   cout << "this is the value of b: " << b << endl;
   cout << "this is a empty value for switching the a and b: " << temp << endl;
   cout << "this is a pointer pointing to the address of a in memory: " << pointer_a << endl;
   cout << "this is a pointer pointing to the address of b in memory: " << pointer_b << endl;
   printf("\n \n");
   cout
       << "now start switching try 1, switch by reference:" << endl;
   cout << "firstly, assign the value of a to temp" << endl;
   temp = a;
   cout << "then, assign the value of b to a, now the value in a is 2" << endl;
   a = b;
   cout << "the new a: " << a << endl;
   cout << "next, assign the value stored in temp to b" << endl;
   b = temp;
   cout << "the value stored in b now is: " << b << endl;
   cout << "value of a and b are:\n"
        << a << "\n"
        << b << "\n"
        << "\n"
        << endl;
   int *pointer_new_a = &a;
   int *pointer_new_b = &b;
   cout << "and the address of a and b are:\n"
        << pointer_new_a << "\n"
        << pointer_new_b << "\n"
        << endl;
   cout << "now start the second try, directly manipulate value through pointer:" << endl;
   cout << "create a temp pointer to save pointer for switch" << endl;
   int *temp_pointer;
   cout << "assign the new temp pointer with the address of a" << endl;
   temp_pointer = pointer_new_a;
   cout << "then, assign the value of pointer a with pointer b" << endl;
   pointer_new_a = pointer_new_b;
   cout << "lastly, assign the pointer b with value stored in temp pointer" << endl;
   pointer_new_b = temp_pointer;
   cout << "the values with in a and b are now:\n"
        << *pointer_new_a << "\n"
        << *pointer_new_b << endl;
   cout << "and the address of a and b are now:\n"
        << pointer_new_a << "\n"
        << pointer_new_b << "\n"
        << "compare with original:\n"
        << pointer_a << "\n"
        << pointer_b << endl;
   return 0;
}