# checks users choice is 'interger', 'text' or 'image' 
def user_choice(): 

    valid = False 
    while not valid: 
        response = input("file type (interger / text / image): ").lower()  
        
        if response == "text" or response == "t":
            return "text" 

        if response == "interger" or response == "int": 
            return "interger" 

        if response == "image" or response == "img": 
            return "image"

        else: 
            print()
            print("Please choose a valid file type!") 
            print() 


# main routine goes here 
data_type = user_choice() 
print()
print("you choose", data_type) 
print()