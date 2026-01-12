def bin_search(sort_array,target):
    sort_array.sort()
    low=0
    high=len(sort_array)-1
    while(low<=high):
        mid=(low+high)//2
        if sort_array[mid]==target:
            return f"{target} found at position {mid+1}"
        elif sort_array[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return f"{target} not found"
array=["123.0.1.2","122.0.2.1","137.2.3.1","121.0.3.1"]
array.sort()
print(array)
print(bin_search(array,'121.0.3.1'))