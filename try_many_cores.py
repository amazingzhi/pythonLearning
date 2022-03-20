# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:03:37 2021

@author: amazi
"""
# multi-processing
# import library
import multiprocessing as mp
import moduel_NBA as mn
import time
# create jobs
def job(q):
    res=0
    for i in range(100000):
        res += i+i**2+i**3
    q.put(res)
# create process
# no arguments in target, put it in arguments
if __name__ == '__main__':
    # get Queue


    st = time.time()
    q = mp.Queue()
    # a=mp.Value("d",0)
    #if there is only one argument in args,
    #you need to put a comma to show it is iterable
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # the number of q.get() is equal to number of processes
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
    et = time.time()
    print(et-st)


#time comparision
import multiprocessing as mp
import threading as td
import time
from queue import Queue

# create jobs
def job(q):
    res=0
    for i in range(100000):
        res += i+i**2+i**3
    q.put(res)
#multiprocessing
def multicore():
    q = mp.Queue()
    #if there is only one argument in args,
    #you need to put a comma to show it is iterable
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # the number of q.get() is equal to number of processes
    res1 = q.get()
    res2 = q.get()
    print('process:' ,res1+res2)
#normal process
def normal():
    res = 0
    #for comparision between normal and process,
    #we need to run it twice
    for j in range(2):
        for i in range(100000):
            res += i+i**2+i**3
    return(print('normal:',res))

#multithread
def multithread():
    # get Queue
    q = mp.Queue()
    #if there is only one argument in args,
    #you need to put a comma to show it is iterable
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # the number of q.get() is equal to number of processes
    res1 = q.get()
    res2 = q.get()
    print('thread:', res1+res2)
#main process
if __name__ == '__main__':
    stn = time.time()
    normal()
    etn = time.time()
    normal = etn-stn
    print('normal time:', normal)
    stt = time.time()
    multithread()
    ett = time.time()
    thread = ett-stt
    print('thread time:', thread)
    stp = time.time()
    multicore()
    etp = time.time()
    process = etp-stp
    print('process time:', process)
    
#test
st=time.time()
res = 0
for i in range(5000):
    for i1 in range(5000):
        res += i+i1
print(res)
et=time.time()
print(et-st)



if __name__ == '__main__':
    # get Queue
    st = time.time()
    q = mp.Queue()
    #if there is only one argument in args,
    #you need to put a comma to show it is iterable
    p1 = mp.Process(target=mn.job1, args=(q,))
    p2 = mp.Process(target=mn.job1, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # the number of q.get() is equal to number of processes
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
    et = time.time()
    print(et-st)

#from documentation
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))













