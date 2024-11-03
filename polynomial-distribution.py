#Polynomial Distribution List

class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

def createNode(coefficient, exponent):
    return Node(coefficient, exponent)

def addTerm(poly, coefficient, exponent):
    if poly is None:
        return createNode(coefficient, exponent)
    else:
        temp = poly
        while temp.next is not None:
            temp = temp.next
        temp.next = createNode(coefficient, exponent)
        return poly

def sortPolynomial(poly):
    if poly is None or poly.next is None:
        return poly
    sorted_poly = poly
    current = poly.next
    sorted_poly.next = None
    while current is not None:
        temp = current
        current = current.next
        if temp.exponent > sorted_poly.exponent:
            temp.next = sorted_poly
            sorted_poly = temp
        else:
            scan = sorted_poly
            while scan.next is not None and scan.next.exponent > temp.exponent:
                scan = scan.next
            temp.next = scan.next
            scan.next = temp
    return sorted_poly

def addPolynomials(poly1, poly2):
    result = None
    while poly1 is not None and poly2 is not None:
        if poly1.exponent > poly2.exponent:
            result = addTerm(result, poly1.coefficient, poly1.exponent)
            poly1 = poly1.next
        elif poly1.exponent < poly2.exponent:
            result = addTerm(result, poly2.coefficient, poly2.exponent)
            poly2 = poly2.next
        else:
            result = addTerm(result, poly1.coefficient + poly2.coefficient, poly1.exponent)
            poly1 = poly1.next
            poly2 = poly2.next
    while poly1 is not None:
        result = addTerm(result, poly1.coefficient, poly1.exponent)
        poly1 = poly1.next
    while poly2 is not None:
        result = addTerm(result, poly2.coefficient, poly2.exponent)
        poly2 = poly2.next
    return sortPolynomial(result)

def displayPolynomial(poly):
    while poly is not None:
        print(f"{poly.coefficient}x^{poly.exponent}", end=" ")
        poly = poly.next
        if poly is not None:
            print("+", end=" ")
    print()

poly1 = None
poly2 = None
result = None

poly1 = addTerm(poly1, 7, 3)
poly1 = addTerm(poly1, 9, 2)
poly1 = addTerm(poly1, 12, 1)
poly1 = sortPolynomial(poly1)

poly2 = addTerm(poly2, 9, 2)
poly2 = addTerm(poly2, 4, 1)
poly2 = addTerm(poly2, 7, 0)
poly2 = sortPolynomial(poly2)

displayPolynomial(poly1)
displayPolynomial(poly2)

result = addPolynomials(poly1, poly2)

displayPolynomial(result)
