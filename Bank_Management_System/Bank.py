import random
class Bank():
    def __init__(self, name, address, initial_balance) -> None:
        self.bank_name = name
        self.address = address
        self.__available_balance = initial_balance
        self.__loan_amount = 0
        self.loan_feature = True
        self.__users_list = {}
        self.__admins_list = {}
        self.__security_key = 'security123'

    # Blance, Deposite/Withdrawal, Transfer Section
    @property   
    def get_balance(self):
        return self.__available_balance
    
    def check_total_balance(self, user):
        if user.is_admin:
            print(f"Total Available Balance: {self.get_balance}")
        else:
            print(f"Sorry {user.name}, You don't have permission to access!")
    
    def deposit_balance(self, user, amount):
        self.__available_balance += amount
        if user.account_number in self.__users_list:
            self.__users_list[user.account_number].deposit(amount)
    
    def withdrawal_balance(self, user, amount):
        if amount > self.__available_balance:
            print (f"The {self.bank_name} is Bankrupt.")
        elif user.account_number in self.__users_list and user.withdrawal(amount):
            self.__available_balance -= amount
    
    def balance_transfer(self, user_from, amount, user_to):
        if user_from.account_number in self.__users_list and user_to.account_number in self.__users_list:
            if self.__users_list[user_from.account_number].transfer(amount, user_to):
                self.__users_list[user_to.account_number].deposit(amount, user_from)

    # Loan Section
    @property
    def get_loan_amount(self):
        return self.__loan_amount

    def set_loan_amount(self, amount):
        self.__loan_amount += amount
    
    def check_loan_ammount(self, user):
        if user.is_admin:
            print(f"Total Loan Amount {self.get_loan_amount}")
        else:
            print(f"Sorry {user.name}, You don't have permission to access!")

    @property
    def get_loan_feature_status(self):
        return self.loan_feature
    
    def set_loan_feature_status(self, status, user):
        if user.is_admin:
            self.loan_feature = status
        else:
            print(f"Sorry {user.name}, You don't have permission to access!")

    def get_loan(self, user, amount):
        if self.get_loan_feature_status == False:
            print(f"Sorry {user.name}, The Loan Feature is not Available Right Now")
        elif amount > self.__available_balance:
            print (f"Unavailable to Provide Loan of {amount}")
        elif user.account_number in self.__users_list and user.take_loan(amount):
            self.__available_balance -= amount
            self.set_loan_amount(amount)
            
    
    # Organizational Section
    def create_account_holder(self, user):
        while True:
            # created an 12 digits user account number
            account_number = random.randint(100000000000, 900000000000)
            if account_number not in self.__users_list:
                user.set_account_number(account_number)
                self.__users_list[account_number] = user
                break
    
    def create_admin_user(self, user):
        if user.security_key == self.__security_key:
            while True:
                 # created 4 digits admin pin number
                pin_number = random.randint(1000, 9000)
                if pin_number not in self.__admins_list:
                    user.set_pin_number(pin_number)
                    self.__admins_list[pin_number] = user
                    break
        else: 
            print(f"Sorry {user.name}, You can't be an admin. Invalid Security-Key!")
            return None
    
    def __repr__(self) -> str:
        print(" ________________________________________")
        print("|                                        |")
        print("|             Bank Details               |")
        print("|________________________________________|")
        print()
        print(f"Name of the Bank: {self.bank_name}")
        print(f"Address: {self.address}")
        print(f"Number of Account Holders: {len(self.__users_list)}")

        print(" ________________________________________")
        print("|                                        |")
        print("|         Account Holders List           |")
        print("|________________________________________|")
        print()
        for key, value in self.__users_list.items():
            print(f"A/C Name: {value.name}, Age: {value.age}")
            print(f"A/C Number: {key}")
            print(f"A/C Balace: {value.get_balance}")
            print(f"Transaction History:")
            for key in value.transaction_history:
                print(f"- {key}")
            print("----------------------")
    
        print(" ________________________________________")
        print("|                                        |")
        print("|         Admin Accounts List            |")
        print("|________________________________________|")
        print()
        for key, value in self.__admins_list.items():
            print(f"Admin Name: {value.name}, Age: {value.age}")
            print(f"Admin Pin: {key}")
            print("----------------------")
        return ""
    
