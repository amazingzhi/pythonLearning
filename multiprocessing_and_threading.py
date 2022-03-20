# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:22:45 2021

@author: amazi
"""
#ONLY IF YOU DO DIFFERENT TYPES OF JOBS, 
#CAN MULTI-THREADING HELP YOU.
#HOWEVER, MULTI-PROCESSING CAN HELP YOU DO SAME
#TYPE JOBS AT THE SAME TIME
#import libraries
import multiprocessing as mp
import threading
import time

#practice 1
def main():
    # #count how many threadings we have
    # print(threading.active_count())
    # #details of those threadings
    # print(threading.enumerate())
    # #what is the threading we use now
    # print(threading.current_thread())
    #add threading with target job
    added_thread = threading.Thread(target = thread_job)
    #start thread
    added_thread.start()

# add job for added thread
def thread_job():
    print('this is an added thread, number is %s'% threading.current_thread())
    

if __name__=='__main__':
    main()
    
    
    
#practice 2    
def main1():
    added_thread = threading.Thread(target=thread_job1, name='T1')
    added_thread.start()
    print('all done\n')

def thread_job1():
    print('T1 starts\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
        
if __name__=='__main__':
    main1()
#通过结果可以看到，主线程main和T1同时在跑，而且主线程
#在T1还没有跑完，main就已经跑完了，为了解决这个问题，
#需要用到join函数,它的作用是让所有不是main的thread
#跑完再把main跑完
#practice 3
def main2():
    added_thread = threading.Thread(target=thread_job2, name='T1')
    thread2 = threading.Thread(target=thread_job21, name='T2')
    added_thread.start()
    thread2.start()
    #add join here
    added_thread.join()
    thread2.join()
    print('all done\n')

def thread_job2():
    print('T1 starts\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
def thread_job21():
    print('T2 start')
    print('T2 finish')
        
if __name__=='__main__':
    main2()

#practice 4 (how to use queue to store results
# from threading)
import threading
import time
from queue import Queue
#define job that calculate sth by given data
def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)
#define main threading
def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__=='__main__':
    multithreading()
    




    
    
    
    
    
    
    
    