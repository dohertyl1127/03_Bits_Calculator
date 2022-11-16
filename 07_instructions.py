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

#displays information/instructions
def instructions(): 

    statement_generator("Instructions / Information", "=") 
    print() 
    print("please choose a data type (image / text / integer)") 
    print() 
    print("this program assumes that the images that are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).") 
    print() 
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.") 
    print() 
    return""

# main routine 
instructions()