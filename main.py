numberList = []

def menuNav(selectedOption):
    match selectedOption:
        case '1':
            calculate()
        case '0':
            print('Goodbye')
        case _:
            print('Invalid option, try again')
            mainMenu()

def mainMenu():    
    print("""
What would you like to do? (Input number)
1 - Calculate
0 - Exit
""")

    menuOption = input()

    menuNav(menuOption)

def calculate():
    finalValue = 0
    x = input('Enter the first value: ')
    numberList.append(int(x))

    operator = input('Enter the operator (+ - / *): ')

    x = input('Enter the second value: ')
    numberList.append(int(x))

    for num in numberList:
        if finalValue == 0:
            finalValue += num
        elif finalValue > 0:
            match operator:
                case '+':
                    finalValue += num
                case '-':
                    finalValue -= num
                case '/':
                    finalValue /= num
                case '*':
                    finalValue *= num
                case _:
                    print('Operator invalid, Cancelling calculation')
                    mainMenu()
    
    print("The result for the equation: " + str(numberList[0]) + operator + str(numberList[1]) + ' = ' + str(finalValue))

mainMenu()