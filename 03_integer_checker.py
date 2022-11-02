# checks if integer is valid
def num_checker(question, low): 
    valid = False 
    while not valid: 

        error = "please choose a number that is more than " 
        "(or equal to) {}".format(low)

        try: 
            # asks user for number
            response = int(input(question)) 

            # checks the number is more than 0
            if response > low : 
                return response 

            else : 
                print(error) 
                print

        except ValueError:
            print(error) 

# main routine goes here 

keep_going = ""
while keep_going == "" :
    print() 
    
