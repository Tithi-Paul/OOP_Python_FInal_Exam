from Bank import Bank

class Account:
    def __init__(self, name, age, nid) -> None:
        self.name = name
        self.age = age
        self.NID = nid

class User(Account):
    def __init__(self, name, age, nid, branch) -> None:
        super().__init__(name, age, nid)
        self.__account_balance = 0
        self.__transaction_history = []
        self.branch = branch
        self.is_admin = False

    def set_account_number(self, ac_number):
        self.__account_number = ac_number
        
    @property
    def account_number(self):
        return self.__account_number

    @property
    def get_balance(self):
        return self.__account_balance

    def check_total_balace(self):
        print(f"{self.name}, Your Total Balance is {self.get_balance}")
    
    def deposit(self, amount, from_user = None):
        self.__account_balance += amount
        if from_user:
            self.__transaction_history.append(f"Recived balance {amount} from {from_user.name}({from_user.account_number}")           
        else:
            self.__transaction_history.append(f"Deposit {amount}")
    
    def take_loan(self, amount):
        if self.__account_balance * 2 >= amount:
            self.__account_balance += amount
            self.__transaction_history.append(f"Take Loan {amount} from the Bank")
            return True
        else:
            print(f"Sorry {self.name}, You can't take loan more than twice of your current balance")
            return False

    def withdrawal(self, amount):
        if amount > self.__account_balance:
            print(f"{self.name}, You can't withdrawal {amount}")
            return False
        else:
            self.__account_balance -= amount
            self.__transaction_history.append(f"withdrawal {amount}") 
        return True
    
    def transfer(self, amount, to_account):
        if amount > self.__account_balance:
            print(f"Insufficient Balance, maximum tansfer {self.__acount_balance}")
        else:
            self.__account_balance -= amount
            self.__transaction_history.append(f"Transfered {amount} to {to_account.name}({to_account.account_number})")
            return True
    
    @property
    def transaction_history(self):
        return self.__transaction_history

class Admin(Account):
    def __init__(self, name, age, nid, security_key) -> None:
        super().__init__(name, age, nid)
        self.security_key = security_key
        self.is_admin = True
    
    def set_pin_number(self, pin):
        self.__pin_number = pin
        
    @property
    def pin_number(self):
        return self.__pin_number


# # Can take a loan from the bank twice of his total amount..