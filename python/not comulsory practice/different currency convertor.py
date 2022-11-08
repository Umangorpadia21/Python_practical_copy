if __name__=="__main__":
    def convertor():
        print("~~~Currency Convertor~~~")
        print("Enter your currency type eg:Dollor,Rupee,Euro")
        choice=str(input("\nEnter your choice:"))
        if choice=="rupee" or "Rupee":
            print("\n1-->Rupee to Dollor")
            print("2-->Rupee to Euro")
            choice=int(input("\nEnter your choice:"))
            if choice==1:
                rupee=int(input("\nEnter currency in Rupee:"))
                dollor=(rupee/74)
                print(rupee,"₹","=",dollor,"$")
            if choice==2:
                rupee=int(input("\nEnter currency in Rupee:"))
                euro=(rupee/79)
                print(rupee,"₹","=",euro,"€")
            else :
                print("Wrong input1")
        if choice=="Dollor" or "Dollor":
            print("\n1-->Dollor to Rupee")
            print("2-->Dollor to Euro")
            if choice==1:
                dollor=int(input("\nEnter currency in dollor:"))
                rupee=(dollor*74)
                print(dollor,"$","=",rupee,"₹")
            if choice==2:
                dollor=int(input("Enter currency in Dollor"))
                Euro=(dollor/1.01)
                print(dollor,"$","=",euro,"€")
            else:
                    print("Wrong input2")
        else :
                print("wrong input3")
convertor()
