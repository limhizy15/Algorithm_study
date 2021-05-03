# 리스트 사용시 런타임 
def firstDuplicate(a):
    s = set()
    for i in a:
        if i in s:
            return i
        s.add(i)
    return -1        
