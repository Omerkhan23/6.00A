# Problem 1: Given a list of numbers. Write a function to turn every item of 
# a list into its square.
def square_list(my_list):
    squared_list = []
    for i,e in enumerate(my_list):
        squared_list.append(my_list[i]**2)
    return squared_list    

# test
print(square_list([1, 2, 3, 4]))
print(square_list([10, 12, 13]))



# Problem 2: Write a Python program to concatenate element-wise 
# three given lists of same length
# Original lists:
list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']
# Expected output : ['0red100', '1green200', '2black300', '3blue400', '4white500']

def concatenate_lists(list_a, list_b, list_c):
    L_new = []
    for i in range(len(list1)):
        L_new += [list1[i] + list2[i] +list3[i]]
    return L_new

# test
print(concatenate_lists(list1, list2, list3))




# Problem 3: Write a function to shift a given list to the right or left 
# direction by a specified amount. Direction, rotation amount, and a 
# list of integers should be inputs to the function.
# e.g. 
# Input list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the input list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the input list in Right direction by 4:
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

# edit this to be "right" or "left"
direction = "right" 

def rotate_list(input_list, direction, by):
    L_new = input_list[:]
    if direction == 'left':
        del input_list[0:by]
        input_list.extend(L_new[0:by]) # adding at the end of the list
        return input_list
    elif direction == 'right':
        del input_list[-by: ]
        input_list[0:0] = L_new[-by: ] # adding at the start of the list
        return input_list
    else:
        return None
    
# this function mutates the list so we need to chnge the list


# test 
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotate_list(input_list, "left", 2))
another_list = [1,2,3,4,5,6,7,8,9,10]
print(rotate_list(another_list,"right" , 5))


#############################################
#Solution         bY              MIT########

# direction = "right" 

# def rotate_list(input_list, direction, shift):
#     shift = shift % len(input_list)
#     if direction == "right":
#         return input_list[-shift:] + input_list[:-shift]
#     elif direction == "left":
#         return input_list[shift:] + input_list[:shift]
#     else:
#         return None

# # test 
# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(rotate_list(input_list, "right", 14))
# print(rotate_list(input_list, "left", 4))
