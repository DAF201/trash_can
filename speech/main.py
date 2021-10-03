import win32com.client
import pathlib
import time
import os


def say(phrase):
    win32com.client.Dispatch("SAPI.SpVoice").Speak(phrase)


PATH = str(pathlib.Path(__file__).parent.resolve())


def read_personal_doc():
    with open(PATH + '\doc.txt')as doc:
        docs = doc.read()
        print(docs)
        say(docs)


def read_group_doc():
    with open(PATH + '\docs.txt')as doc:
        docs = doc.read()
        print(docs)
        say(docs)


def exiting():
    say('exiting in three seconds')
    for x in [3, 2, 1, 0]:
        print('exiting in %s seconds' % x, end='\r')
        if x != 0:
            say(x)
            time.sleep(1)
    say('exit!')
    os._exit(0)


def main():
    print("I case I am kind of busy and lazy, I spend about 10 mins to make this bot to help me")
    print("if you need the voice control version of this or other things, goes to my Github @DAF201")
    while True:
        print("Do something...\nCurrent functions:\n1.Read group doc\n2.Read the personal part\n3.exit")
        user_input = input()
        if user_input == "1":
            print("1.Read group doc", end="\r")
            read_group_doc()
            exiting()

        if user_input == "2":
            print("2.Read the personal part", end="\r")
            read_personal_doc()
            exiting()

        if user_input == "3":
            print("3.exit", end="\r")
            exiting()
        else:
            print("invaild input")


main()
