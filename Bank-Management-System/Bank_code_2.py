from Bank_Main import *
import sys
import random
import mysql.connector as mc


class use(bankAccount):

    def __init__(self, owner_name, age, g_mail, ph_num1, ad_num1, pc_num, password, account_number, balance1, loan_bal,
                 m_pin, c_bill_s):
        super().__init__(owner_name, account_number, balance1, m_pin, c_bill_s)
        self.age = age
        self.g_mail = g_mail
        self.ph_num = ph_num1
        self.ad_num = ad_num1
        self.pc_num = pc_num
        self.password = password
        self.loan_bal = loan_bal

    def loan_balance(self):
        self.my_cursor.execute(f'select loan_bal from user_info where Account_number = {self.account_number}')
        my_result = self.my_cursor.fetchone()
        for i in my_result:
            print(Fore.LIGHTBLUE_EX + ' Loan Balance : ' + Style.RESET_ALL, i,'.00')

    def update(self):
        try:
            self.my_cursor.execute(
                f'update user_info SET balance = {self.balance} where Account_number = {self.account_number}')
            self.my_cursor.execute(
                f'update user_info SET loan_bal = {self.loan_bal} where Account_number = {self.account_number}')
            self.my_cursor.execute(
                f'update user_info SET c_bill = {self.c_bill_s} where Account_number = {self.account_number}')
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)

    def display(self):
        if self.c_bill_s < 15:
            self.c_bill_s+= 10
            try:
                mydb = mc.connect(host="localhost", user="root", password="naveen", database='Bank_Management_System')
                my_cursor = mydb.cursor()
                quarry = 'insert into user_info(name, age, e_mail, pass, ph_num, ad_num, pc_num,' \
                         ' balance, loan_bal, m_pin, c_bill) ' \
                         'values("{}",{}, "{}", "{}", {}, {}, "{}", {}, {}, {}, {})'.format(self.Owner_name, self.age,
                                                                                            self.g_mail, self.password,
                                                                                            self.ph_num, self.ad_num,
                                                                                            self.pc_num, self.balance,
                                                                                            self.loan_bal, self.m_pin,
                                                                                            self.c_bill_s)
                my_cursor.execute(quarry)
                mydb.commit()
            except Exception as e:
                print(' create account again')
                raise Exception(e)
            else:
                try:
                    mydb = mc.connect(host="localhost", user="root", password="naveen",
                                      database='Bank_Management_System')
                    my_cursor = mydb.cursor()
                    my_cursor.execute(f'select Account_number from user_info where e_mail = "{self.g_mail}"')
                    my_result = my_cursor.fetchone()
                    for i in my_result:
                        self.account_number = i
                    mydb.commit()
                    my_cursor.execute(
                        f'update bank_info set Account_num_c = {self.account_number} where IFSC_CODE = "BANK0FT6UTH1"')
                except Exception as e:
                    raise Exception(' Something Wrong :', e)
                else:
                    mydb = mc.connect(host="localhost", user="root", password="naveen",
                                                   database='Bank_Transaction_History')

                    mycurser = mydb.cursor()
                    k = 's'+ str(self.account_number)

                    mycurser.execute(
                        f'create table {str(k)}(Date varchar(30), Time varchar(30),'
                        f' Description varchar(100), Deposit int(30), Money_Tr int(30), loan_bal int(30),'
                        f' payed_loan_bal int(30), Operation varchar(30), main_balance Bigint(30))')
            print(Fore.BLUE + 'Your Account Successfully Created' + Style.RESET_ALL)
            print(f' Name                            : {self.Owner_name}\n'
                  f' E-Mail                          : {self.g_mail}\n'
                  f' Age                             : {self.age}\n'
                  f' Phone-Number                    : {self.ph_num}\n'
                  f' Account-Number                  : {self.account_number}\n'
                  f' Balance                         : {self.balance}.00')
        else:
            raise Exception(' Something Wrong')

    def display2(self):
        m_pin = int(input(' enter PIN                       : '))
        if m_pin == self.m_pin:
            print("*" * 90)
            try:
                self.my_cursor.execute(f'select * from user_info where Account_number = {self.account_number}'
                                       f' and e_mail = "{self.g_mail}";')
                my_result = self.my_cursor.fetchall()
                for i in my_result:
                    self.account_number = i[0]
                    self.Owner_name = i[1]
                    self.age = i[2]
                    self.g_mail = i[3]
                    self.password = i[4]
                    self.ph_num = i[5]
                    self.ad_num = i[6]
                    self.pc_num = i[7]
                    self.balance = i[8]
                    self.loan_bal = i[9]
                    self.m_pin = i[10]
                    self.c_bill_s = i[11]
                self.mydb.commit()
            except Exception as e:
                raise Exception(e)
            else:
                print(Fore.LIGHTBLUE_EX + ' ------------ ACCOUNT INFORMATION -------------' + Style.RESET_ALL)
                print(f' Name                            : {self.Owner_name}\n'
                      f' E-Mail                          : {self.g_mail}\n'
                      f' Age                             : {self.age}\n'
                      f' Phone-Number                    : {self.ph_num}\n'
                      f' Account-Number                  : {self.account_number}\n'
                      f' Balance                         : {self.balance}.00\n'
                      f' IFSE-CODE                       : BANK0FT6UTH1')
        else:
            print(Fore.LIGHTRED_EX+' INVALID PIN'+Style.RESET_ALL)

    def bank_loan(self, var):
        if self.c_bill_s >= 50:
            m_pin = int(input(' enter PIN                       : '))
            if m_pin == self.m_pin:
                self.c_bill_s = self.c_bill_s + 5
                self.balance = self.balance + var
                self.loan_bal = self.loan_bal + var
                amount = 0
                try:
                    try:
                        self.my_cursor.execute(' select BanK_Balance from bank_info where IFSC_CODE = "BANK0FT6UTH1"')
                        my_result = self.my_cursor.fetchone()
                        for i in my_result:
                            amount = i
                        self.mydb.commit()
                    except Exception as e:
                        self.mydb.rollback()
                        print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)
                    self.my_cursor.execute(
                        f'update bank_info set Bank_Balance = {amount} - {var} where IFSC_CODE = "BANK0FT6UTH1"')
                    self.mydb.commit()
                except Exception as e:
                    self.mydb.rollback()
                    print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)
                else:
                    t = datetime.datetime.now()
                    k = 's' + str(self.account_number)
                    self.my_cursor1.execute(
                        ' insert into ' + str(k) + '(Date, Time ,Description, loan_bal, Operation,'
                        ' main_balance) values("{}", "{}", "{}", {}, "{}", {})'.format(
                            t.date(), t.time(),
                            f"bank loan approved for A/c: "
                            f"{str(self.account_number)}",
                            var, "+", self.balance))
                    self.mydb1.commit()

                print(Fore.LIGHTBLUE_EX + " Account Balance : " + Style.RESET_ALL, self.balance, '.00')
            else:
                print(Fore.LIGHTRED_EX+' INVALID PIN'+Style.RESET_ALL)
        else:
            print(Fore.YELLOW + ' your C-Bill is less, so you not eligible for loan' + Style.RESET_ALL)

    def pay_loan(self):
        if self.loan_bal > 0:
            m_pin = int(input(' enter PIN                       : '))
            if m_pin == self.m_pin:
                print(Fore.LIGHTBLUE_EX + ' YOUR LOAN BALANCE : ' + Style.RESET_ALL, self.loan_bal)
                var = int(input(' enter amount                    : '))
                if self.loan_bal >= var:
                    self.c_bill_s += 5
                    self.loan_bal -= var
                    amount = 0
                    try:
                        try:
                            self.my_cursor.execute(
                                ' select BanK_Balance from bank_info where IFSC_CODE = "BANK0FT6UTH1"')
                            my_result = self.my_cursor.fetchone()
                            for i in my_result:
                                amount = i
                        except Exception as e:
                            print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)
                        self.my_cursor.execute(
                            f'update bank_info set Bank_Balance = {amount} + {var} where IFSC_CODE = "BANK0FT6UTH1"')
                        self.mydb.commit()
                    except Exception as e:
                        self.mydb.rollback()
                        print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)
                    else:
                        print(Fore.LIGHTBLUE_EX + ' LOAN PAYMENT SUCCESSFUL ' + Style.RESET_ALL)
                        t = datetime.datetime.now()
                        self.my_cursor1.execute(
                            f' update "{"s"+str(self.account_number)}" SET Date = {t.date()}, SET Time = {t.time()}'
                            f'SET Description = "loan-balance payed to A/c: {self.account_number}", SET payed_loan_bal = {var},'
                            f'SET Operation = " ", SET main_balance = {self.balance} ')
                        k = 's' + str(self.account_number)
                        self.my_cursor1.execute(
                            ' insert into ' + str(k) + '(Date, Time ,Description, Money_Tr, Operation,'
                            ' main_balance) values("{}", "{}", "{}", {}, "{}", {})'.format(
                                t.date(), t.time(),
                                f"loan-balance payed for A/c: "
                                f"{str(self.account_number)}",
                                var, " ", self.balance))
                        self.mydb1.commit()
                        self.mydb1.commit()
                    print(Fore.LIGHTBLUE_EX + ' Account Balance                 : ' + Style.RESET_ALL, self.balance, '.00')
                    print(Fore.LIGHTBLUE_EX + ' Loan Balance                    : ' + Style.RESET_ALL, self.loan_bal, '.00')
                else:
                    print(Fore.LIGHTYELLOW_EX + ' INVALID AMOUNT' + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX+' INVALID PIN'+Style.RESET_ALL)
        elif self.loan_bal == 0:
            print(Fore.LIGHTRED_EX + ' YOU HAVE NO LOAN BALANCE' + Style.RESET_ALL)

    def edit_option(self):
        for i4 in range(0, 10):
            print('*' * 90)
            print(Fore.BLUE, '-------------------SECURITY PORTAL--------------------', Style.RESET_ALL)
            print(f'|----------------------|               |-----------------------|\n'
                  f'| 1. Edit E-Mail       |               | 2. Edit Phone-Number  |\n'
                  f'|----------------------|               |-----------------------|\n'
                  f'                                                                \n'
                  f'|----------------------|               |-----------------------|\n'
                  f'| 3. Edit Account PIN  |               | 4. Edit password      |\n'
                  f'|----------------------|               |-----------------------|\n'
                  f'                                                                \n'
                  f'|----------------------|               |-----------------------|\n'
                  f'| 5. Home Page         |               | 6. Delete Account     |\n'
                  f'|----------------------|               |-----------------------|\n')
            print('*' * 90)
            opt = input(" enter your option               : ")
            # Edit E-MAIL
            if opt == '1':
                pass_word = input(' enter password                  : ')
                if self.password == pass_word:
                    new_g_mail = str(input(' enter New E-Mail                : '))
                    for i1 in range(len(new_g_mail)):
                        if '@' == new_g_mail[i1]:
                            break
                    else:
                        print(Fore.LIGHTRED_EX+' INVALID E-MAIL'+Style.RESET_ALL)
                        break
                    self.g_mail = new_g_mail
                    try:
                        quarry = f'update user_info SET e_mail ="{self.g_mail}" where Account_number ={self.account_number} '
                        self.my_cursor.execute(quarry)
                        self.mydb.commit()
                    except Exception as e:
                        print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                        self.mydb.rollback()
                    print(' new E-Mail                      : ', self.g_mail)
                else:
                    print(Fore.LIGHTRED_EX + ' invalid password, try again later' + Style.RESET_ALL)
            # Edit Phone-Number
            elif opt == '2':
                for i3 in range(1):
                    old_phn = int(input(' enter Phone-Number              : '))
                    if self.ph_num == old_phn:
                        otp2 = random.randint(00000, 99999)
                        print(Fore.LIGHTBLUE_EX + ' OTP SENT SUCCESSFULLY' + Style.RESET_ALL)
                        print('-' * 60)
                        print(Fore.GREEN + ' MESSAGE : THIS IS ONE TIME PASSWORD ' + Style.RESET_ALL, otp2, Fore.GREEN +
                              ' DO NOT SHARE WITH ANY ONE' + Style.RESET_ALL)
                        print('-' * 60)
                        otp3 = int(input(' enter OTP                       : '))
                        if otp2 == otp3:
                            new_num = int(input(' enter New Phone Number          : '))
                            if new_num == self.ph_num:
                                count1 = 0
                                for i2 in range(0, 3):
                                    if new_num in range(6000000000, 9999999999):
                                        print(Fore.LIGHTBLUE_EX + f' {new_num} VALIDATED SUCCESSFULLY')
                                        print(' OTP SENT SUCCESSFULLY' + Style.RESET_ALL)
                                        break
                                    elif count1 <= 2:
                                        print(Fore.LIGHTRED_EX + ' INVALID PHONE NUMBER' + Style.RESET_ALL)
                                        new_num = int(input(' enter correct phone number      : '))
                                        count1 = count1 + 1
                                    elif count1 == 3:
                                        print(
                                            Fore.LIGHTRED_EX + ' REACHED THE LIMIT, TRY AGAIN LATER' + Style.RESET_ALL)
                                otp11 = random.randint(00000, 99999)
                                print("-" * 60)
                                print(Fore.GREEN + ' MESSAGE : THIS IS ONE TIME PASSWORD ----" ' + Style.RESET_ALL,
                                      otp11,
                                      Fore.GREEN + ' "---- DO NOT SHARE WITH ANY ONE. ' + Style.RESET_ALL)
                                print("-" * 60)
                                otp22 = int(input(' enter OPT                       : '))
                                count1 = 0
                                for i11 in range(0, 3):
                                    if otp11 == otp22:
                                        print(Fore.LIGHTBLUE_EX + ' OTP VALIDATED SUCCESSFULLY' + Style.RESET_ALL)
                                        self.ph_num = new_num
                                        try:
                                            quarry = f"update user_info SET ph_num ={new_num} where Account_number" \
                                                     f" = {self.account_number} "
                                            self.my_cursor.execute(quarry)
                                            self.mydb.commit()
                                        except Exception as e:
                                            print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                                            self.mydb.rollback()
                                        print(' Phone Number updated Successfully : ', self.ph_num)
                                        break
                                    elif count1 <= 2:
                                        print(Fore.LIGHTRED_EX + ' INVALID OTP' + Style.RESET_ALL)
                                        otp22 = int(input(' enter correct OTP               : '))
                                        count1 = count1 + 1
                                    elif count1 == 3:
                                        print(
                                            Fore.LIGHTRED_EX + ' REACHED THE LIMIT, TRY AGAIN LATER' + Style.RESET_ALL)
                                        break
                            else:
                                print(Fore.LIGHTRED_EX+' PLEASE ENTER NEW PHONE-NUMBER '+Style.RESET_ALL)
                                break
                        else:
                            print(Fore.LIGHTRED_EX + ' INVALID OTP, TRY AGAIN LATER' + Style.RESET_ALL)
                            break
                    else:
                        print(Fore.LIGHTRED_EX + ' INVALID PHONE-NUMBER, TRY AGAIN LATER' + Style.RESET_ALL)
                        break
            # Edit M-PIN
            elif opt == '3':
                o_pin = int(input(' enter current PIN               : '))
                if self.m_pin == o_pin:
                    pin1 = int(input(' enter New PIN                   : '))
                    count1 = 0
                    for i2 in range(0, 3):
                        if pin1 in range(0000, 9999):
                            break
                        elif count1 <= 2:
                            print(Fore.LIGHTRED_EX + ' PIN NUMBER MUST BE WITH IN 4 DIGITS RANGE' + Style.RESET_ALL)
                            pin1 = int(input(' enter valid PIN                 : '))
                            count1 = count1 + 1
                        elif count1 == 3:
                            print(Fore.LIGHTRED_EX + ' REACHED THE LIMIT, TRY AGAIN LATER' + Style.RESET_ALL)
                            break
                    pin2 = int(input(' conform PIN                     : '))
                    for i11 in range(0, 3):
                        if pin1 == pin2:
                            print(' PIN Created Successfully ')
                            print('*' * 90)
                            self.m_pin = pin2
                            self.my_cursor.execute(f'update user_info SET m_pin = {self.m_pin}'
                                                   f' where Account_number = {self.account_number}')
                            self.mydb.commit()
                            break
                        elif count1 <= 2:
                            print(Fore.LIGHTRED_EX + ' INVALID PIn' + Style.RESET_ALL)
                            pin2 = int(input(' enter Valid PIN                 : '))
                            count1 = count1 + 1
                        elif count1 == 3:
                            print(Fore.LIGHTRED_EX + ' REACHED THE LIMIT, TRY AGAIN LATER' + Style.RESET_ALL)
                            break
                else:
                    print(Fore.LIGHTRED_EX + ' INVALID PIN, TRY AGAIN LATER' + Style.RESET_ALL)
                    break
            elif opt == '4':
                if True:
                    o2 = random.randint(00000, 99999)
                    print('-' * 80)
                    print(Fore.GREEN + ' MESSAGE : THIS IS ONE TIME PASSWORD ----" ' + Style.RESET_ALL, o2,
                          Fore.GREEN + ' "---- DO NOT SHARE WITH ANY ONE. ' + Style.RESET_ALL)
                    print('-' * 80)
                    o3 = int(input(' enter otp                       :'))
                    count = 0
                    for i in range(0, 3):
                        if o2 == o3:
                            print(Fore.LIGHTBLUE_EX + ' OTP VALIDATED SUCCESSFULLY' + Style.RESET_ALL)
                            new_pss = input(' enter new Password              : ')
                            new_pss1 = input(' conform new password            : ')
                            for i1 in range(0, 3):
                                if new_pss == new_pss1:
                                    self.password = new_pss1
                                    try:
                                        quarry = f"update user_info SET pass ={new_pss1} where Account_number = " \
                                                 f"{self.account_number} "
                                        self.my_cursor.execute(quarry)
                                        self.mydb.commit()
                                    except Exception as e:
                                        print(Fore.LIGHTRED_EX, "EXCEPTION : ", e, Style.RESET_ALL)
                                        self.mydb.rollback()
                                    print(Fore.LIGHTBLUE_EX + ' Password updated successfully' + Style.RESET_ALL)
                                elif i1 <= 2:
                                    print(Fore.LIGHTRED_EX + ' INVALID PASSWORD' + Style.RESET_ALL)
                                    new_pss1 = input(' conform new password            : ')
                                else:
                                    sys.exit(' REACHED THE LIMIT, TRY AGAIN LATER')
                            break
                        elif count <= 2:
                            print(Fore.LIGHTRED_EX + ' INVALID OTP' + Style.RESET_ALL)
                            o3 = int(input(' enter correct OTP               : '))
                            count = count + 1
                        elif count == 3:
                            sys.exit(' REACHED THE LIMIT, TRY AGAIN LATER')
            elif opt == '5':
                break
            elif opt == '6':
                m_pin = int(input(' enter PIN                       : '))
                if m_pin == self.m_pin:
                    paa = input(' enter your password             : ')
                    if self.password == paa:
                        print(Fore.LIGHTBLUE_EX+" NOTE : once account is deleted, you can't get anything back "+Style.RESET_ALL)
                        if self.balance > 0:
                            print(Fore.LIGHTRED_EX + " NOTE : Please Withdrawal the money " + Style.RESET_ALL)
                            print(f' Your Account Balance            : {self.balance}')
                        print(Fore.LIGHTBLUE_EX + ' Note : say yes or no ' + Style.RESET_ALL)
                        i4 = input(' Conform                         : ')
                        if i4 in ('yes', 'ok', 'OK', 'Ok', 'YES', 'Yes'):
                            try:
                                quarry = f"delete from user_info where Account_number = {self.account_number}"
                                self.my_cursor.execute(quarry)
                                self.mydb.commit()
                            except Exception as e:
                                print(Fore.LIGHTRED_EX + ' EXCEPTION : ' + Style.RESET_ALL, e)
                                self.mydb.rollback()
                            else:
                                self.mydb.close()
                                sys.exit(' your account has been deleted, you can not get anything back , \n'
                                         ' THANK YOU FOR USING THE BANK, vesit again')
                        else:
                            break
                    else:
                        print(Fore.LIGHTRED_EX + ' Invalid Password' + Style.RESET_ALL)
                else:
                    print(Fore.LIGHTBLUE_EX + ' INVALID PIN ' + Style.RESET_ALL)
