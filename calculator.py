def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter my choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()


def HDL_driver():
    #Get input
    Input = get_input()
    #Check if HDL is normal
    Analysis = Check_input(Input)
    #Output
    Output(Input, Analysis)
    return

def get_input():
    a = input("Input HDL level: ")
    return int(a)

def Check_input(a):
    if a >= 60:
        return "Normal"
    elif 40 <= a < 60:
        return "Borderline Low"
    elif a < 40:
        return "Low"

def Output(input, results):
    print("Your HDL level is {}".format(input))
    print("Which is ".format(results))
    return


interface()
