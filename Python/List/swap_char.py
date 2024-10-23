original_list=['Gfg', 'is','best','for','Geeks']
print("The original list is: "+str(original_list))
result=[sub.replace('G','g').replace('e','G')for sub in original_list]
print("The list after performing swap is: "+str(result)) 
