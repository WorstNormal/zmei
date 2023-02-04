from threading import Thread
import time
from pathlib import Path
def writer(filename, n, k):
    with open(filename, 'w') as fout:
        for i in range(n * k - n, n * k):
            fout.write(str(i))
            
def writer1(filename, n):
    with open(filename, 'w') as fout:
        for i in range(n):
            fout.write(str(i))
            
if __name__ == "__main__":
    for j in range(10):
        lis1 = []
        lis2 = []
        for i in range(1):
            t = time.time()
            t1 = Thread(target=writer, args=("test1.txt", 125000, 1,))
            t2 = Thread(target=writer, args=("test2.txt", 125000, 2,))
            t3 = Thread(target=writer, args=("test3.txt", 125000, 3,))
            t4 = Thread(target=writer, args=("test4.txt", 125000, 4,))
            t5 = Thread(target=writer, args=("test5.txt", 125000, 5,))
            t6 = Thread(target=writer, args=("test6.txt", 125000, 6,))
            t7 = Thread(target=writer, args=("test7.txt", 125000, 7,))
            t8 = Thread(target=writer, args=("test8.txt", 125000, 8,))
            
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            t8.join()
            
            tt = time.time()
            lis1.append(tt - t)
            
            t = time.time()
            writer1('test01.txt', 1000000)
            tt = time.time()
            lis2.append(tt - t)
        print(sum(lis1))
        print(sum(lis2))
        print()