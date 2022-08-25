low, high = 0, len(ansList)-1
    while low <= high:
        mid = (high + low) //2
        if ansList[mid] < l <= ansList[mid+1]:
            print(mid+2)
            break
        elif ansList[mid] >= l:
            high = mid -1
        else:
            low = mid + 1