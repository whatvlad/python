class Bank:
    def __init__(self,account):
        self.account=account
    def describe_bank(self):
        print(f"На вашем счету{self.account}грн.")
    def withdraw(self,n):
        if n<self.account:
            self.account-=n
            print(f"Вы сняли со счета суму в размере {n}грн. , на вашем счету {self.account} грн.")
        else: print("Вы не можете снять больше чем у вас на счету!")
    def replenish(self,m):
         self.account+=m
         print(f"Вы пополнили счетт суму в размере {m}грн. , на вашем счету {self.account}грн.")     


Balance=Bank(5000)
Balance.describe_bank()
n=int(input("Введите суму которую хотите снять --> "))
Balance.withdraw(n)
m=int(input("Введите суму на которую хотите пополнить --> "))
Balance.replenish(m)
n=int(input("Введите суму которую хотите снять --> "))
Balance.withdraw(n)   
