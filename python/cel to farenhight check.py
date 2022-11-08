if __name__=="__main__":
    def convertor():
        ##Name:Umang ROll no:F098
        print("~~~Temperature Convertor~~~")
        print("1--> Fah to cel")
        print("2--> cel to fah")
        choice=int(input("enter your choice:"))
        if choice==1:
            fah=int(input("Enter temperature in celcius:"))
            cel=(fah*9/5)+32
            print(fah,"Degree celcius","=",cel,"degree farenhight")
        elif choice==2:
            cel=int(input("Enter temperaturein farenhight:\n"))
            fah=(cel-32)*5/9
            print(cel,"Degree farenhight","=",fah,"degree celcius")
        else :
            print("wrong input")
convertor()

    
