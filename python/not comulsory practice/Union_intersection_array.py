a=list(map(int,input('Enter elements of first list:').split()))
b=list(map(int,input('Enter elements of second list:').split()))

A=list(set(a)|set(b))
B=list(set(a)&set(b))

print('Union of the arrays:',A)
print('intersection of the arrays:',B)
