from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('Start Process，process id [ %d ].' % getpid())
    print('Start Download %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s Download Success. Take %d seconds' % (filename, time_to_download))

def main():
    start = time()
    # 利用 Process 類別創建了 process 物件
    # 透過 target 參數傳入一個函數來表示 process 啟動後要執行的程式碼
    # 後面的 args 代表傳遞給函數的參數
    # Process 物件的 start 方法來啟動 process 而 join 方法 (method) 表示等待 process 執行結束。
    p1 = Process(target = download_task, args = ('Python.pdf', ))
    p1.start()

    p2 = Process(target = download_task, args = ('Hot.avi', ))
    p2.start()
    
    p1.join()
    p2.join()
    
    end = time()
    print('Total take %.2f seconds.' % (end - start))

if __name__ == '__main__':
    main()