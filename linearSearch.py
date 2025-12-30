def linear_search(dataset,target):
    for i in range (len(dataset)):
        if dataset[i]==target:
            return f"{target} found at position {i+1}"
    return f"{target} not found"
dataset=["123.0.1.2","122.0.2.1","137.2.3.1","121.0.3.1"]
print(linear_search(dataset,"122.0.2.1"))  