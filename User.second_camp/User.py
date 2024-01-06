class User:#This is the object 
    def __init__(self,first_name,last_name,email,age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.Gold_card_points = 0



    def display_info(self):
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

    def Check_member(self):
        if self.is_rewards_member == True:
            print ('You are already a member')
            return self

userone = User('Kyree','Graham','KG@GMAIL.COM',19)
usertwo = User('Brandon','Graham','Bgraham23602',43)
userthree = User('Charmaine','Atwater','Charmaine4hair@gmail.com',43)
userone.spend_points(50)
usertwo.enroll().spend_points(80).display_info()
userone.display_info()
usertwo.display_info()
userthree.display_info()

#HAD TROUBLE CHAINING METHODS
#WHICH PART OF CRUD IS THIS




        
        