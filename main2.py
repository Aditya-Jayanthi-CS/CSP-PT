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

deposit_string = tk.StringVar()
deposit_note_string = tk.StringVar()
note_deposit = deposit_note_string.get()

withdraw_string = tk.StringVar()
withdraw_note_string = tk.StringVar()
note_withdraw = withdraw_note_string.get()

username_text = tk.StringVar()
password_text = tk.StringVar()
user = username_text.get()
pas = password_text.get()

balance = 0

def net():
    #customer_details = [user, balance]
    user = username_text.get()
    f = open("Account_Details.txt", "+a")
    f.write("\n \nUsername: " + user + "\n")
    f.write("Current Balance: " + str(balance))
    f.close()

def signup_submit():
    #user = username_text.get()
    #pas = password_text.get()
    output = tk.Label(text = "Your information has been saved. \n You may continue to the login page.")
    output.pack(pady=2)
    submit_button.config(state = tk.DISABLED)

def login_submit():
    if username_text.get() == login_user.get() and password_text.get() == login_pass.get():
        bank.deiconify()
        bank_page()
    else:
        tk.Label(login, text = "Either the username or password you entered incorrect.").pack(pady=10)

def bank_page():
    button_frame = tk.Frame(bank)
    button_frame.pack()
    button1 = tk.Button(button_frame, text="Deposit", command = display_deposit)
    button1.pack(padx = 5, pady = 5, side="left")

    button2 = tk.Button(button_frame, text="Withdraw", command = display_withdraw)
    button2.pack(padx = 5, pady = 5, side="left")

    widget_frame.pack()

def clear_frame():
      for widget in widget_frame.winfo_children():
        widget.destroy()

def display_deposit():
    clear_frame()
    tk.Label(widget_frame, text = "You are now DEPOSITING.").pack()

    tk.Label(widget_frame, text = "Deposit Amount:").pack(pady=5)
    deposit_entry = tk.Entry(widget_frame, textvariable = deposit_string, width = 20)
    deposit_entry.pack()

    tk.Label(widget_frame, text = "Note:").pack(pady=10)
    deposit_note = tk.Entry(widget_frame, textvariable = deposit_note_string, width = 30)
    deposit_note.pack()

    deposit_submit = tk.Button(widget_frame, text = "Submit", width = 10, command = submit_deposit)
    deposit_submit.pack()

def submit_deposit():
    #amount_deposit = deposit_string.get()
    #note_deposit = deposit_note_string.get()
    global balance
    amount_deposit = deposit_string.get()
    balance += float(amount_deposit)

    net()

def submit_withdraw():
    #amount_withdraw = withdraw_string.get()
    #note_withdraw = withdraw_note_string.get()
    global balance
    amount_withdraw = withdraw_string.get()

    if balance - float(amount_withdraw) >= 0:
        balance -= float(amount_withdraw)
        net()
    else:
        tk.Label(widget_frame, text = "There is not sufficient money to withdraw").pack(pady=10)

def display_withdraw():
    clear_frame()
    tk.Label(widget_frame, text = "You are now WITHDRAWING.").pack()

    tk.Label(widget_frame, text = "Withdrawal Amount:").pack(pady=5)
    withdraw_entry = tk.Entry(widget_frame, textvariable = withdraw_string, width = 20)
    withdraw_entry.pack()

    tk.Label(widget_frame, text = "Note:").pack(pady=10)
    withdraw_note = tk.Entry(widget_frame, textvariable = withdraw_note_string, width = 30)
    withdraw_note.pack()

    withdraw_submit = tk.Button(widget_frame, text = "Submit", width = 10, command = submit_withdraw)
    withdraw_submit.pack()

def login_page():
    global login
    login.deiconify()

    tk.Label(login, text = "Enter Username:").pack(pady=10)
    tk.Entry(login, textvariable = login_user, width = 20).pack(pady=2)

    tk.Label(login, text = "Enter Password:").pack(pady=5)
    tk.Entry(login, textvariable = login_pass, width=20, show = "*").pack(pady=2)

    log_submit = tk.Button(login, text = "Submit", command = login_submit)
    log_submit.pack(pady=5)

login_button = tk.Button(frame, text = "Login", command = login_page, width = 8, height = 2)
login_button.pack(side = "top", anchor = "ne")

username = tk.Label(text = "Username:")
username.pack(pady=5)

#username_text = tk.StringVar()
username_entry = tk.Entry(frame, textvariable = username_text, width=20)
username_entry.pack(pady=2)

password = tk.Label(text = "Password:")
password.pack(pady=5)

#password_text = tk.StringVar()
password_entry = tk.Entry(frame, textvariable = password_text, width=20, show = "*")
password_entry.pack(pady=2)

submit_button = tk.Button(frame, text = "Submit", command = signup_submit)
submit_button.pack(pady=5)

tk.mainloop()
