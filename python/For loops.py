##5-A
def lists():
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)
def tuples():
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)
def strings():
    for x in "banana":
        print(x)
##5-b
def ranges():
    for x in range(6):
        print(x)
##5-c
def with_while_loop():
    i = 1
    while i < 6:
        print(i)
        i += 1
print(lists())
print(tuples())
print(strings())
print(ranges())
print(with_while_loop())

