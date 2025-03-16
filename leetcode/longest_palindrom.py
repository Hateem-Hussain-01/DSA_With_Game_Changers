
def longestPalindrome(s) -> str:
    max_char = 26
    lst = []
    length = 0
    palindrom = []
    t = "hay"
    for i in range(len(s)):
        q = ""
        for j in range(i, len(s)):
            q += s[j]
            # print(q)
            lst.append(q)
        for x in lst: #[2,3,4,5,6,7,8,9,10]
            if x == x[::-1]:
                # if len(lst[x]) > length:
                #     length = len(lst[x])
                palindrom.append(x)
        for c in palindrom:
            if len(c) > length:
                length = len(c)
                t = c
    print(t)
            
    #print(palindrom)
longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth')

        