def findsalt():
    ##Name:Umang , Rollno: F098
    ph_val = int(input("Enter the value between 0 to 14:"))
    if ph_val>=0 and ph_val<7:
        print("phval",ph_val,"is acidic")
    if ph_val==7:
        print("phval",ph_val,"is neutral")
    if ph_val>7 and ph_val<=14:
        print("phval",ph_val,"is basis")
    if ph_val>14 and ph_val<0:
        print("invalid input")
findsalt()



