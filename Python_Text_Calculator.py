def Calculator():

    calc = input("What kind of calculation do you wish to do? (type ? for help): ")

    if calc == "?":
        print("Currently supported: *, /, + and - ")
        print("")
        Calculator();

    elif calc == "*":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))
        print("Answer: ", number1 * number2)
        print("")
        Calculator();

    elif calc == "/":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 / number2)
        print("")
        Calculator();

    elif calc == "-":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 - number2)
        print("")
        Calculator();

    elif calc == "+":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 + number2)
        print("")
        Calculator();
        
        
    elif calc == "%":
        try:
            number1 = int(input("Please select the first number(greater): "))
            number2 = int(input("Please select the second number(smaller): "))
        except (TypeError, ValueError):
            print("Invalid input")
            print("")
            Calculator();        
        if(abs(number1)<abs(number2)):
           print("")
           print("The second number entered is greater than the bigger number")
           Calculator();
        print("Answer: ", number1-number2*int(number1/number2))
        print("")
        Calculator();
        
	
    elif calc == "exit":
        exit();
	
    else:
        print("")
        print("Sorry, I dont understand your request. Currently supported calculations: *, /, - and +. Sorry for the inconvenience!")
        print("")
        Calculator();

print("")
Calculator();
