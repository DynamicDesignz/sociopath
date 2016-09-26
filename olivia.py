def poly_order(coeffs):
    if len(coeffs)>0:
        return len(coeffs)-1
    else:
         return 0

def poly_coefficient(coeffs, i):
    if i>len(coeffs) -1:
        return 0
    return coeffs[i]

def poly_evaluate(coeffs, value):
    final = 0
    for x in range(0, len(coeffs)):
        final = final + (value**x)
    return final

def poly_add(coeffs1, coeffs2):
    coeffs = []
    for x in range(0, len(coeffs1)):
        if x < len(coeffs2):
            coeffs.append(coeffs1[x]+coeffs2[x])
        else:
            coeffs.append(coeffs1[x])
    for x in coeffs2[len(coeffs):]:
        coeffs.append(x)
    return coeffs

def poly_mul(coeffs1, coeffs2):
    coeffs = []
    for x in range(0,len(coeffs1)):
        for y in range(0, len(coeffs2)):
            while (x+y) > len(coeffs) -1:
                coeffs.append(0)
            coeffs[(x+y)] = coeffs[(x+y)] + (coeffs1[x]*coeffs2[y])
    return coeffs

def main():
    coeffs = [1,2,3,4,5]
    print(poly_order(coeffs))
    print(poly_coefficient(coeffs, 3))
    print(poly_evaluate(coeffs, 1))
    print(poly_add(coeffs,[1,2,3,4,5,6,7,8,9]))
    print(poly_add(coeffs,[1,2,3]))
    print(poly_mul([1,1,1,1], [1,2]))

if __name__ == "__main__":
    main()