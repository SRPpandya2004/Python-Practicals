"""" 3 WAP to find roots of quadratic equations if roots are real.________________________________
#_________________________Dout_____________________________________________________________"""

import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        return (root,)
    else:
        # If discriminant is negative, roots are not real
        return "No real roots"

# Example usage
a = 1
b = -3
c = 2

roots = find_roots(a, b, c)
if isinstance(roots, tuple):
    if len(roots) == 2:
        print(f"The roots are real and distinct: {roots[0]} and {roots[1]}")
    else:
        print(f"The root is real and repeated: {roots[0]}")
else:
    print(roots)