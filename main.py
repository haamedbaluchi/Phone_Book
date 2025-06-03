class Account:
    def __init__(self, balance=0.0, account_number=""):
        self.current_balance = balance
        self.account_number = account_number

    def get_current_balance(self):
        return self.current_balance

    def set_current_balance(self, balance):
        self.current_balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.current_balance:.2f}"


class Client:
    def __init__(self, name="", last_name="", national_code="", birth_date="", account=None):
        self.name = name
        self.last_name = last_name
        self.national_code = national_code
        self.birth_date = birth_date
        self.account = account if account else Account()

    def set_c_name(self, name):
        self.name = name

    def set_lst_name(self, last_name):
        self.last_name = last_name

    def set_national_code(self, code):
        self.national_code = code

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_account(self, account):
        self.account = account

    def get_national_code(self):
        return self.national_code

    def get_c_account(self):
        return self.account

    def __str__(self):
        return (f"Name: {self.name} {self.last_name}, "
                f"National Code: {self.national_code}, "
                f"Birth Date: {self.birth_date}, {self.account}")


class Employee:
    def __init__(self, name="", last_name="", personal_code="", basic_salary=0.0):
        self.name = name
        self.last_name = last_name
        self.personal_code = personal_code
        self.basic_salary = basic_salary
        self.attendance_time = 0

    def set_p_name(self, name):
        self.name = name

    def set_p_lst_name(self, last_name):
        self.last_name = last_name

    def set_personal_code(self, code):
        self.personal_code = code

    def set_basic_salary(self, salary):
        self.basic_salary = salary

    def set_attendance_time(self, time):
        self.attendance_time = time

    def get_personal_code(self):
        return self.personal_code

    def get_attendance_time(self):
        return self.attendance_time

    def __str__(self):
        return (f"Name: {self.name} {self.last_name}, "
                f"Personal Code: {self.personal_code}, "
                f"Basic Salary: {self.basic_salary:.2f}, "
                f"Attendance Time: {self.attendance_time}")


class Manager(Employee):
    def __init__(self, name="", last_name="", personal_code="", basic_salary=0.0):
        super().__init__(name, last_name, personal_code, basic_salary)
        self.duty_time = 0
        self.birth_date = ""
        self.bank = None

    def set_duty_time(self):
        # این متد در کد C++ به صورت بدون آرگومان صدا زده شده؛ در اینجا می‌توان
        # یا مقدار پیش‌فرض گذاشت یا از کاربر بخواهیم وارد کند. در این پیاده‌سازی،
        # صرفاً مقدار صفر تنظیم شده.
        self.duty_time = 0

    def set_p_birth(self, birth_date):
        self.birth_date = birth_date

    def calculate_salary(self):
        # در کد C++ این متد صدا زده می‌شود اما جزییات محاسبات مشخص نبود.
        # بنابراین یک پیام نمایش داده می‌شود و خود کاربر می‌تواند
        # جزییات محاسبه را اضافه کند.
        print(f"Calculating salary for manager {self.name}... (not implemented)")

    def set_manager_bank(self, bank):
        self.bank = bank

    def show_m_pecifications(self):
        print(f"Manager Specifications: {self}")

    def searching_client(self, bank, national_code):
        for client in bank.clients:
            if client.get_national_code() == national_code:
                print(client)
                return
        print("Client not found!")

    def searching_employee(self, bank, personal_code):
        for emp in bank.employees:
            if emp.get_personal_code() == personal_code:
                print(emp)
                return
        print("Employee not found!")

    def create_new_account(self, client, amount, account_number):
        return Account(balance=amount, account_number=account_number)

    def remove_client(self, bank, national_code):
        bank.remove_client(national_code)

    def add_employee(self, bank, employee):
        bank.add_employee(employee)

    def remove_emoloyee(self, bank, personal_code):
        bank.remove_employee(personal_code)

    def set_attendance_ttime(self, bank, index, time):
        bank.employees[index].set_attendance_time(time)


class Bank:
    def __init__(self):
        self.name = ""
        self.name_of_shobeh = ""
        self.bank_code = 0
        self.clients = []
        self.employees = []
        self.manager = None

    def set_manager_bank(self, manager):
        self.manager = manager

    def unique_client_code(self, code):
        return all(client.get_national_code() != code for client in self.clients)

    def unique_employee(self, code):
        return all(emp.get_personal_code() != code for emp in self.employees)

    def set_client(self, client, index=None):
        if index is None:
            self.clients.append(client)
        else:
            self.clients[index] = client

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_client(self, national_code):
        self.clients = [c for c in self.clients if c.get_national_code() != national_code]

    def remove_employee(self, personal_code):
        self.employees = [e for e in self.employees if e.get_personal_code() != personal_code]

    def get_number_of_personels(self):
        return len(self.employees)

    def get_number_of_clients(self):
        return len(self.clients)


if __name__ == "__main__":
    # معادل این بخش در C++:
    manager = Manager()
    manager.set_p_name("malihe")
    manager.set_p_lst_name("moradi")
    manager.set_duty_time()
    manager.set_p_birth("3/11/1351")
    manager.set_personal_code("838367786384")
    manager.set_attendance_time(60)
    manager.calculate_salary()

    bank = Bank()
    bank.name = "meli"
    bank.name_of_shobeh = "rabor"
    bank.bank_code = 1
    manager.set_manager_bank(bank)

    while True:
        print("1. employee\n2. manager\n3. client\n4. exit")
        try:
            x = int(input())
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if x == 1:
            # زیرمنوی «کارمند» (employee)
            while True:
                print("1. Show Personal Specifications\n"
                      "2. Show Client Specifications\n"
                      "3. Create New Account\n"
                      "4. Remove Client\n"
                      "5. Exit")
                try:
                    y = int(input())
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                if y == 1:
                    personal_code = input("personal code: ")
                    manager.searching_employee(bank, personal_code)

                elif y == 2:
                    national_code = input("enter national code: ")
                    manager.searching_client(bank, national_code)

                elif y == 3:
                    name = input("name: ")
                    famil = input("last name: ")
                    national_code = input("national code: ")
                    birth = input("birth date: ")
                    new_client = Client()
                    new_client.set_c_name(name)
                    new_client.set_lst_name(famil)
                    new_client.set_national_code(national_code)
                    new_client.set_birth_date(birth)

                    if bank.unique_client_code(national_code):
                        try:
                            mablagh = float(input("Enter the money amount: "))
                        except ValueError:
                            print("Invalid amount!")
                            continue

                        account = manager.create_new_account(new_client, mablagh, "1402")
                        new_client.set_account(account)
                        bank.set_client(new_client)
                    else:
                        print("This person already exists!!!!")

                elif y == 4:
                    national_code = input("national code: ")
                    manager.remove_client(bank, national_code)

                elif y == 5:
                    break

                else:
                    print("Invalid option!")

        elif x == 2:
            # زیرمنوی «مدیر» (manager)
            while True:
                print("1. Show Personal Specifications\n"
                      "2. Show Client's Informations\n"
                      "3. Create New Account for Client\n"
                      "4. Remove Client\n"
                      "5. Show Employee's Information\n"
                      "6. Add Employee\n"
                      "7. Remove Employee\n"
                      "8. Registration of Attendance Hours\n"
                      "9. Exit")
                try:
                    y = int(input())
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                if y == 1:
                    manager.show_m_pecifications()

                elif y == 2:
                    national_code = input("enter national code: ")
                    manager.searching_client(bank, national_code)

                elif y == 3:
                    name = input("name: ")
                    famil = input("last name: ")
                    national_code = input("national code: ")
                    birth = input("birth date: ")
                    new_client = Client()
                    new_client.set_c_name(name)
                    new_client.set_lst_name(famil)
                    new_client.set_national_code(national_code)
                    new_client.set_birth_date(birth)

                    if bank.unique_client_code(national_code):
                        try:
                            mablagh = float(input("amount of money: "))
                        except ValueError:
                            print("Invalid amount!")
                            continue

                        account = manager.create_new_account(new_client, mablagh, "1402")
                        new_client.set_account(account)
                        bank.set_client(new_client)
                    else:
                        print("This person already exists!")

                elif y == 4:
                    national_code = input("national code: ")
                    manager.remove_client(bank, national_code)

                elif y == 5:
                    personal_code = input("personal code: ")
                    manager.searching_employee(bank, personal_code)

                elif y == 6:
                    name = input("name: ")
                    famil = input("last name: ")
                    personal_code = input("personal code: ")
                    try:
                        basic_salary = float(input("basic salary: "))
                    except ValueError:
                        print("Invalid salary!")
                        continue
                    new_emp = Employee()
                    if bank.unique_employee(personal_code):
                        new_emp.set_p_name(name)
                        new_emp.set_p_lst_name(famil)
                        new_emp.set_personal_code(personal_code)
                        new_emp.set_basic_salary(basic_salary)
                        bank.add_employee(new_emp)
                    else:
                        print("This employee already exists!!!")

                elif y == 7:
                    personal_code = input("personal code: ")
                    manager.remove_emoloyee(bank, personal_code)

                elif y == 8:
                    for i in range(bank.get_number_of_personels()):
                        emp_code = bank.employees[i].get_personal_code()
                        try:
                            time = int(input(f"{emp_code} - Enter attendance time: "))
                        except ValueError:
                            print("Invalid time! Skipping.")
                            continue
                        manager.set_attendance_ttime(bank, i, time)

                elif y == 9:
                    break

                else:
                    print("Invalid option!")

        elif x == 3:
            # زیرمنوی «مشتری» (client)
            while True:
                print("1. Add Account Balance\n"
                      "2. Withdrawal from Account\n"
                      "3. Personal Information\n"
                      "4. Exit")
                try:
                    y = int(input())
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

                if y == 1:
                    national_code = input("national code: ")
                    try:
                        mablagh = float(input("amount of money: "))
                    except ValueError:
                        print("Invalid amount!")
                        continue

                    while mablagh < 0:
                        print("error! try again.")
                        try:
                            mablagh = float(input("amount of money: "))
                        except ValueError:
                            print("Invalid amount!")
                            mablagh = 0

                    for client in bank.clients:
                        if client.get_national_code() == national_code:
                            acc = client.get_c_account()
                            acc.set_current_balance(acc.get_current_balance() + mablagh)
                            print(f"New balance: {acc.get_current_balance():.2f}")
                            break

                elif y == 2:
                    national_code = input("national code: ")
                    try:
                        mablagh = float(input("amount of money: "))
                    except ValueError:
                        print("Invalid amount!")
                        continue

                    while mablagh < 0:
                        print("error! try again.")
                        try:
                            mablagh = float(input("amount of money: "))
                        except ValueError:
                            print("Invalid amount!")
                            mablagh = 0

                    for client in bank.clients:
                        if client.get_national_code() == national_code:
                            acc = client.get_c_account()
                            acc.set_current_balance(acc.get_current_balance() - mablagh)
                            print(f"New balance: {acc.get_current_balance():.2f}")
                            break

                elif y == 3:
                    national_code = input("enter national code: ")
                    manager.searching_client(bank, national_code)

                elif y == 4:
                    break

                else:
                    print("Invalid option!")

        elif x == 4:
            print("Exiting...")
            break

        else:
            print("Invalid option!")
