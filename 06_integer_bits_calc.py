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

# finds the bits needed for an integer 
def int_bits(): 

    # get integer (must be >=0)
    var_int = input("please enter an integer: ", 0) 

    var_binary = "{0:b}".format(var_int) 

    # calculate the number of bits(lenght of sting above) 
    num_bits = len(var_binary) 

        # output answer with working 
    print() 
    print("{} in binary is {} ".format(var_int, var_binary)) 
    print("we need {} bits to represent {} ".format(num_bits, var_int)) 
    print() 
 
    return ""

# main routine goes here 

int_bits()

