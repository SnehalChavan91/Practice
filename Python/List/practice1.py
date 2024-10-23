from itertools import groupby
test_list=["geeks","for","geeks","is","best"]
print("The original list is: "+str(test_list))
result=[i.upper() for i in test_list]
print("The uppercased list is : "+str(result))

result=list(map(str.lower,test_list))
print("The lowercased list is: "+str(result))

original_list=[1,1,2,3,3,3,4,5,5]
split_list=[list(group) for key, group in groupby(original_list)]
print(split_list)
original_list=["a","b","c","d","e","f"]
split_lst=[number.split(',')for number in original_list]
print(split_lst)

lst=[[1,2,3],[4,5],[6,7,8,9]]
result=[item[-1] for item in lst]
print("The result is: "+str(result))
result1=[item[0] for item in lst]
print("The result is: "+str(result1))
