A=[3,5,2,4,8,0,7]
def search(n):

    for i in range(len(A)-1):
        if A[i]==n:
            print('the number is there')
            break
    else:
        print('the number is not there')
search(1)
