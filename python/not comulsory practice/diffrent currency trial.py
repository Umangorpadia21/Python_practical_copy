if __name__=="__main__":
    def convertor():
        print("~~~Currency Convertor~~~")
        print("Enter your currency type eg:1 for Rupee,2 for Dollor,3 for Euro")
        choice=int(input("\nEnter your choice:"))
        if choice==1:
            print("\n1.1-->Rupee to Dollor")
            print("1.2-->Rupee to Euro")
            choice=float(input("\nEnter your choice:"))
            if choice==1.1:
                rupee=int(input("\nEnter currency in Rupee:"))
                dollor=(rupee/81)
                print(rupee,"₹","=",dollor,"$")
            if choice==1.2:
                rupee=int(input("\nEnter currency in Rupee:"))
                euro=(rupee/79)
                print(rupee,"₹","=",euro,"€")
        if choice==2:
            print("\n1-->Dollor to Rupee")
            print("2-->Dollor to Euro")
            if choice==2.1:
                dollor=int(input("\nEnter currency in dollor:"))
                rupee=(dollor*81)
                print(dollor,"$","=",rupee,"₹")
            if choice==2.2:
                dollor=int(input("Enter currency in Dollor"))
                euro=(dollor/1.01)
                print(dollor,"$","=",euro,"€")
        if choice==3:
            print("\n1-->Euro to Rupee")
            print("2-->Euro to Dollor")
            if choice==3.1:
                euro=int(input("\nEnter currency in Euro"))
                rupee=(euro*79)
                print(dollor,"€","=",euro,"₹")
            if choice==3.2:
                euro=int(input("Enter currency in Dollor"))
                dollor=(euro/1.01)
                print(euro,"€","=",dollor,"$")
       # else :
       #         print("wrong input3")
convertor()
