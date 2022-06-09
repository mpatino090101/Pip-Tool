import os

def install_module():
    instruction = input("What module would you like to install?")
    os.system("pip install {0}".format(instruction))
    print("Action Completed...")

def uninstall_module():
    instruction = input("What module would you like to uninstall?")
    os.system("pip uninstall {0}".format(instruction))
    print("Action Completed...")

def check_version():
    print(os.system("pip --version"))

def upgrade_pip_version():
    print(os.system("pip install --upgrade pip"))

def command_choice(choice):
    match choice:
        case 1:
            install_module()
        case 2:
            uninstall_module()
        case 3:
            check_version()
        case 4:
            upgrade_pip_version()
status = True

while status == True:
    command_choice(int(input(print(
        "1. Install a Module.\n2. Uninstall a Module.\n3. Check Pip Version. \n4. Upgrade Pip Version\n\nWhat action would you like to take?"))))
    continue_program= input(print("Would you like to take another action?\nY/N?"))
    if continue_program.lower() == "n":
        status = False
        print("Program ended.\nThank you for using the Pip Tool.")
