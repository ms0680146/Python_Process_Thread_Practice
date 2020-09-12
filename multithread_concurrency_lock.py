from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._deposit = 0
        self._lock = Lock()

    def make_deposit(self, money):
        # 鎖起來 才能執行後續的程式碼
        self._lock.acquire()
        new_deposit = self._deposit + money
        sleep(0.01)
        self._deposit = new_deposit
        # 釋放鎖
        self._lock.release()

    @property
    def deposit(self):
        return self._deposit

class AddMoneyThread(Thread):
    def __init__ (self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.make_deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(50):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Total deposit : %d dollars' % account.deposit)

if __name__ == '__main__':
    main()