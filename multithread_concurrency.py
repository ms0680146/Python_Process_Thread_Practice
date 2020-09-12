from time import sleep
from threading import Thread

class Account(object):
    def __init__(self):
        self._deposit = 0

    def make_deposit(self, money):
        new_deposit = self._deposit + money
        sleep(0.01)
        self._deposit = new_deposit

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
    # 創建 50 個存款的 thread 向同一個帳戶中存錢
    for _ in range(50):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    
    # 等所有存款的 thread 都執行完畢
    for t in threads:
        t.join()

    print('Total Deposit : %d dollars' % account.deposit)

if __name__ == '__main__':
    main()