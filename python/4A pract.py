def Rocktheit():
    name=str(input("Enter your name: "))
    w=int(input("Enter weight of parcel(In Kg): "))
    if w>0 and w<=10:
        cal=w*25
        print("Calculation",cal)
    elif w>10 and w<=20:
        cal=w*20
        print("Calculation",cal)
    elif w>20 and w<=30:
        cal=w*10
        print("Calculation",cal)
    else :
        print("Invalid input")
    Total=5/100*cal+cal
    print("Total value is: ",Total)


    
    print("~~"*40)
    print("Name\tWeight\tcharge\tTotal\n")
    
    print(name,'\t',w,'\t',cal,'\t',Total)
Rocktheit()


    
