####
# Elliptic curve arithmetic

####

# putting the parent folder in syspath 
# to be able to import all the modules in the package
import os, sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..'
        )
    )
)
###########################################

from modarith import modarith




# Elliptic curve Class


class EllipticCurve():
    """
    Object representing an elliptic curve

    y^2 = x^3 + a* x + b mod p
    """

    def __init__(self, p, a = 0, b = 0, ord = None):
        #order is optional
        self.p = p
        self.a = a
        self.b = b
        self.ord = ord

    

def check_validity(ecpoint):
    if ecpoint.infinity: return True

    p = ecpoint.ec.p
    return (modarith.power_mod(ecpoint.y, 2, p) 
            == (modarith.power_mod(ecpoint.x,3, p) + 
            (ecpoint.ec.a * ecpoint.x)% p + ecpoint.ec.b
            ) % p)

class ECPoint():
    """Object representing an elliptic curve point"""

    def __init__(self, ec, x= None, y = None, infinity = False):
        self.ec = ec #parent elliptic curve
        self.infinity = infinity # True for point at infinity
        self.x = x
        self.y = y
        
        #check validity
        
        if not check_validity(self): raise Exception("Invalid point")
        
    def __repr__(self) -> str:
        if self.infinity:
            return "<INF>"
        else:
            return "".join(["<",str(self.x),",",str(self.y),">"])

    def inverse(self):
        #additive inverse
        if self.infinity:
            return self
        else:
            return ECPoint(
                self.ec,
                x   = self.x ,
                y   = (- self.y)% self.ec.p #just the opposite point
            )

    def __eq__(self, other) -> bool:
        if self.ec != other.ec: return False
        if self.infinity and other.infinity: return True
        return all([
            self.x == other.x,
            self.y == other.y
            ])

    def __add__(self, other):
        #implementing elliptic curve addition
        
        #identity elements
        if self.infinity: return other
        if other.infinity: return self

        #print(self.inverse(), other)
        #print(self.inverse() == other)
        if self.inverse() == other: 
            
            return ECPoint(self.ec, infinity=True)
            
        p = self.ec.p   
        if self == other:
            #point doubling 
            lam = (3*modarith.power_mod(self.x, 2, p) + self.ec.a)%p
            lam = (lam * modarith.inverse(2*self.y,p))%p
        else:
            #normal addition
            lam = (other.y - self.y) % p
            lam = (lam * modarith.inverse(other.x - self.x, p)) % p
        
        new_x = (lam*lam - self.x - other.x)%p
        new_y = (lam*(self.x - new_x) - self.y)%p

        return ECPoint(self.ec, x = new_x, y = new_y)

    def __rmul__(self, integer): 
        #print(self)
        #print(integer)

        #exp -> integer, self -> base
        
        # point at infinity
        # if base == ECPoint(self.ec, infinity=True) and integer > 0: return base

        if integer == 0: return ECPoint(self.ec, infinity=True)
        if integer == 1: return self

        my_int = integer
        result = ECPoint(self.ec, infinity=True) 

        """
        result = 1
        while exp > 0:
        
            #check the last bit
            if exp % 2 : #exp is odd
                result = (result * base) % n
            #forget the last bit
            exp = exp >> 1
            base = (base * base) % n
        
        return result
        """
        #Most Significant Bit to Least Significand Bit 
        bits = [int(x) for x in '{:0100b}'.format(integer).lstrip('0')]

        for bit in bits:
            result = result + result #double
            if bit:
                result = result + self    #add
        
        return result
            


if __name__ == "__main__":
    my_ec = EllipticCurve(17, a = 2, b = 2)

    my_infinity_point = ECPoint(my_ec, infinity=True)
    my_ecpoint = ECPoint(my_ec, x =5, y = 1)
    check_validity(my_infinity_point)
    check_validity(my_ecpoint)
    print(my_infinity_point)
    print(my_ecpoint)

    
    
    print("Testing addition")
    my_2ecpoint = my_ecpoint + my_ecpoint
    print("+infinity_point:", my_ecpoint + my_infinity_point)
    print(my_2ecpoint)
    print(my_ecpoint + my_2ecpoint)
    print(my_2ecpoint +my_ecpoint)
    print("inverse:", my_ecpoint.inverse())
    print("+inverse", my_ecpoint + my_ecpoint.inverse())

    
    test_point = my_infinity_point
    for i in range(10):
        test_point += my_ecpoint
        print("sum iteration", str(i).zfill(2),test_point)

    print("Testing multiplication")

    my_new_point = 3*my_2ecpoint
    print(my_new_point)


    test_point = my_infinity_point
    for i in range(20):
        test_point = i*my_ecpoint
        print("mul iteration", str(i).zfill(2),test_point)
