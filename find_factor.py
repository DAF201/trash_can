import threading
num = int(input())
the_root = num**(1/2)
a = [x for x in range(0, int(the_root)+1)]
a1 = iter(a)
a.reverse()
a2 = iter(a)
run = True


def bottom():
    global run
    for x in a1:
        if run == True:
            if num % x == 0:
                print('find on bottom')
                print(x)
                print(int(num/x))
                run = False
                break


def top():
    global run
    for x in a2:
        if run == True:
            if num % x == 0:
                print('find on top')
                print(x)
                print(int(num/x))
                run = False
                break


t1 = threading.Thread(target=bottom)
t2 = threading.Thread(target=top)
t1.start()
t2.start()
t1.join()
t2.join()
