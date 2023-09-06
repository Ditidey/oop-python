
def make_upper(up):
    up_make = up.upper()
    return up_make

def make_capital(cap):
    cap_make = cap.capitalize()
    return cap_make

def make_lower(low):
    low_make = low.lower()
    return low_make

def test_script():
    up = 'diti rani'
    U_m = make_upper(up)
    print(U_m)

    low = 'Diti RANI'
    L_m = make_lower(low)
    print(L_m)

    ca = 'diti rani'
    C_m = make_capital(ca)
    print(C_m)

test_script()