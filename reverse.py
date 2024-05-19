def reverse_array(arr,leng):
    for i in range(leng//2):
        arr[i],arr[leng-i-1]=arr[leng-i-1],arr[i]
    return arr   

arr=list(map(int,input().split()))
leng=len(arr)
print(reverse_array(arr,leng))      