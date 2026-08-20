program_run = input('Do you want to run the program? Type y for YES if you do and n For NO: ')[0].lower()
print(program_run)

def confirm():
    print("The Program is Running!")
    my_list = ['apple', 'orange', 'banana', 'grapes']

    print(" juice - ".join(my_list))

    for i in range(5):
        print("Dante")

if program_run == "y":
    confirm()
else:
    print("Okay program Stopped!")



