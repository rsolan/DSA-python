def pal(i,n,s):
    if i>=n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return pal(i+1,n,s)
    

s = 'madame'
n = len(s)
print(pal(0,n,s))
