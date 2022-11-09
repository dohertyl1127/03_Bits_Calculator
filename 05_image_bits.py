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

# finds # of bits for 24 bit color 
def image_bits(): 

    # asks user for image width and height
    print()
    image_width = num_check("enter image width: ", 1) 
    image_height = num_check("enter image height: ", 1)

    num_pix = image_width * image_height 

    num_bits = num_pix *24

    # output 
   
    print()   
    print("# of pixels = {} x {} = {} ".format(image_width, image_height, num_pix)) 
    print("# of bits = {} x 24 = {} ".format(num_pix, num_bits))
    print()


# main routine goes here 
image_bits() 
