# functions go here 

# calculates the number of bits for text (# of character *8) 
def text_bits(): 

    print() 
    # ask user for a string 
    var_text = input("enter your text: ") 

    # calculate the number of bits (length of string *8) 
    var_length = len(var_text) 
    num_bits = 8 * var_length 

    # output answer with working 
    print() 
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} * 8".format(var_length)) 
    print("we need {} bits to represent {}".format(num_bits, var_text)) 
    print() 

    return "" 
 
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

# puts symbols at start and end of text (for emphasis)
def statement_generator(text, decoration, lines) :
    middle = "{} {} {}".format(decoration*3, text, decoration*3)
    top_bottom = decoration * len(middle)

    if lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(middle)

    return None

    
    statement_generator("Bits Calculator", "-")

# checks users enter text / image or integer
def user_choice(): 
   
    # list of valid responses
    
    text_ok = ["t", "text", "txt"]
    interger_ok = ["in", "int", "integer"]
    image_ok = ["image", "img","p"]
    
    # checks if users choice is vaiable

    valid = False 
    while not valid: 
        print()
        response = input("file type (interger / text / image): ").lower()  
        
        if response in text_ok :
            return "text" 

        elif response in interger_ok: 
            return "integer" 
        
        elif response in image_ok:
            return "image" 

        elif response == "i": 
            want_int = input("press <enter> for an interger, or any key, <enter> for image")
            if want_int == "": 
                return "integer" 
            else:
                return "image"

        # error message 

        else: 
            print()
            print("Please choose a valid file type!") 
            print() 

    data_type = user_choice() 
    print()
    print("you chose", data_type) 
    print()

# checks integer is a number more than a given value
def num_check(question, low): 
    valid = False 
    while not valid: 

        error = "please choose a number that is more than (or equal to) {}".format(low)

        try: 
            # asks user for number
            response = int(input(question)) 

            # checks the number is more than 0
            if response >= low : 
                return response 

            else : 
                print(error) 
                print()

        except ValueError:
            print()
            print(error) 
            print()

# main routine goes here 

statement_generator("bit calculator for intergers, text and images", "-", 3)

# display instruction if user has never used the program before

# loop to allopw for multiple calculations per second

keep_going = ""
while keep_going == "":
    
    # checks users choice is 'interger', 'text' or 'image' 
    data_type = user_choice()
    print(data_type)

    # for integers, ask integer 
    if data_type =="integer": 
        print()
        var_integer = num_check("Please enter an integer: ", 1) 

    # for images, ask image 
    elif data_type =="image": 
        print()
        image_width = num_check("Please enter image width: ", 1) 
        print()
        image_height = num_check("please enter image height: ", 1) 

    # for text, ask for string
    else : 
        text_bits()
    
print("We are done") 
print()