def selection_sort(arr):
    # Selection sort algorithm implementation
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[j]
    return arr
arr=[4,8,1,3,5]
print(selection_sort(arr))