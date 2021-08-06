import threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    balance = balance - n
    balance = balance + n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

# t1 = threading.Thread(target=run_thread, args=(1,))
# t2 = threading.Thread(target=run_thread, args=(-1,))
t1 = threading.Thread(target=run_thread(n=1))
t2 = threading.Thread(target=run_thread(n=1))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)