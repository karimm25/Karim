# number of local variables

def test():
    a = 1
    s = '1000'
    l = ()
    return a,s,l

print(test.__code__.co_nlocals)