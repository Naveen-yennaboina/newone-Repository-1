from Bank_code_2 import *
import sys
from colorama import Back
import random

if __name__ == '__main__':

    print('', '*' * 100, '\n',
          '------------------------------------' + Back.MAGENTA + '"WELCOME TO BANK OF TRUTH"' + Style.RESET_ALL +
          '-----------------------------------',
          '\n', '*' * 100, '\n')
    print('-' * 70)
    print(' enter "C" for creating account')
    print(' enter "L" for login into account')
    print('-' * 70)
    create = input(' enter your option               : ')
    if create in ('L', 'l', 'login', 'Login'):
        user_name = input(' E-MAIL                          : ')
        pass1 = input(' PASSWORD                        : ')
        account_number, balance, loan_bal, m_pin, c_bill, ph_num, ad_num, age = 0, 0, 0, 0, 0, 0, 0, 0
        name, e_mail, pc_num, password = '', '', '', ''
        try:
            bankAccount.my_cursor.execute(f'select * from user_info where e_mail = "{user_name}" and pass = {pass1};')
            my_result = bankAccount.my_cursor.fetchall()
            for i in my_result:
                account_number = i[0]
                name = i[1]
                age = i[2]
                e_mail = i[3]
                password = i[4]
                ph_num = i[5]
                ad_num = i[6]
                pc_num = i[7]
                balance = i[8]
                loan_bal = i[9]
                m_pin = i[10]
                c_bill = i[11]
            if account_number == 0 and age == 0 and ph_num == 0 and m_pin == 0 and ad_num == 0:
                raise Exception(' INVALID E-MAIL OR PASSWORD')
        except Exception:
            raise Exception(' INVALID PASSWORD OR E-MAIL')
        else:
            account1 = use(name, age, e_mail, ph_num, ad_num, pc_num, password, account_number, balance, loan_bal,
                           m_pin, c_bill)
            account1.display2()

    elif create in ('create', 'Create', 'c', 'C'):  # ----------creating account
        while True:
            print(Fore.CYAN + ' CREATE BANK ACCOUNT' + Style.RESET_ALL)
            # name ----------------------------------------------------- Name
            name = input(' enter name                      : ')
            # age------------------------------------------------------- Age
            try:
                ag = int(input(' enter age                       : '))
            except ValueError as e:
                print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                try:
                    ag = int(input(' enter age                       : '))
                except ValueError as e1:
                    raise ValueError(' INVALID INFO')
            # E-mail-----------------------------------------------------E-mail
            email = input(' enter E-Mail                    : ')
            for i1 in range(len(email)):
                if '@' == email[i1]:
                    break
            else:
                sys.exit(' invalid e_mail')
            # phone number -------------------------------------------- phone number
            ph_num = 0
            try:
                ph_num = int(input(' enter Phone Number              : '))
            except ValueError as e:
                print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                try:
                    ph_num = int(input(' enter Phone Number              : '))
                except ValueError as e1:
                    raise ValueError(' INVALID INFO')
            count = 0
            for i in range(0, 3):
                if ph_num in range(6000000000, 9999999999):
                    print(Fore.LIGHTBLUE_EX + f' {ph_num} VALIDATED SUCCESSFULLY')
                    print(' OTP SENT SUCCESSFULLY' + Style.RESET_ALL)
                    break
                elif count <= 2:
                    print(Fore.LIGHTRED_EX + ' INVALID PHONE NUMBER' + Style.RESET_ALL)
                    ph_num = int(input(' enter valid phone number     : '))
                    count = count + 1
                elif count == 3:
                    sys.exit(' REACHED THE LIMIT, TRY AGAIN LATER')
            # OTP -----------------------------------------------------OTP
            otp1 = random.randint(00000, 99999)
            print("-" * 60)
            print(Fore.GREEN + ' MESSAGE : THIS IS ONE TIME PASSWORD ----" ' + Style.RESET_ALL, otp1,
                  Fore.GREEN + ' "---- DO NOT SHARE WITH ANY ONE. ' + Style.RESET_ALL)
            print("-" * 60)
            otp = 0
            try:
                otp = int(input(' enter OTP                       : '))
            except ValueError as e:
                print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                try:
                    otp = int(input(' enter OTP                       : '))
                except ValueError as e1:
                    print(Fore.LIGHTRED_EX, "EXCEPTION : ", e1, Style.RESET_ALL)

            count = 0
            for i in range(0, 3):
                if otp1 == otp:
                    print(Fore.LIGHTBLUE_EX + ' OTP VALIDATED SUCCESSFULLY' + Style.RESET_ALL)
                    break
                elif count <= 2:
                    print(Fore.LIGHTRED_EX + ' INVALID OTP' + Style.RESET_ALL)
                    otp = int(input(' enter correct OTP               : '))
                    count = count + 1
                elif count == 3:
                    sys.exit(' REACHED THE LIMIT, TRY AGAIN LATER')
            print("-" * 60)
            print(Fore.GREEN + ' MESSAGE : MAKE SURE  AADHER MUST BE CONNECTED WITH PHONE NUMBER' + Style.RESET_ALL)
            print("-" * 60)
            # addhar number----------------------------------Aadher Number
            ad_num = 0
            try:
                ad_num = int(input(' enter Aadher Number             : '))
            except ValueError as e:
                print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                try:
                    ad_num = int(input(' enter Valid Aadher Number    : '))
                except ValueError as e1:
                    print(Fore.LIGHTRED_EX, "EXCEPTION : ", e1, Style.RESET_ALL)
            count = 0
            for i in range(0, 3):
                if ad_num in range(100000000000, 999999999999):
                    break
                elif count <= 2:
                    print(Fore.LIGHTRED_EX + ' INVALID AADHER NUMBER' + Style.RESET_ALL)
                    ad_num = int(input(' enter Valid Aadher number       : '))
                    count = count + 1
                    continue
                elif count == 3:
                    sys.exit(' -------------> REACHED THE LIMIT, TRY AGAIN LATER <-------------')
            # pan-cord number --------------------------------------PAN-CORD NUMBER
            pan_num = input(' enter PAN-CARD Number           : ')
            count = 1
            for i in range(0, 3):
                if len(pan_num) == 10:
                    print(Fore.LIGHTBLUE_EX + f' {pan_num} VALIDATED SUCCESSFULLY' + Style.RESET_ALL)
                    break
                elif count <= 2:
                    print(Fore.LIGHTRED_EX + ' INVALID PAN_CORD NUMBER' + Style.RESET_ALL)
                    pan_num = input(' enter Valid PAN-CARD Number     : ')
                    count = count + 1
                elif count == 3:
                    sys.exit(' REACHED THE LIMIT, TRY AGAIN LATER')
            # password --------------------------------------------- PASSWORD
            pss = input(' create password                 : ')
            pss2 = input(' conform password                : ')
            count = 0
            for i in range(0, 3):
                if pss == pss2:
                    break
                elif count <= 2:
                    print(Fore.LIGHTRED_EX + ' INVALID PASSWORD' + Style.RESET_ALL)
                    pss2 = input(' conform password                : ')
                    count = count + 1
                elif count == 3:
                    sys.exit(' -----------> REACHED THE LIMIT, TRY AGAIN LATER <-------------')
            # conform account creation
            conf = input(' conform account creation        : ')
            if conf in ('Yes', 'yes', 'YES', 'Y', 'y', 'OK', 'ok'):
                balance = 0.00
                loan_bal = 0.00
                account_num = 0
                c_bill = 0
                # create m-pin----------------------------- M-PIN
                m_pin = int(input(' create M-PIN                    : '))
                m_pin1 = int(input(' conform M-PIN                   : '))
                count = 0
                for i in range(0, 3):
                    if m_pin == m_pin1:
                        break
                    elif count <= 2:
                        print(Fore.LIGHTRED_EX + " INVALID M-PIN " + Style.RESET_ALL)
                        m_pin1 = int(input(' conform M-PIN                   : '))
                        count += 1
                    elif count == 3:
                        sys.exit(' -------------- TRY AGAIN LATER --------------')
                print('*' * 90)
                account1 = use(name, ag, email, ph_num, ad_num, pan_num, pss2, account_num, balance, loan_bal, m_pin1,
                               c_bill)
                account1.display()
                break
    else:
        sys.exit(' INVALID ENTRY ')


    def person2():
        for q in range(0, 3):
            while True:
                j = 1
                for g in range(j):
                    print('*' * 90)
                    print(Fore.BLUE + ' ------------------- HELLO', name.upper(),
                          ' ------------------' + Style.RESET_ALL)
                    print(f'|----------------|               |------------------|\n'
                          f'|  1. Deposit    |               |  6.Loan Balance  |\n'
                          f'|----------------|               |------------------|\n'
                          f'                                                     \n'
                          f'|----------------|               |------------------|\n'
                          f'|2.Money Transfer|               |  7. pay Loan     |\n'
                          f'|----------------|               |------------------|\n'
                          f'                                                     \n'
                          f'|-------  -------|               |------------------|\n'
                          f'|  3.Balance     |               |  8. C-Bill Score |\n'
                          f'|------  --------|               |------------------|\n'
                          f'                                                     \n'
                          f'|----------------|               |------------------|\n'
                          f'| 4.Account_info |               |  9. Security     |\n'
                          f'|----------------|               |------------------|\n'
                          f'                                                     \n'
                          f'|----------------|               |------------------|\n'
                          f'|  5.Bank Loan   |               |  10. Exit        |\n'
                          f'|----------------|               |------------------|\n'
                          f'|---------------------------------------------------|\n'
                          f'|            11. Transaction History                |\n'
                          f'|---------------------------------------------------|')
                    print('*' * 90)
                    opt = input(' enter your option               : ')
                    if opt == '1':  # adding money
                        try:
                            print(Fore.LIGHTCYAN_EX + ' PROCESSING......' + Style.RESET_ALL)
                            account1.deposit()
                            account1.update()
                        except Exception as e3:
                            print(Fore.LIGHTRED_EX + ' Please Enter Valid Information  : ' + Style.RESET_ALL, e3)
                    elif opt == '2':  # money transfer
                        try:
                            var1 = int(input(' Account-Number                  : '))
                            var11 = int(input(' Re-enter Account_Number         : '))
                            var2 = input(' Account-Holder name             : ')
                            var3 = input(' IFSC-CODE                       : ')
                            if var1 == var11:
                                print(Fore.LIGHTCYAN_EX + ' PROCESSING......' + Style.RESET_ALL)
                                account1.transfer_money(var11, var2, var3)
                                account1.update()
                        except Exception as e3:
                            print(Fore.LIGHTRED_EX + ' Please Enter Valid Information  : ' + Style.RESET_ALL, e3)
                    elif opt == '3':  # checking account balance
                        account1.check_acc_bal()
                    elif opt == '4':
                        print(Fore.LIGHTCYAN_EX + ' PROCESSING......' + Style.RESET_ALL)
                        account1.display2()
                    elif opt == '5':  # applying bank loan
                        try:
                            bal = int(input(' enter amount for loan           : '))
                            tim = int(input(' enter time in days              : '))
                            account1.bank_loan(bal)
                            account1.update()
                        except Exception as e2:
                            print(Fore.LIGHTRED_EX + ' Please Enter Valid Information  : ' + Style.RESET_ALL, e2)
                    elif opt == '6':  # checking loan balance
                        account1.loan_balance()
                    elif opt == '7':  # paying loan balance
                        try:
                            account1.pay_loan()
                            account1.update()
                        except Exception as e3:
                            print(Fore.LIGHTRED_EX + ' Please Enter Valid Information  : ' + Style.RESET_ALL, e3)
                    elif opt == '8':  # checking c_bill score
                        account1.c_bill_score()
                    elif opt == '9':  # security option
                        account1.edit_option()
                        account1.update()
                    elif opt == '10':  # exit
                        bankAccount.mydb.close()
                        sys.exit(' "------------> THANK YOU, HAVE A NICE DAY <------------"')
                    elif opt == '11':  # transaction history
                        print(Fore.LIGHTRED_EX + ('*' * 110) + Style.RESET_ALL)
                        account1.tr_history()
                        print(Fore.LIGHTRED_EX + ('*' * 110) + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTRED_EX + ' INVALID OPTION' + Style.RESET_ALL)
                    print(' -------*--------*--------*--------')
                    opt1 = input(' do you want to continue         : ')
                    for v in range(0, 3):
                        if opt1 in ('yes', 'YES', 'Yes', 'Y', 'y', 'OK', 'Ok', 'ok'):
                            j = j + 1
                            break
                        elif opt1 in ('no', 'No', 'N', 'n', 'NO'):
                            bankAccount.mydb.close()
                            sys.exit(' "------------>THANK YOU , VISIT AGAIN<------------"')
                        elif v <= 3:
                            print(Fore.LIGHTRED_EX + '  INVALID OPTION , TRY AGAIN' + Style.RESET_ALL)
                            opt1 = input(' do you want to continue         : ')
                            v += 1
                        else:
                            sys.exit(' "------------>THANK YOU , VISIT AGAIN<------------"')


    person2()
