from colorama import Fore, Style
import mysql.connector as mc
from prettytable import PrettyTable
import datetime


class bankAccount:
    mydb = mc.connect(host="localhost", user="root", password="15c11a0237", database='Bank_Management_System')
    my_cursor = mydb.cursor()

    def __init__(self, owner_name, account_number, balance1, m_pin, c_bill_s):
        self.Owner_name = owner_name
        self.account_number = account_number
        self.balance = balance1
        self.m_pin = m_pin
        self.c_bill_s = c_bill_s
        self.mydb = bankAccount.mydb
        self.my_cursor = bankAccount.my_cursor

        if 1000 > self.balance and self.c_bill_s >= 50:
            print(Fore.LIGHTRED_EX + '"------LOW ACCOUNT BALANCE FEE : 200 ------"' + Style.RESET_ALL)
            amount = 0
            try:
                try:
                    self.my_cursor.execute(' select Bank_Balance from bank_info where IFSC_CODE = "BANK0FT6UTH1"')
                    my_result = self.my_cursor.fetchone()
                    for i in my_result:
                        amount = i
                    self.mydb.commit()
                except Exception as e1:
                    print(Fore.LIGHTRED_EX + "EXCEPTION : " + Style.RESET_ALL, e1)
                quarry = f"update bank_info set Bank_Balance = {amount} + {200} where IFSC_CODE = 'BANK0FT6UTH1'"
                quarry1 = f"update user_info set balance = {self.balance} - {200}" \
                          f" here account = {self.account_number}"
                self.my_cursor.execute(quarry)
                self.my_cursor.execute(quarry1)
                self.mydb.commit()
            except Exception as e:
                print(Fore.LIGHTRED_EX + "EXCEPTION : " + Style.RESET_ALL, e)
                self.mydb.rollback()
            else:
                self.balance = self.balance - 200
                print(Fore.LIGHTBLUE_EX + " Account Balance                 : " + Style.RESET_ALL, self.balance, '.00')

    def tr_history(self):
        try:
            my_table = PrettyTable(['Date', 'Time', "Description", 'Deposit', 'Money-Transfer', 'Loan-Balance',
                                    'Payed-loan-balance', 'Operation', 'Main-Balance'])
            bankAccount.my_cursor.execute(f'select * from {"s" + str(self.account_number)}')
            my_result = bankAccount.my_cursor.fetchall()
            for i in my_result:
                my_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        except Exception as e:
            print(Fore.LIGHTRED_EX + ' Exception : ' + Style.RESET_ALL, e)
        else:
            print(my_table)

    def c_bill_score(self):
        try:
            self.my_cursor.execute(f'select c_bill from user_info where Account_number = {self.account_number}')
            my_result = self.my_cursor.fetchone()
            for i in my_result:
                print(Fore.LIGHTBLUE_EX + ' Account C-Bill Score            : ' + Style.RESET_ALL, i)
        except Exception as e:
            print(Fore.LIGHTRED_EX + "EXCEPTION : " + Style.RESET_ALL, e)

    def check_acc_bal(self):
        try:
            m_pin = int(input(' enter PIN : '))
            if m_pin == self.m_pin:
                self.c_bill_s = self.c_bill_s + 2
                print(Fore.LIGHTBLUE_EX + ' your Account Balance            : ' + Style.RESET_ALL, self.balance, '.00')
            else:
                print(Fore.LIGHTRED_EX + ' INVALID PIN' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)

    def deposit(self):
        try:
            bal = int(input(' enter amount                    : '))
            m_pin = int(input(' enter PIN                       : '))
            if m_pin == self.m_pin:
                self.balance = self.balance + bal
                try:

                    quarry = f"update user_info SET balance = {self.balance}" \
                             f" where Account_number = {self.account_number}"
                    self.my_cursor.execute(quarry)
                    self.mydb.commit()
                except Exception as e:
                    self.balance = self.balance - bal
                    print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                    self.mydb.rollback()
                else:
                    self.c_bill_s = self.c_bill_s + 5
                    print(Fore.LIGHTBLUE_EX + f'Rs.{bal}.00 credited to A/c : {self.account_number}.'
                                              f' total balance : Rs.{self.balance}.00' + Style.RESET_ALL)
                    t = datetime.datetime.now()
                    k = 's' + str(self.account_number)
                    self.my_cursor.execute(
                        ' insert into ' + str(k) + '(Date, Time ,Description, Deposit, Operation,'
                                                   ' main_balance) values("{}", "{}", "{}", {}, "{}", {})'.format(
                            t.date(), t.time(),
                            f"money added to A/c: "
                            f"{str(self.account_number)}",
                            bal, "+", self.balance))
                    self.mydb.commit()

            else:
                print(Fore.LIGHTRED_EX + ' INVALID PIN ' + Style.RESET_ALL)

        except Exception as e:
            print(' EXCEPTION : ', e)

    def transfer_money(self, var_an, var_name, if_se):
        ifsc1 = ''
        try:
            quarry = f"select balance from user_info where Account_number = {var_an}"
            self.my_cursor.execute(quarry)
            bal1 = self.my_cursor.fetchone()
            for i in bal1:
                bal1 = i
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            self.mydb.close()
            raise Exception(e)
        else:
            quarry = f"select balance from user_info where Account_number = {self.account_number}"
            self.my_cursor.execute(quarry)
            bal = self.my_cursor.fetchone()
            for i in bal:
                bal = i
        if bal > 0:
            bal_2 = int(input(' enter amount                    : '))
            m_pin = int(input(' enter PIN                       : '))
            if m_pin == self.m_pin:
                if bal_2 <= bal:
                    try:
                        self.my_cursor = self.mydb.cursor()
                        self.my_cursor.execute('select IFSC_CODE from bank_info')
                        my_result = self.my_cursor.fetchone()
                        for i in my_result:
                            ifsc1 = i
                        if ifsc1 == if_se:
                            try:
                                quarry = f"update user_info SET balance = {self.balance} - {bal_2} " \
                                         f"where Account_number = {self.account_number} "
                                self.my_cursor.execute(quarry)
                                self.mydb.commit()
                                try:
                                    quarry1 = f"update user_info SET balance = {bal1} + {bal_2} where" \
                                              f" Account_number = {var_an}"
                                    self.my_cursor.execute(quarry1)
                                    self.mydb.commit()
                                except Exception as e:
                                    self.mydb.rollback()
                                    self.mydb.close()
                                    raise Exception(e)
                            except Exception as e:
                                print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                                self.mydb.rollback()
                            else:
                                self.balance = self.balance - bal_2
                                self.my_cursor.execute(f'update user_info SET balance = {self.balance}'
                                                       f' where Account_number = {self.account_number}')
                                self.mydb.commit()
                                self.c_bill_s = self.c_bill_s + 5
                                t = datetime.datetime.now()
                                k = 's' + str(self.account_number)
                                self.my_cursor.execute(
                                    ' insert into ' + str(k) + '(Date, Time ,Description, Money_Tr, Operation,'
                                    ' main_balance) values("{}", "{}", "{}", {}, "{}", {})'.format(
                                        t.date(), t.time(),
                                        f"money transfer to A/c: "
                                        f"{str(var_an)}",
                                        bal_2, "-", self.balance))
                                self.mydb.commit()
                                print(Fore.LIGHTBLUE_EX + ' TRANSACTION SUCCESSFUL ' + Style.RESET_ALL)
                    except Exception as e:
                        self.mydb.close()
                        raise Exception(e)
                else:
                    print(Fore.LIGHTRED_EX + " INVALID AMOUNT " + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + " INVALID PIN " + Style.RESET_ALL)
