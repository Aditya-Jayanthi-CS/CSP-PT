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

deposit_frame = tk.Frame(bank)

tk.Label(deposit_frame, text = "You are now DEPOSITING.").pack()
    
tk.Label(deposit_frame, text = "Deposit Amount:").pack(pady=5)
deposit_string = tk.StringVar()
deposit_entry = tk.Entry(deposit_frame, textvariable = deposit_string, width = 20)
deposit_entry.pack()

tk.Label(deposit_frame, text = "Note:").pack(pady=10)
deposit_note_string = tk.StringVar()
deposit_note = tk.Entry(deposit_frame, textvariable = deposit_note_string, width = 30)
deposit_note.pack()

def signup_submit():
    user = username_text.get()
    pas = password_text.get()
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

def display_deposit():
    tk.Label(bank, text = "You are now DEPOSITING.").pack()

    tk.Label(bank, text = "Deposit Amount:").pack(pady=5)
    deposit_string = tk.StringVar()
    deposit_entry = tk.Entry(bank, textvariable = deposit_string, width = 20)
    deposit_entry.pack()

    tk.Label(bank, text = "Note:").pack(pady=10)
    deposit_note_string = tk.StringVar()
    deposit_note = tk.Entry(bank, textvariable = deposit_note_string, width = 30)
    deposit_note.pack()

def display_withdraw():
    tk.Label(bank, text = "You are now WITHDRAWING.").pack()

    tk.Label(bank, text = "Withdrawal Amount:").pack(pady=5)
    withdraw_string = tk.StringVar()
    withdraw_entry = tk.Entry(bank, textvariable = withdraw_string, width = 20)
    withdraw_entry.pack()

    tk.Label(bank, text = "Note:").pack(pady=10)
    withdraw_note_string = tk.StringVar()
    withdraw_note = tk.Entry(bank, textvariable = withdraw_note_string, width = 30)
    withdraw_note.pack()


def login_page():
    global login
    login.deiconify()

    tk.Label(login, text = "Enter Username:").pack(pady=10)
    tk.Entry(login, textvariable = login_user, width = 20).pack(pady=2)

    tk.Label(login, text = "Enter Password:").pack(pady=5)
    tk.Entry(login, textvariable = login_pass, width=20, show = "*").pack(pady=2)

    log_submit = tk.Button(login, text = "Submit", command = login_submit)
    log_submit.pack(pady=5)

    #error from 51-53
    '''if username_text.get() == login_user.get() and password_text.get() == login_pass.get():
        print("2")
        log_submit.config(state = tk.DISABLED)'''


login_button = tk.Button(frame, text = "Login", command = login_page, width = 8, height = 2)
login_button.pack(side = "top", anchor = "ne")

username = tk.Label(text = "Username:")
username.pack(pady=5)

username_text = tk.StringVar()
username_entry = tk.Entry(frame, textvariable = username_text, width=20)
username_entry.pack(pady=2)

password = tk.Label(text = "Password:")
password.pack(pady=5)

password_text = tk.StringVar()
password_entry = tk.Entry(frame, textvariable = password_text, width=20, show = "*")
password_entry.pack(pady=2)

submit_button = tk.Button(frame, text = "Submit", command = signup_submit)
submit_button.pack(pady=5)

tk.mainloop()
