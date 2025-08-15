class Bank_account:
    def account(self,account_holder,balances):
        self.account_holder=account_holder
        self.balances=balances
        print("they account holder name:",self.account_holder)
        print('now the current balances is:',self.balances)
    def deposit(self,deposit1):
        self.deposit1=deposit1
        print("you have Deposited:",deposit1)
    def withdraw(self,with_draw):
        self.with_draw=with_draw
        print('You have withdraw:',with_draw)
    def display_balances(self,current_balances):
        current_balances=(self.balances+self.deposit1)-self.with_draw
        print("Balances:",current_balances)

bank=Bank_account()
bank.account('Tonny',1000)
bank.deposit(255)
bank.withdraw(500)
bank.display_balances(100)
    
        