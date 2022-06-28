import threading
import time

'''
python 自带 gil锁
    线程在同一时刻，只能由一个线程在运行
    python运行不那么高效
    cpu代表多进程的能力
'''

def task():
    time.sleep(5)
    # print("扔第二个苹果")
def task2():
    print("扔第三个苹果")
def main():
    start_time=time.time()
    #threading创建了一个线程
    thread1=threading.Thread(target=task)
    thread2 = threading.Thread(target=task)

    thread1.start()
    thread2.start()

    #让其他线程等待自己执行完成
    thread1.join()
    thread2.join()

    end_time=time.time()
    print(end_time-start_time)

if __name__=="__main__":
    main()