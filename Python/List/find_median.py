def findMedian(list1,list2):
    combined_list=list1+list2
    combined_list.sort()
    print(combined_list)

    n=len(combined_list)
    if n%2==1:
        median=combined_list[n//2]
        return median
    else:
        mid1=combined_list[(n//2)-1]
        mid2=combined_list[n//2]
        median=(mid1+mid2)//2
        return median
list1=[1,2,3,4]
list2=[4,5,6,7]
print(findMedian(list1,list2))