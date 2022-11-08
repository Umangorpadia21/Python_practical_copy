def findsalt():
    ##Name:Umang , Rollno: F098
    ph_val = int(input("Enter the value between 0 to 14:"))
    if ph_val>=0 and ph_val<7:
        print("phval",ph_val,"is acidic")
    elif ph_val==7:
        print("phval",ph_val,"is neutral")
    elif ph_val>7 and ph_val<=14:
        print("phval",ph_val,"is basis")
    else :
        print("invalid input")
findsalt()



