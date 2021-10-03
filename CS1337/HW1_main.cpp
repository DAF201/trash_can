#include <iostream>
#include <string>
#include <bits/stdc++.h>
#pragma GCC diagnostic ignored "-Wsizeof-array-argument"
/*
    I guess I just have no talent in making wheels... No idea how am I going to handle those data in a single txt like "1001 CS 3.8...".
    So I separate three txt files and read them (I will use json to store data normally).
    Also I am not quite sure how am I suppoer to link those datas in three arrays with out something like dictionary (reason for I create a class, and I didn't sort those)
    Another issue I met is something called "segmentation fault", not even sure what is that...
*/
using namespace std;
int netid[128];
string major[128];
double gpa[128];
char input[128];
int conv;
int get_input()
{
    cin.getline(input, sizeof(input), '\n');
    conv = stoi(input);
    cout << " "
         << endl;
    return conv;
}
class student
{
    int student_netid;
    string student_major;
    double student_gpa;

public:
    void set_gpa(int i)
    {
        student_gpa = gpa[i];
    }
    void set_netid(int i)
    {
        student_netid = netid[i];
    }
    void set_major(int i)
    {
        student_major = major[i];
    }
    double get_gpa()
    {
        return student_gpa;
    }
    int get_netid()
    {
        return student_netid;
    }
    string get_major()
    {
        return student_major;
    }
};
void exit_mode()
{
    cout << "Exiting\n"
         << endl;
    system("pause");
    exit(0);
}
void read_file()
{
    ifstream NetID_file("NetId.txt");
    ifstream GPA_file("GPA.txt");
    ifstream Major_file("Major.txt");

    if (NetID_file.is_open())
    {
        int position = 0;
        string line;

        while (getline(NetID_file, line))
        {
            netid[position] = stoi(line);
            position++;
        }
    }
    else
    {
        cout << "could not open the file: NetId.txt\n"
             << endl;
        exit_mode();
    }

    if (GPA_file.is_open())
    {
        int position = 0;
        string line;

        while (getline(GPA_file, line))
        {
            gpa[position] = stod(line);
            position++;
        }
    }
    else
    {
        cout << "could not open the file: GPA.txt\n"
             << endl;
        exit_mode();
    }

    if (Major_file.is_open())
    {
        int position = 0;
        string line;

        while (getline(Major_file, line))
        {
            major[position] = line;
            position++;
        }
    }
    else
    {
        cout << "could not open the file: major.txt\n"
             << endl;
        exit_mode();
    }
}
void read_mode(int times, student students[])
{
    if (times > 128)
    {
        times = 128;
    }
    cout << "NetId\tGPA\tMajor\t" << endl;
    for (int i = 0; i < times; i++)
    {
        cout << students[i].get_netid() << "\t" << students[i].get_gpa() << "\t" << students[i].get_major() << "\t" << endl;
    }
}
void search_mode(int netid, student students[])
{
    bool found = false;
    for (int i = 0; i < sizeof(students); i++)
    {
        if (students[i].get_netid() == netid)
        {
            found = true;
            cout << "NetId\tGPA\tMajor" << endl;
            cout << students[i].get_netid() << "\t" << students[i].get_gpa() << "\t" << students[i].get_major() << "\t" << endl;
            cout << " "
                 << endl;
        }
    }
    if (found == false)
    {
        cout << "can not find the student associated to this NetId: " << netid << endl;
        cout << " "
             << endl;
    }
}
int main()
{
    read_file();
    student students[128];
    for (int i = 0; i < 128; i++)
    {
        students[i].set_gpa(i);
        students[i].set_major(i);
        students[i].set_netid(i);
        // cout << students[i].get_netid() << "\t" << students[i].get_gpa() << "\t" << students[i].get_major() << endl;
    }
    while (true)
    {
        cout << "***************\nMenu of choices\n***************\n1 - List top n students\n2 - Search on a netID\n3 – Quit " << endl;
        cout << " "
             << endl;
        switch (get_input())
        {
        case 1:
            cout << "please enter number of students you want to check (MAX-128)" << endl;
            read_mode(get_input(), students);
            break;
        case 2:
            cout << "please enter a NetId to start searching" << endl;
            search_mode(get_input(), students);
            break;
        default:
            exit_mode();
            break;
        }
    }

    return 0;
}
/*
import json
import os
from os import path
temp = []
Net_Id = []
Gpa_info = []
Major_info = []
info = {}
current_path = os.getcwd()
if path.isfile(current_path+"/NetId.txt"):
    if path.isfile(current_path+"/Major.txt"):
        if path.isfile(current_path+"/GPA.txt"):
            with open(current_path+"/NetId.txt", "r")as NetId:
                with open(current_path+"/GPA.txt", "r")as Gpa:
                    with open(current_path+"/Major.txt", "r")as Major:
                        temp = NetId.readlines()
                        for x in temp:
                            if("\n" in x):
                                x = x[0:len(x)-1]
                                Net_Id.append(x)
                        temp = Gpa.readlines()
                        for x in temp:
                            if("\n" in x):
                                x = x[0:len(x)-1]
                                Gpa_info.append(x)
                        temp = Major.readlines()
                        for x in temp:
                            if("\n" in x):
                                x = x[0:len(x)-1]
                                Major_info.append(x)
                        for x in range(0, len(Net_Id)):
                            info[Gpa_info[x]] = [Net_Id[x], Major_info[x]]
                        with open("student_data.json", "w")as students_data:
                            json.dump(info, students_data)
*/
/*
import json
import time
import os
from os import path
current_path = os.getcwd()
temp = []
sorted = {}
student_data = {}


def fetch():
    if path.isfile(current_path+"/student_data.json"):
        with open(current_path+"/student_data.json", "r")as students:
            global student_data
            student_data = json.load(students)


def read_mode(number):
    for keys in student_data:
        temp.append(keys)
    temp.sort(reverse=True)
    print("GPA\tNetId\tMajor")
    for x in range(0, int(number)):
        print(temp[x], "\t", student_data[temp[x]]
              [0], "\t", student_data[temp[x]][1])


def search_mode(id):
    found = False
    for keys in student_data:
        if student_data[keys][0] == id:
            print("GPA\tNetId\tMajor")
            print(keys, "\t", student_data[keys]
                  [0], "\t", student_data[keys][1])
            found = True
    if(found == False):
        print("Can not find student with this student id: ", id)


fetch()

while(True):
    print("***************\nMenu of choices\n***************\n1 - List top n students\n2 - Search on a netID\n3 – Quit ")
    use_in = input()
    if(use_in == "1"):
        print("enter the number of student you want")
        read_mode(input())
    elif (use_in == "2"):
        print("enter the NetId of student you want")
        search_mode(input())
    else:
        print("existing...")
        time.sleep(3)
        exit()

*/