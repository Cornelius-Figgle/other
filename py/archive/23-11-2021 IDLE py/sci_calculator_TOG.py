import math                                                             #adds extra maths stuff

restart = "y"                                                           #sets 'restart' to be yes
while restart == "y" or restart == "Y":                                 #as long as restart is equal to yes, the script will loop
    numOne = str(input("\nInput first number or input a constant: "))   #sets 'numOne' to be a string, which is an input also, which uses the question
    
    if numOne == "π" or numOne == "pi" or numOne == "Pi":               #if the first number is π then 
        ansOne = math.pi                                                    #sets the first answer as the value
    elif numOne == "e" or numOne == "E":                                #if the first number is e then 
        ansOne = math.e                                                     #sets the first answer as the value
    elif numOne == "τ" or numOne == "tau" or numOne == "Tau":           #if the first number is τ then 
        ansOne = math.tau                                                   #sets the first answer as the value
    else:                                                               #if a constant is not inputted
        numOne = float(numOne)                                                  #converts the string of numOne to a float
        print("Choose operation:")                                              #prints choose
        operator = input("+ - * / x^y |x| √ ⌈x⌉ ⌊x⌋ : ")                        #asks with list of operators to sets 'opp' as
        
        if operator == "|x|" or operator == "abs" or operator == "Abs":         #if operator is abs
            ansOne == abs(numOne)                                                   #calculates the abs of numOne
        elif operator == "√" or operator == "sqrt" or operator == "Sqrt":       #if operator is sqrt
            ansOne == math.sqrt(numOne)                                             #calulates sqrt
        elif operator == "⌈x⌉" or operator == "ceil" or operator == "Ceil":     #if operator is ceiling
            ansOne == math.ceil(numOne)                                              #calulates ceil
        elif operator == "⌊x⌋" or operator == "floor" or operator == "Floor":   #if operator is floor
            ansOne == math.floor(numOne)                                            #calulates floor
        else:                                                                   #if the calulation requires 2 numbers
            numTwo = float(input("Input second number: "))                          #sets 'numTwo' to be a float, which is an input also, which uses the question
            if operator == "+":                                                     #if operator is a "+"
                ansOne = numOne + numTwo                                                #sets the first answer to be number one + number two
            elif operator  == "-":                                                  #if operator is a "-"
                ansOne = numOne - numTwo                                                #sets the first answer to be number one - number two
            elif operator  == "":                                                  #if operator is a ""
                ansOne = numOne * numTwo                                                #sets the first answer to be number one * number two
            elif operator  == "/":                                                  #if operator is a "/"
                ansOne = numOne / numTwo                                                #sets the first answer to be number one / number two
            elif operator == "x^y" or operator == "X^y" or operator == "^":         #if operator is an indice
                ansOne = pow(numOne, numTwo)                                            #calculates the indice
            else:                                                                   #if the operator is none of the above
                print("Please enter a correct operator value")                          #prints an error message
                q = input("")                                                           #waits until enter pressed
                continue                                                                #goes back to the top of the loop

    print(ansOne)                                                       #prints the first answer
    print("\nDo you wish to solve another equation:")                   #prints do restart after missing a line
    restart = input("y/n : ")                                           #asks whether y or n to set restart as
    
else:                                                               #if restart is false
     q = input()                                                        #wait until enter pressed to quit
