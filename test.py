def fun(var):
    for i in range(5): 
        if (var == "A" or var == "B"):
            pass
        elif (var == "C" or var == "D"):
            print("Cat")
            break
        else:
            print("dog")
            continue
    return var



var = input("Enter a letter: ")

fun(var)