
def plus (a, b):
    return ( int(a) + int(b) )

def minus (a, b):
    return ( int(a) - int(b))

def times (a, b):
    return ( int(a) * int(b))

def quotient (a, b):
    return ( int(a) / int(b))

def remainder (a, b):
    return ( int(a) % int(b))

def powered (a, b):
    return ( int(a) ** int(b))

def absolutes (a):
    return ( abs(int(a)) )

print( plus( 1, "2") ) # 3
print( minus( 1, "2") ) # -1
print( times( 1, "2" )) # 2
print( quotient( 1, "2" )) # 0.5
print( remainder( 1, "2" )) # 1
print( powered( 2, "4" )) # 16
print( absolutes("-1")) # 1
