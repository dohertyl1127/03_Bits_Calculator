# checks integer is a number more than a given value
def num_check(question, low): 
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
    # asks for a integer(must be more than or equal than 0)
    var_integer = num_check("enter an integer: ", 1) 
    print() 

    # ask for image width and height 
    # must be a number more than 1
    image_width = num_check("enter image width: ", 1)
    image_height = num_check("enter image height: ", 1)