from Bank import Bank
from Account import User, Admin

def main():
    abc_bank = Bank('ABC Bank', 'Uttara, Dhaka', 1000)
    user_1 = User('Tithi Paul', '25', '123456789', 'Barishal')
    user_2 = User('Madhu Shaha', '32', '923456789', 'Dhaka')
    abc_bank.create_account_holder(user_1)
    abc_bank.create_account_holder(user_2)

    abc_bank.deposit_balance(user_1, 50)
    abc_bank.deposit_balance(user_2, 80)
    abc_bank.withdrawal_balance(user_1, 60)
    abc_bank.withdrawal_balance(user_2, 20)

    abc_bank.balance_transfer(user_1, 25, user_2)
    abc_bank.balance_transfer(user_2, 45, user_1)

    abc_bank.get_loan(user_1, 100)
    abc_bank.get_loan(user_2, 200)
    abc_bank.get_loan(user_2, 75)

    user_1.check_total_balace()
    user_2.check_total_balace()

    admin_1 = Admin('Ben', '65', '333456789', 'security123')
    admin_2 = Admin('Jhon', '35', '723456789', 'security123')
    admin_3 = Admin('Rahim', '25', '623456789', 'nosecuritykey')
    abc_bank.create_admin_user(admin_1)
    abc_bank.create_admin_user(admin_2)
    abc_bank.create_admin_user(admin_3)

    abc_bank.check_total_balance(admin_1)
    abc_bank.check_loan_ammount(admin_1)
    abc_bank.set_loan_feature_status(False, admin_1)

    abc_bank.get_loan(user_1, 100)
    abc_bank.set_loan_feature_status(False, user_1)

    print(abc_bank)

if __name__ == '__main__':
    main()