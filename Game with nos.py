def game_with_number (arr,  n) : 
    #Complete the function
    l  = []
    for i in range(n-1):
        l.append(arr[i] ^ arr[i+1])
    l.append(arr[n-1])
    return l
