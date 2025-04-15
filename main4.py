import tkinter as tk
frame = tk.Tk()

frame.geometry("600x600")
frame.title("Sign Up Page")
frame.config(bg="lightblue")

login_user = tk.StringVar()
login_pass = tk.StringVar()

login = tk.Toplevel(frame)
login.geometry("600x600")
login.title("Login Page")
login.config(bg="lightblue")
login.withdraw()

bank = tk.Toplevel(frame)
bank.geometry("600x600")
bank.title("Bank Account Manager")
bank.config(bg="lightblue")
bank.withdraw()

widget_frame = tk.Frame(bank)
display_frame = tk.Frame(bank)

deposit_string = tk.StringVar()
deposit_note_string = tk.StringVar()

withdraw_string = tk.StringVar()
withdraw_note_string = tk.StringVar()

username_text = tk.StringVar()
password_text = tk.StringVar()

balance = 0

count_transactions = 0
save = {}

def net(username, balance):
    username = username_text.get()
    with open("Account_Details.txt", "a") as f:
        f.write("\nUsername: " + username + "\n")
        f.write("Current Balance: " + str(balance) + "\n")

def signup_submit():
    output = tk.Label(frame, text="Your information has been saved.\nYou may continue to the login page.")
    output.pack(pady=2)

def login_submit():
    if username_text.get() == login_user.get() and password_text.get() == login_pass.get():
        bank.deiconify()
        bank_page()
    else:
        tk.Label(login, text="Either the username or password you entered is incorrect.").pack(pady=10)

def bank_page():
    button_frame = tk.Frame(bank)
    button_frame.pack()
    button1 = tk.Button(button_frame, text="Deposit", command=display_deposit)
    button1.pack(padx=5, pady=5, side="left")

    button2 = tk.Button(button_frame, text="Withdraw", command=display_withdraw)
    button2.pack(padx=5, pady=5, side="left")

    button3 = tk.Button(button_frame, text = "Mini-Statement", command=display_statement)
    button3.pack(padx=5, pady=5, side="left")

    widget_frame.pack()

def display_statement():
    global depwith_string
    global num_transactions
    depwith_string = tk.StringVar()
    depwith_string.set("Deposits")
    options = ["Deposits", "Withdrawal"]
    depwith = tk.OptionMenu(widget_frame, depwith_string, *options)
    depwith.pack(padx = 15, side="left")

    num_transactions = tk.StringVar()
    num_transactions.set("1")
    transaction_options = ["1", "2", "3", "4", "5"]
    transactions = tk.OptionMenu(widget_frame, num_transactions, *transaction_options)
    transactions.pack(padx=15, side="left")

    ok_submit = tk.Button(widget_frame, text = "Ok", command=submit_mini(depwith, num_transactions))
    ok_submit.pack(padx=15, side="left")

def submit_mini(depwith, num_transactions):
    lst = []
    if depwith_string.get() == "Deposits":
        for data in save.values():
            if data[0] == "D":
                lst.append(data)
    else:
        for data in save.values():
            if data[0] == "W":
                lst.append(data)
    
    number_transactions = num_transactions.get()
    print("This: " + number_transactions)
    for each in range(int(number_transactions)):
        tk.Label(widget_frame, text = lst[each]).pack(pady=10)


def clear_frame():
    for widget in widget_frame.winfo_children():
        widget.destroy()

def display_deposit():
    clear_frame()
    tk.Label(widget_frame, text="You are now DEPOSITING.").pack()

    tk.Label(widget_frame, text="Deposit Amount:").pack(pady=5)
    deposit_entry = tk.Entry(widget_frame, textvariable=deposit_string, width=20)
    deposit_entry.pack()

    tk.Label(widget_frame, text="Note:").pack(pady=10)
    deposit_note = tk.Entry(widget_frame, textvariable=deposit_note_string, width=30)
    deposit_note.pack()

    deposit_submit = tk.Button(widget_frame, text="Submit", width=10, command=submit_deposit)
    deposit_submit.pack()

def submit_deposit():
    global balance
    global count_transactions
    try:
        amount_deposit = float(deposit_string.get())
        note_deposit = deposit_note_string.get()
        balance += amount_deposit

        save_list = ["D", balance, amount_deposit, note_deposit]
        count_transactions += 1
        save[count_transactions] = save_list

        net(username_text.get(), balance)
        with open("Account_Details.txt", "a") as f:
            f.write(f"Deposit Amount: {amount_deposit}\n")
            f.write(f"Deposit Note: {note_deposit}\n")
        
        display_balance()
    except ValueError:
        tk.Label(widget_frame, text="Invalid deposit amount. Please enter a number.").pack(pady=10)

def display_balance():
    tk.Label(widget_frame, text=f"Current Balance: {balance}").pack(pady=10)

def submit_withdraw():
    global balance
    global count_transactions
    try:
        amount_withdraw = float(withdraw_string.get())
        note_withdraw = withdraw_note_string.get()

        if balance >= amount_withdraw:
            balance -= amount_withdraw
            
            save_list = ["W", balance, amount_withdraw, note_withdraw]
            count_transactions += 1
            save[count_transactions] = save_list

            net(username_text.get(), balance)
            with open("Account_Details.txt", "a") as f:
                f.write(f"Withdraw Amount: {amount_withdraw}\n")
                f.write(f"Withdraw Note: {note_withdraw}\n")

            display_balance()
        else:
            tk.Label(widget_frame, text="Insufficient funds for withdrawal.").pack(pady=10)
            display_balance()
    except ValueError:
        tk.Label(widget_frame, text="Invalid withdrawal amount. Please enter a number.").pack(pady=10)

def display_withdraw():
    clear_frame()
    tk.Label(widget_frame, text="You are now WITHDRAWING.").pack()

    tk.Label(widget_frame, text="Withdrawal Amount:").pack(pady=5)
    withdraw_entry = tk.Entry(widget_frame, textvariable=withdraw_string, width=20)
    withdraw_entry.pack()

    tk.Label(widget_frame, text="Note:").pack(pady=10)
    withdraw_note = tk.Entry(widget_frame, textvariable=withdraw_note_string, width=30)
    withdraw_note.pack()

    withdraw_submit = tk.Button(widget_frame, text="Submit", width=10, command=submit_withdraw)
    withdraw_submit.pack()

def login_page():
    login.deiconify()

    tk.Label(login, text="Enter Username:").pack(pady=10)
    tk.Entry(login, textvariable=login_user, width=20).pack(pady=2)

    tk.Label(login, text="Enter Password:").pack(pady=5)
    tk.Entry(login, textvariable=login_pass, width=20, show="*").pack(pady=2)

    log_submit = tk.Button(login, text="Submit", command=login_submit)
    log_submit.pack(pady=5)

login_button = tk.Button(frame, text="Login", command=login_page, width=8, height=2)
login_button.pack(side="top", anchor="ne")

username = tk.Label(frame, text="Username:")
username.pack(pady=5)

username_entry = tk.Entry(frame, textvariable=username_text, width=20)
username_entry.pack(pady=2)

password = tk.Label(frame, text="Password:")
password.pack(pady=5)

password_entry = tk.Entry(frame, textvariable=password_text, width=20, show="*")
password_entry.pack(pady=2)

submit_button = tk.Button(frame, text="Submit", command=signup_submit)
submit_button.pack(pady=5)

tk.mainloop()
