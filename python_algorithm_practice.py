# # Swap Pairs
# # Write a function to swap positions of successive pairs of values of given list. If length is odd, do not change the final element.
# # For example: 
# # - For input [1,2,3,4], return [2,1,4,3].
# # - For input [1,2,3,4,5], return [2,1,4,3,5].  
# # - For input ["Brian",True,42], return [True,"Brian",42]. 
# # Do this without using any built-in list methods.

# def swap_pairs(list):
#     for i in range(0,len(list) - 1,2):
#         temp = list[i]
#         list[i] = list[i+1]
#         list[i+1] = temp
#     return list

# print(swap_pairs ([1,2,3,4]))
# swap_pairs([1,2,3,4,5])
# swap_pairs( [ "Brian",True,42] )

# # Remove At
# # Given a list and an index as arguments, write a function to remove and return the list value at that index and print the shortened list. Do this without using built-in list methods except pop().
# # For example: 
# # - For input [1,2,3,4,5] and 2, print [1,2,4,5], return 3

# def remove_at(list,index):
#     # iterate through list from passed-index to the end of list
#     for i in range(index,len(list)-1,1):
#         temp = list[i]
#         list[i] = list [i+1]
#         list[i+1] = temp
#         # print(f"list index:{i}")
#         # print(f"list value:{list[i]}")
#     removed = list.pop()
#     print (list)
#     return removed 
    
    
    
# remove_at([1,2,3,4,5],2)

# List: Reverse
# Given a numerical list reverse the order of values, in-place. The reversed list should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working ‘in-place’ means that you cannot use a second list– you must move values within the list that you are given. As always, do not use built-in list functions.

# def reverse (list):
#     # access individual indices with a for in range
#     for i in range(0,len(list)//2, 1): # have to look up floor division or integer division operator
#         # print(f"index: {i}")
#         # print(f"value: {list[i]}")
#         # assign current index value to a temp variable
#         temp = list[i]
#         # print(temp)
#         list[i] = list[len(list)-i-1]
#         # print(list[i])
#         list[(len(list)-i)-1] = temp
#         # print(list[len(list)-i-1])

        
#     return list

# test = [1,2,3,4,5, 6, 7]
# print(reverse(test))

# Rotate
# Implement get_shwifty(input, shiftBy) that accepts a list and offset. Shift input’s values to the right by that amount. ‘Wrap-around’ any values that shift off the list's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), change the list to [3,1,2]. Don’t use built-in functions.
#     Second: allow negative shiftBy (shift L, not R).

def get_shwifty(input, shiftBy):
    # value at the current index needs to be assigned to the index + shiftBy
    for i in range(len(input)):
        # but if current index + shiftBy is greater than the last index value it will be out of range
    print(input)
get_shwifty([1,2,3],1)

