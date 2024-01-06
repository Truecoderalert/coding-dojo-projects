class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print (f'After withdrawing {amount} dollars Your new balance is {self.balance}') 
        return self

    def withdraw(self,amount):
        if (self.balance) > 0:
            self.balance -= amount
            print(f"After withdrawing {amount} dollars Your new balance is {self.balance}" )
        else:print ('insufficiant funds')
        return self

    def display_info(self):
        print(f"Your current balance is {self.balance} With an interest rate of {self.int_rate}" )
        return self
        
    def yeildint(self):
        if (self.balance) > 0:
            (self.balance) * (self.int_rate)
            print(f"Your new balance is {self.balance}" )
        else:print ('insufficiant funds')
        return self
    
    @classmethod 
    def display_all_info(cls):
        for account in cls.all_accounts:
            print (account.balance)




BankAccountone = BankAccount(0,0)
BankAccounttwo = BankAccount(0,10)
BankAccountone.deposit(10).deposit(10).deposit(30).withdraw(20).yeildint().display_info()
BankAccounttwo.deposit(50).deposit(50).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yeildint().display_info
BankAccountone.display_all_info()