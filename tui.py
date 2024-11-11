"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def display_welcome():
    title = "Disneyland Review Analyzer"
    print(f"\n{'-' * len(title)}\n{title}\n{'-' * len(title)}\n")


def display_main_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualize Data")
    print("[x] Exit")
    return input("Your choice: ").strip().upper()


def display_view_data_menu():
    print("\nPlease enter the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    return input("Your choice: ").strip().upper()


def display_visualize_data_menu():
    print("\nPlease enter the following options:")
    print("[A] Most reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most popular Month by Park")
    return input("Your choice: ").strip().upper()



#