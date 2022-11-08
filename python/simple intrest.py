def inputdata():
    name=input("Enter your name")
    p=float(input("principle amount"))
    n=int(input(" no of months"))
    r=float(input("Rate of intrest"))
    calSI(name,p,n,r)
def calSI(name,p,n,r):
    si=(p*n*r)/100
    amt=si+p
    display(name,p,n,r,si,amt)
def display(name,p,n,r,si,amt):
    print("~~"*20)
    print("name:",name)
    print("principlers:",p)
    print("no.of months",n)
    print("rate of intrest",r,"per month")
    print("simple intrest",si)
    print("total amount",amt)
    print("~~"*20)
if __name__=="__main__":
    inputdata()
    

