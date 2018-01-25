def ask_int():
    a = True
    while a:
        try:    # Here we put the code that can fail
            val = int(raw_input("Type in an integer"))
        except: # Here we put what to do if the code fails, you can actually specify the type of error
            print ("That is not an integer. Try again")
        else:   # Here we put what to do in case there is no error
            a = False
        finally:# This block will always run, wether there is error or not
            if a:
                print ("I ran, but don't have an integer yet")
            else:
                print ("I ran, and we have a valid value: {}".format(val))

ask_int()
