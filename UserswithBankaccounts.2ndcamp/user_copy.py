class User:#This is the object 
    
    def __init__(self,first_name,last_name,email,age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age


    def display_personal_info(self):
        print (self.first_name)
        print (self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.Gold_card_points += 200
        print (self.is_rewards_member)
        print (self.Gold_card_points)
        return self

    def spend_points(self,points):
        self.Gold_card_points -= points
        print (self.Gold_card_points)
        return self


class BankAccount(User):
    def __init__(self,int_rate,balance,first_name,last_name,email,age,):
        self.balance = balance
        self.int_rate = int_rate
        super().__init__(first_name,last_name,email,age)

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


BankAccountone = BankAccount(0,0,'first_name','last_name','email','age')
BankAccounttwo = BankAccount(0,10,'first_name','last_name','email','age')
BankAccountone.deposit(10).deposit(10).deposit(30).withdraw(20).yeildint().display_info()


        
        