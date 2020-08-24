def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter my choice: ")
        if choice=='9':
            return
        elif choice == '1':
            HDL_driver()

#call three functions

def HDL_driver(a):
    #Get input
    Input = get_input()
    #Check if HDL is normal
    #Output

def get_input():
    a = input("Input HDL level: ")
    return int(a)

# def Check_input(a):
#     if a >= 60:
#         print("Normal")
#     elif a >= 40 && a < 60:
#         print("Borderline Low")



interface()
