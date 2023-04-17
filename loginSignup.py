# import modules

from tkinter import *
from game import startgame

# Defines a function called register
def register():
    # Declares that the "register_screen" variable is a global variable.
    global register_screen
    # Creates a new window using Toplevel, which will be used for the registration screen.
    # The new window will be displayed on top of the "main_screen" window.
    register_screen = Toplevel(main_screen)
    # Sets the title of the registration screen.
    register_screen.title("Register")
    # Sets the dimensions of the registration screen to be 1920x1080.
    register_screen.geometry("1920x1080")

    # Declares that the following variables are global variables.
    global username
    global password
    global username_entry
    global password_entry
    # Creates two StringVar objects to store the values entered by the user for username and password.
    username = StringVar()
    password = StringVar()

    # Creates a label that will display the text "Please enter details below" on the registration screen.
    # The label will have a background color of MediumPurple1, a width of 300, a height of 2, and a font of Calibri with size 13.
    # The label is then packed into the registration screen.
    Label(register_screen, text="Please enter details below",
        bg="MediumPurple1", width="300", height="2", font=("Calibri", 13)).pack()
    # Creates an empty label, which is packed into the registration screen to provide some space between the two labels.
    Label(register_screen, text="").pack()
    # Creates a label that will display the text "Username" on the registration screen.
    # The label is then packed into the registration screen.
    username_lable = Label(register_screen, text="Username", font=("Calibri", 16),pady=20)
    username_lable.pack()
    # Creates an Entry widget that allows the user to enter their username.
    # The value entered by the user will be stored in the "username" variable.
    # The widget is then packed into the registration screen.
    username_entry = Entry(register_screen, textvariable=username,width=20)
    username_entry.pack()
    # Creates a label that will display the text "Password" on the registration screen.
    # The label is then packed into the registration screen.
    password_lable = Label(register_screen, text="Password", font=("Calibri", 16), pady=20)
    password_lable.pack()
    # Creates an Entry widget that allows the user to enter their password.
    # The value entered by the user will be stored in the "password" variable.
    # The widget will display asterisks instead of the actual characters entered by the user.
    # The widget is then packed into the registration screen.
    password_entry = Entry(register_screen, textvariable=password,show='*',width=20)
    password_entry.pack()
    # Creates an empty label, which is packed into the registration screen to provide some space between the two widgets.
    Label(register_screen, text="").pack()
    # Creates a button labeled "Register" that is 10 characters wide and 2 characters tall.
    # The button will have a background color of MediumPurple1.
    # When the button is clicked, the "register_user" function will be called.
    # The button is then packed into the registration screen.
    Button(register_screen, text="Register", width=10,
           height=2, bg="MediumPurple1", command=register_user, font=("Calibri", 12)).pack(pady=20)



# Designing window for login
def login():
    global login_screen
    # Creates a new window using Toplevel, which will be used for the login screen.
    # The new window will be displayed on top of the "main_screen" window.
    login_screen = Toplevel(main_screen)
    # Sets the title of the login screen.
    login_screen.title("Login")
    login_screen.geometry("1920x1080")
    Label(login_screen, text="Please enter details below to login",
          bg="MediumPurple1", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    # Creates a label that will display the text "Username" on the login screen.
    Label(login_screen, text="Username",  font=("Calibri", 16), pady=20).pack()
    # Creates an Entry widget that allows the user to enter their username during the login process.
    username_login_entry = Entry(
        login_screen, textvariable=username_verify, width=20)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    # Creates a label that will display the text "Password" on the login screen.
    Label(login_screen, text="Password", font=("Calibri", 16), pady=20).pack()
    # Creates an Entry widget that allows the user to enter their password during the login process.
    # The widget will display asterisks instead of the actual characters entered by the user.
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*', width=20)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    # Creates a button labeled "Login"
    Button(login_screen, text="Login", bg="MediumPurple1",width=10,
           height=2, command=login_verify, font=("Calibri", 12)).pack(pady=20)

# This function registers a new user by saving their username and password to a file named "save_data.txt" and provides feedback to the user if the registration was successful or not.
def register_user():

    username_info = username.get()
    password_info = password.get()

    #These two lines get the username and password entered by the user in the registration screen and store them in two variables username_info and password_info.
    file = open("save_data.txt", "a")
    file.write(username_info + ":" + password_info + "\n")
    file.close()
    # These lines clear the username and password entry fields after the user submits their registration information.
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="").pack()
    #These lines add a label saying "Registration Success!" to the registration screen to let the user know that their registration was successful.
    Label(register_screen, text="Registration Success!",
          bg="SteelBlue1", width="100", height="2", font=("Calibri", 10)).pack()
    Label(register_screen, text="").pack()
    # This line adds a "OK" button to the registration screen which, when clicked, calls the delete_register_success() function to close the registration screen.
    Button(register_screen, text="OK",
           command=delete_register_success).pack()


# This function verifies the login credentials entered by the user by checking them against the data stored in the "save_data.txt" file. If the login credentials match with any of the records in the file, it calls the login_success() function. Otherwise, it calls the password_not_recognised() function to let the user know that the entered credentials are incorrect.
def login_verify():
    #These two lines get the username and password entered by the user in the login screen and store them in two variables username1 and password1.
    username1 = username_verify.get()
    password1 = password_verify.get()
    # These lines clear the username and password entry fields after the user submits their login information.
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # These lines open the file named "save_data.txt" in read-only mode and initialize a boolean variable found to False to indicate if the user's login credentials match with any of the records in the file.
    file = open("save_data.txt", "r")
    found = False
    # These lines iterate through each line in the file, split it into username and password using the colon separator :, and compare them with the user's entered username1 and password1. If a match is found, the found variable is set to True and the loop is terminated using the break statement.
    for line in file:
        username, password = line.strip().split(":")
        if username1 == username and password1 == password:
            found = True
            break
    # This line closes the file after the search operation is completed.
    file.close()

    # These lines check the value of found. If it is True, it calls the login_success() function to indicate a successful login. Otherwise, it calls the password_not_recognised() function to inform the user that the entered login credentials are incorrect.
    if found:
        login_sucess()
    else:
        password_not_recognised()

# This function creates a new window to display a success message when the user successfully logs in. It also provides some buttons for the user to proceed to play the game, access instructions, and view information about the developers.
def login_sucess():
    # make login_success_screen a global variable so that it can be accessed from other functions
    global login_success_screen
    # create a new window to display the success message
    login_success_screen = Toplevel(login_screen)
    # set the window title
    login_success_screen.title("Success")
    # set the window size
    login_success_screen.geometry("1920x1080")
    # create a label to display the success message
    Label(login_success_screen, text="Login Success", bg="MediumPurple1",
          width="300", height="2", font=("Calibri", 13)).pack()
    # create an empty label to add spacing between the success message and the buttons
    Label(login_success_screen, text="").pack()
    # create a button for the user to proceed to play the game
    Button(login_success_screen, text="Proceed to Play", bg="MediumPurple1",
           height="2", width="30", command=delete_login_success).pack()
    # create an empty label to add spacing between the "Proceed to Play" and "Instructions" buttons
    Label(login_success_screen, text="").pack()
    # create a button for the user to access the game instructions
    Button(login_success_screen, text="Instructions", bg="MediumPurple1",
           height="2", width="30", command=lambda: openInstructions()).pack()
    # create an empty label to add spacing between the "Instructions" and "About Us" buttons
    Label(login_success_screen, text="").pack()
    # create a button for the user to view information about the developers
    Button(login_success_screen, text="About Us", bg="MediumPurple1",
           height="2", width="30", command=lambda: openAboutUs()).pack()
    # create an empty label to add spacing at the bottom of the window
    Label(login_success_screen, text="").pack()

# This function is called when the user enters an incorrect password during the login process. It displays a new window with a message saying "Invalid Password" and an "OK" button that, when clicked, closes the window.
def password_not_recognised():
    global password_not_recog_screen   # declares a global variable for the window
    # creates a new window that appears on top of the login_screen window
    password_not_recog_screen = Toplevel(login_screen)
    # sets the title of the new window to "Success"
    password_not_recog_screen.title("Success")
    # sets the size of the new window to 150x100 pixels
    password_not_recog_screen.geometry("150x100")
    # creates a label with the text "Invalid Password" and adds it to the new window
    Label(password_not_recog_screen, text="Invalid Password").pack()
    # creates a button with the text "OK" and a command to call the function delete_password_not_recognised() when clicked, and adds it to the new window.
    Button(password_not_recog_screen, text="OK",
            command=delete_password_not_recognised).pack()

# This function creates a pop-up window that displays a message "User Not Found" and an "OK" button to close the window when the user is not found
def user_not_found():
    global user_not_found_screen  # declare a global variable for the pop-up window
    # create the pop-up window as a child of the login screen
    user_not_found_screen = Toplevel(login_screen)
    # set the title of the window to "Success"
    user_not_found_screen.title("Success")
    # set the size of the window to 150x100 pixels
    user_not_found_screen.geometry("150x100")
    # create a Label widget with the message "User Not Found" and add it to the window
    Label(user_not_found_screen, text="User Not Found").pack()
    # create an "OK" button widget and add it to the window, and set its command to a function that will close the window
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# This function is used to delete the login success screen and start the game
def delete_login_success():
    login_success_screen.destroy()
    startgame()

# This function is used to delete the register success screen
def delete_register_success():
    register_screen.destroy()

# This function is used to delete the password not recognized screen    
def delete_password_not_recognised():
    password_not_recog_screen.destroy()

# This function is used to delete the user not found screen
def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# This function is responsible for creating the main account screen for the user to either login or register
def main_account_screen():
    # Declare main_screen as a global variable to be accessible by other functions
    global main_screen
    # Create a new window with dimensions 1920x1080 and title "Account Login"
    main_screen = Tk()
    main_screen.geometry("1920x1080")
    main_screen.title("Account Login")
    # Create a label for the user to select their choice and pack it into the main screen
    Label(text="Select Your Choice", bg="MediumPurple1", width="300",
            height="2", font=("Calibri", 15)).pack()
    # Add some empty space between the label and the buttons
    Label(text="").pack()
    # Create a login button with a purple background and larger font size and set the command to the login function
    Button(text="Login", bg="MediumPurple3", height="3",
            width="30", font="Calibri 20", command=login).pack(pady=60, anchor="center")
    # Add some empty space between the buttons
    Label(text="").pack()
    # Create a register button with a purple background and larger font size and set the command to the register function
    Button(text="Register", bg="MediumPurple3", height="3",
            width="30", font=("Calibri", 20), command=register).pack(pady=10, anchor="center")
    
    # Start the main loop to display the window and wait for user interaction
    main_screen.mainloop()

# This function opens the About Us screen
def openAboutUs():
    global open_AboutUs_screen
    open_AboutUs_screen = Tk()
    open_AboutUs_screen.title("AboutUs")
    open_AboutUs_screen.config(background="Light Blue")
    open_AboutUs_screen.geometry("1920x1080")
    Label(open_AboutUs_screen, text="This is our final project for the course AML 1214 - Python Programming 01 Course. We have developed a Dots and Boxes game in python using tkinter and numpy.\n\nTeam members:\n 1.Himanshu\n 2.Namita\n 3.Bhavneet\n 4.Shree Prada\n 5.Dushyant\n\n\nWe hope you have a great time playing this game!Enjoy!", font=("Helvetica", 15), fg="black", bg="Light Blue", padx=50, pady=250, anchor=W, justify=LEFT).pack()
    open_AboutUs_screen.mainloop()

# This function opens the Instructions screen
def openInstructions():
    global open_Instructions
    open_Instructions = Tk()
    open_Instructions.title("Instructions")
    open_Instructions.geometry("1920x1080")
    open_Instructions.config(background="Light Blue")
    open_Instructions.title("Instructions")
    aboutlabel = Label(open_Instructions, text="Instructions: \n1.Each player will take turns drawing a line between two dots on the board.The line can be vertical or horizontal, \nbut it must connect two adjacent dots.\n2.If a player completes a box, the box gets coloured and they can take another turn.\n3.The game continues until all of the boxes have been completed.\n4.The player with the most completed boxes at the end of the game is the winner.", font=("Helvetica", 15), fg="black", bg="Light Blue", padx=50, pady=250, anchor=W, justify=LEFT).pack()
    open_Instructions.mainloop()
