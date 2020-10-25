def Signin():
    while True:
    	user = input('\nENTER USER NAME: ')
    	if user in users:
    		if user == users[0]:
    			n = 0
    		else:
    			n = 1
    		break
    	else:
    		print('INVALID USERNAME')
    while True:
    	password = input('PLEASE ENTER Password: ')
    	if user == 'Sachin':
    		if password == Password[0]:
    			break
    		else:
    			print('INVALID PIN')
    			print()
    	if user == 'Tanuj':
    		if password == Password[1]:
    			break
    		else:
    			print('INVALID PIN')
    			print()
    	else:
    		print('Password INVALID')
    print("Welcome to your account")
    def CheckBalance():
        print("Current Balance : ",balance)
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
        p()
    def DepositBalance():
        dep = int(input("Enter your amount :"))
        global balance
        balance = balance + dep
        print("\n Amount Deposited:",dep)
        p()
    def Withdrawl():
        global balance
        wid = int(input("Enter amount to be Withdrawn: "))
        if balance >= wid:
            balance = balance - wid
            print("\n You Withdrew:", wid)
        else: 
            print("\n Insufficient balance  ")
        p()
    def Logout():
        s = input("Do you want to log out : ")
        if s == 'yes':
            main()
        else:
            p()
    def Forgetpass():
        password=input('Please Enter Your old Password :')
        if password == 'red@123':
            new = input('Enter Your new Password:')
            confirm = input("Enter your Password Again :") 
            if new == confirm:
                Password[0] = new
                print ('New Passwordhas been set continue your banking.')
        else:
            print ('You Have Enterd Invalid Password. Try Again')

        p()
    def p():
        res = input('Enter your choice: \n1. Check Balance \n2. Deposit Balance \n3. Withdrawl \n4. Log out\n5. Forget Password\nchoice:')
        valid_res = ['1', '2','3','4']
        if res == '1':
            CheckBalance()
        elif res == '2':
            DepositBalance()
        elif res == '3':
            Withdrawl()
        elif res == '4':
            Logout()
        elif res == '5':
            Forgetpass()
        else:
        	print('RESPONSE NOT VALID')
    p()

def SignUp():
    username = input("Enter your username : ")
    name = input("Enter Your name : ")
    password = input("Enter your password : ")
    bal  = input("Enter your balance in yout account :"+"Rs" )
    email = input("Enter your Email : ")
    print("Username Successfully created")
    main()


users = ['Sachin', 'Tanuj']
Password = ['red@123','red@1234']
balance = 0
count = 0
def main():
    response = input('Enter your choice: \n1. Signin \n2. SignUp \n3. Exit\nchoice: ')
    valid_responses = ['1', '2','3']
    if response == '1':
        Signin()
    elif response == '2':
        SignUp()
    elif response == '3':
        exit()
    else:
    	print('RESPONSE NOT VALID')
main()