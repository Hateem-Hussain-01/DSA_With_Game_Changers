x = "hayitshuffy"
s = list(x)
lenth = len(s)
b = 6
c = 4
for i in range(b):
    s[i], s[(i+c)%lenth] = s[(i+c)%lenth] , s[i]
newstr = ''.join(s)
print(newstr)
print(x)
