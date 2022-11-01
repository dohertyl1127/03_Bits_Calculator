# functions go here 

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

# checks users enter text / image or integet
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

# main routine goes here 

statement_generator("bit calculator for intergers, text and images", "-", 3)

# display instruction if user has never used the program before

# loop to allopw for multiple calculations per second

keep_going = ""
while keep_going == "":
    
    # checks users choice is 'interger', 'text' or 'image' 
    data_type = user_choice()
    print(data_type)

    keep_going = input("Press <enter> to keep going or any key to quit")
    print()

print("We are done") 
print()