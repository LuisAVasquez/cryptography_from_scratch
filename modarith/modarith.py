


#gcd: euclidean algorithm 

def gcd(a,b) -> int:
    """
    GCD of two integer numbers
    """
    if b == 0: return a
    if a < 0: return gcd(-a, b)
    if b < 0: return gcd(a, -b)
    if b > a : return gcd(b,a)
    return gcd(b, a%b )

#print( gcd( 3, 5 ))
#print( gcd( -3, 5 ))


#extended euclidean algorithm
def extended_euclid(m, n):
    """"
    extended_euclid(m,n) returns integers (a,b,d) such that
    a*m + b*n = d = gcd(m,n)
    """

    #initializations
    (s, r) = (0,n)
    (previous_s, previous_r) = (1, m)

    while r!=0:
        quotient = previous_r // r
        (previous_r, r) = (r, previous_r % r)
        (previous_s, s) = (s, previous_s - quotient * s)

    if n == 0:
        b = 0
    else:
        b = (previous_r - previous_s * m) // n
    
    # previous_r is the gcd

    #making sure we work with a positive gcd
    if(previous_r < 0):
        (previous_s, b, previous_r) = (-previous_s, -b, -previous_r)

    #print(previous_r)
    #print((previous_s, b, previous_r))
    return (previous_s, b, previous_r)

#print(extended_euclid(3,5) )
#print(extended_euclid(3,-5) )
#print(extended_euclid(-3,5) )
#print(extended_euclid(-3,-5) )

#print(extended_euclid(-15,-35) )


def inverse(a, n):
    """
    inverse(a,n) gives the multiplicative inverse modulo n
    """
    #working mod -n is the same as working mod n
    # Z_{-n} = Z_{n}
    if n<0: return inverse(a, -n) 

    (x, y, d) = (extended_euclid(a, n) )
    #print((x,y,d))
    if d != 1:
        raise ArithmeticError("Non invertible element")
    
    return x % n

"""
print("-"*20)
print(inverse(3,5))
print(inverse(-13, 10))

try: 
    print(inverse(3,3))
except ArithmeticError:
    print("there's a non invertible element")
"""

# modular exponentiation
def power_mod(base, exp, n ):
    """
    power_mod(base, exp, n) returns base^exp mod n
    based on square-multiply
    """
    #print("one entrance")
    base = base %n
    if base == 0 and exp > 0: return 0
    if exp == 0: return 1
    if exp == 1: return base #% n
    
    if exp%2: #exp is odd
        return (
            base * power_mod(( base*base) %n, (exp-1) /2, n)
        ) % n
    else: #exp is even
        return power_mod( (base*base)%n, exp/2, n) %n #is this modulus necesary? 


#print("-"*10)
#print(power_mod(5,3,10))
#print(power_mod(12342,4312,10))
#print(power_mod(12342*10,4312,10))