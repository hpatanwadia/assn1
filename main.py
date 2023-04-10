import string
 
# initializing list
test_list = [4, 5, 2, 4, 2, 6, 5, 2, 5]
 
# printing list
print("The original list : " + str(test_list))
 
temp = {}
cntr = 0
for ele in test_list:
    if ele in temp:
        continue
     
    # assigning same Alphabet to same element
    temp[ele] = string.ascii_lowercase[cntr]
    cntr += 1
     
# flattening
res = [temp.get(ele) for ele in test_list]
 
# printing results
print("The mapped List : " + str(res))