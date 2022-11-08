def sum1(arr):
    result=sum(arr)
    return result
if __name__=="__main__":
    arr=list(map(int, input("Enter multiple values: "). split()))
    print('sum1: {}'.format(sum1(arr)))
