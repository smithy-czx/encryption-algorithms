  
def egcd(a, b):
    #finding x and y in the equation 'ax + by = gcd'
    if a == 0:
        return (b, 0, 1)
    
    old_coefficient_a, old_coefficient_b = 1, 0
    current_coeffient_a, current_coeffient_b = 0, 1


    while b != 0:
        division_result = a // b
        remainder = a % b
        a = b
        b = remainder

        coefficient_a = old_coefficient_a - (division_result * current_coeffient_a)
        coefficient_b = old_coefficient_b - (division_result * current_coeffient_b) # Updating each of the coefficients


        old_coefficient_a = current_coeffient_a
        old_coefficient_b = current_coeffient_b
        current_coeffient_a = coefficient_a 
        current_coeffient_b = coefficient_b

    #represent the linear equation 'ax + by = gcd'
    x = old_coefficient_a
    y = old_coefficient_b
    return (a, x, y)


def modinv(a, m):
    gcd, coefficient_a, coefficient_b = egcd(a, m)
    if gcd != 1:
        return 'No modular inverse'
    return coefficient_a%m

