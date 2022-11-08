if __name__=="__main__":
    def convertor():
        print("~~~Currency Convertor~~~")
        print("1--> rupee to dollor")
        print("2--> dollor to rupee")
        choice=int(input("enter your choice:"))
        if choice==1:
            rupee=int(input("Enter currency in rupee:"))
            dollor=(rupee/80)
            print(rupee,"₹","=",dollor,"$")
        elif choice==2:
            dollor=int(input("Enter currency in dollor:"))
            rupee=(dollor*80)
            print(dollor,"$","=",rupee,"₹")
        else :
            print("wrong input")
convertor()
