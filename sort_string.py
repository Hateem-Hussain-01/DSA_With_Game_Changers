#s = "geeksforgeeks"
#list1 = ["greeks","for"]
#print(s.sort())
#list1.sort()
# Sort the string and join it back
#s = ''.join(sorted(s))

# Print the sorted string
#print(s)

#print(list1)
MAX_CHAR = 26
# i_char = []
# j_char=[]
def sort_string(s):
    char_count = [0] * MAX_CHAR
    for ch in s:
        char_count[ord(ch)-ord("a")] +=1
    # for i in range(MAX_CHAR):
    #     #i_char.append(i)
    #     for j in range(char_count[i]):
    #         #j_char.append(j)
    #         print(chr(ord("a")+i) , end='')
        
    # for q in range(MAX_CHAR):
    #     for z in char_count:
    #         if char_count[z] !=0:
    #             print(chr(ord("a")+q), char_count[z] , end='')
    for i in range(MAX_CHAR):  # ✅ Correct: Use index i
        if char_count[i] != 0:
            print(chr(ord("a") + i),char_count[i], end=' ')
            
s = "hayitshateemhusbandofabidashoukat"
sort_string(s)
# print(i_char)
# print(j_char)

