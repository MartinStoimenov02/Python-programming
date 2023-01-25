def anagram(str, str1):
    d={}
    d1={}
    for i in str:
        a=str.count(i)
        d[i]=a
        b=str1.count(i)
        d1[i]=b
    if d1==d and len(str)==len(str1):
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."

s=input("string 1:")
s1=input("string 2:")
print(anagram(s, s1))