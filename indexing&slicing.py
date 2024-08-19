# import  numpy as np
# a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
# #print 2nd row
# print(f'  2nd row is : {a[1]}\n')
#
# #print 1st and 3rd row
# print(f'1st and 3rd row {a[[1,3]]}\n')
#
# #select the middle three colums
# print(f'middle 3 colums are:  \n{a[:,1:4]}\n')
#
#  #show 12 and 13 from an array
# print(f'show 12 and 13 from an array : \n {a[2:4, 2]}\n')
#
#  #show revers order of third rows values
#
# # print(a[2::-1,:] )
#
#  #Select the fourth rows and find max, min, sum, mean, std and var of  values
# print()
#
#  #Find log10, log2, log values of rows one
# print()


import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20]])

# Print 2nd row
print(f'2nd row: {a[1]}\n')

# Print 1st and 3rd row
print(f'1st and 3rd row:\n{a[[0, 2]]}\n')

# Select the middle three columns
print(f'Middle 3 columns:\n{a[:, 1:4]}\n')

# Show 12 and 13 from the array
print(f'Show 12 and 13 from the array:\n{a[[2,3],[3,0]]}\n')
 

# Show reverse order of third row's values
print(f'Reverse order of third row:\n{a[2, ::-1]}\n')

# Select the fourth row and find max, min, sum, mean, std, and var of values
fourth_row = a[3]
print(f'Fourth row: {fourth_row}')
print(f'Max: {np.max(fourth_row)}')
print(f'Min: {np.min(fourth_row)}')
print(f'Sum: {np.sum(fourth_row)}')
print(f'Mean: {np.mean(fourth_row)}')
print(f'Std: {np.std(fourth_row)}')
print(f'Var: {np.var(fourth_row)}\n')

# Find log10, log2, log values of row one
row_one = a[0]
print(f'Log10 of row one: {np.log10(row_one)}')
print(f'Log2 of row one: {np.log2(row_one)}')
print(f'Natural log of row one: {np.log(row_one)}')
