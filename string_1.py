# x = "hay this is hateem"
# print(len(x))
# print(x[-1])
# y = "hay this is" 
# print(x[3]==y[3])
# print(x==y)
# print(x[1000])
# name = "hateem"
# print(name.index("m"))
# new_name= name[:2]+name[3:]
# # print(new_name)
# print(name.replace('t',''))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = (filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
print(''.join(even_numbers))
