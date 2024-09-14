import datetime

# adding new registration in username file
def add_username_detail(username,password):
    with open("username_detail",'a+') as file:
        file.write(f"username : {username}\nPassword : {password}\n")
    
# registration page
def register_page():
    style_register="registration page"
    print(style_register.center(50,'_'),"\n")
    username=input("Enter your name : ")
    password=input("Create your password : ")
    check=check_username(username)
    date_time=datetime.datetime.now()
    time=date_time.time()
    date=date_time.date()
    txt="*"
    txt=txt.center(50,'_')
    
    if check:
        print("username alredy exist.")
        option=input("Will you want to try again (yes/no) : ")
        option=option.lower()
        if option == "yes":
            register_page()
        else:
            first_page()
    else:
        add_username_detail(username,password)
        amount=input("Deposite your first amount : ")
        with open(f"{username}_bank_statment",'a+') as file:
            file.write(f"{txt}\nDEPOSITE\nTotal amount : {amount}\nTime : {time}\tDate : {date}\n")
        with open(f"{username}_total_amount",'w+') as amount_file:
            amount_file.write(amount)
    first_page()

#check username 

def check_username(username):
    try:
        with open("registration_detail",'r') as file:
            content=file.readlines()
            for i in range(0 , len(content)-1, 2):
                stored_username_line = content[i].strip()
                if stored_username_line.startswith("username : "):
                    stored_username=stored_username_line.split(':',1)[1].strip()
                else:
                    continue
                if stored_username==username:
                    return True
                else:
                    return False
    except:
        return False



# check the password and username
def check_login_detail(username, password):
    try:
        with open("username_detail", 'r') as file:
            lines = file.readlines()
            # Iterate through lines to find username and password pairs
            for i in range(0, len(lines) - 1, 2):  # Increment by 2 to handle pairs of lines
                # Read username and password from consecutive lines
                stored_username_line = lines[i].strip()
                stored_password_line = lines[i + 1].strip()
                
                # Extract actual username and password
                if stored_username_line.startswith("username :"):
                    stored_username = stored_username_line.split(':', 1)[1].strip()
                else:
                    continue  # Skip if the line does not start with "username :"
                
                if stored_password_line.startswith("Password :"):
                    stored_password = stored_password_line.split(':', 1)[1].strip()
                else:
                    continue  # Skip if the line does not start with "Password :"
                
                # Compare extracted username and password with provided values
                if username.strip() == stored_username and password.strip() == stored_password:
                    return True
    except FileNotFoundError:
        print("The file 'username_detail' does not exist.")
        return False
    return False


# show available balance
def total_amount(username):
    try:
        with open(f"{username}_total_amount",'r') as file:
            total_amount=file.read().strip()
            print(f"\nAvilable amount {total_amount}\n")
    except:
        print("\nZero Balance\n")
    input("Press Enter to continue...")
    login_option(username)


# withdrawl amount
def debit_amount(username):
    amount=int(input("Enter the ammount you want to withdrawl : "))
    debited_note = input("Enter the withdrawl note : ")
    date_time=datetime.datetime.now()
    time=date_time.time()
    date=date_time.date()
    txt="*"
    txt=txt.center(50,'_')
    
    with open(f"{username}_total_amount",'r+') as total_file:
        total_file.seek(0)
        total_amount=int(total_file.read().strip())

    if total_amount<amount:
        print("Not a sufficient balance.") 
    else:
        total_amount-=amount
        with open(f"{username}_debit_amount",'a+') as file:
            file.write(f"{txt}\nDebit Note : {debited_note}\nDebit Amount : {amount}\nTime : {time}\nDate : {date}\n{txt}\n")

        with open(f"{username}_bank_statment",'a+') as bank_file:
            bank_file.write(f"{txt}\nWITHDRAWL\nCurrent Balance : {total_amount}\nWithdrawl Amount : {amount}\nDebit Note : {debited_note}\nTime : {time}\tDate : {date}\n{txt}\n")
        
        with open(f"{username}_total_amount",'w+') as file1:
            file1.write(str(total_amount))
    login_option(username)



# deposite amount  
def credit_amount(username):
    credit_amount=int(input("Enter the amount you want to deposite : "))
    credit_note=input("Enter the deposite note :")
    date_time=datetime.datetime.now()
    time=date_time.time()
    date=date_time.date()
    txt="*"
    txt=txt.center(50,'_')
            
    with open(f"{username}_total_amount",'r+') as total_amount:
        total_amount.seek(0)
        bank_amount=int(total_amount.read().strip())
        bank_amount+=credit_amount
        
        with open(f"{username}_total_amount",'w+') as file1:
            file1.write(str(bank_amount))
    
        with open(f"{username}_bank_statment",'a+') as bank_statment:
            bank_statment.write(f"{txt}\nDEPOSITE\nCurrent Balance : {bank_amount}\nDeposite Amount : {credit_amount}\nDeposite Note : {credit_note}\nTime : {time}\tDate : {date}\n{txt}\n")

    with open(f"{username}_credit_amount",'a+') as credit_file:
        txt="*"
        txt=txt.center(50,'_')
        credit_file.write(f"{txt}\nDeposite Note : {credit_note}\nDeposite Amount : {credit_amount}\nTime : {time}\nDate : {date}\n{txt}\n")
    login_option(username)


# show all deposite detail
def deposit_detail(username):
    try:
        with open(f"{username}_credit_amount", 'r') as file:
            deposit_detail = file.read().strip()  # Read the file content
            print(deposit_detail, "\n")
    except:
        print("No deposite statment avilable\n")
    input("Press Enter to continue...")  # Optional pause to let user review the details
    login_option(username)  # Return to login options


# show all withdrawl detail
def withdraw_detail(username):
    try:
        with open(f"{username}_debit_amount",'r') as file:
            withdraw_detail = file.read().strip()
            print(withdraw_detail, "\n")
    except:
        print("No withdraw statment avilable.\n")
    input("Press Enter to continue...")    
    login_option(username)


# show bank statment
def bank_statment(username):
    try:
        with open(f"{username}_bank_statment",'r') as file:
            bank_detail=file.read().strip()
            print(bank_detail,"\n")
    except:
        print("No bank statment.\n")
    input("Press Enter to continue...")
    login_option(username)


def login_option(username):
    style="login option"
    print(f"{style.center(50,'_')}\n")
    print("Avilable amount = 1\tWithdraw amount = 2\nBank statment = 3\tDeposite amount = 4\nDeposite detail = 5\tWithdrawl detail = 6\nLogout = 7\n")
    choose=int(input("Enter your choice : "))
    if choose==1:
        total_amount(username)
    elif choose==2:
        debit_amount(username)
    elif choose==3:
        bank_statment(username)
    elif choose==4:
        credit_amount(username)
    elif choose==5:
        deposit_detail(username)
    elif choose==6:
        withdraw_detail(username)
    elif choose==7:
        first_page()
    else:
        print("Enter valid option only.")
        login_option()

# login page
def login_page():
    style_login="login page"
    print(style_login.center(50,'_'),"\n")
    count=0
    while count<=3:
        username=input("Enter your account username : ")
        password=input("Enter your account password : ")
        check=check_login_detail(username,password)
        count+=1
        if check==False:
            print("Innvalid Username or Password")
            print(f"Number of trial left {3-count}\n")
            select=input("do you want to try again (yes/no) : ")
            if select=="yes":
                first_page()
            else:
                first_page()
            if count==3:
                first_page()
        else:
            login_option(username)


# first page of bank
def first_page():
    txt="***"
    print(txt.center(50,"_"))
    print("Login = 1\nRegister = 2\n")
    choose=int(input("Enter your choice : "))
    if choose==1:
        login_page()
    elif choose==2:
        register_page()

while True:
    bank="B A N K"
    print(bank.center(50,'_'))
    first_page()
