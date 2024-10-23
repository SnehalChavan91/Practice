def max_and_min(arr):
    return (min(arr),max(arr))

print(max_and_min([3,2,1,56,10000,167]))

def union_of_arrays(arr1,arr2):
    arr=arr1+arr2
    return len(set(arr))

arr1=[1,2,3,4,5]
arr2=[1,2,3]
print(union_of_arrays(arr1,arr2))


def intersection_of_arrays(arr1,arr2):
    intersection=[]
    for i in arr1:
        if i in arr2:
            intersection.append(i)
    return intersection
arr1=[1,2,3,4]
arr2=[2,4,6,7,8]
print(intersection_of_arrays(arr1,arr2))
