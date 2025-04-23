# arithemetic operators
a =10
b = 20
c = 350

print(f"{a}")
print(f"{a-b}")
print(f"{a} // {b} = {a // b}") 
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}") 

# assignment operators

x = 5
print("Initial x:", x) # 5
x += 2
print("x += 2:", x) # 7
x *= 3
print("x *= 3:", x) # 21
x -= 4
print("x -= 4:", x) # 17
y = x / 2
print("x /= 2:", y, "\n") 

# computational operatorns

print(f"{a} == {b} →", a == b) # False
print(f"{a} != {b} →", a != b) # True
print(f"{a} > {b} →", a > b) # False
print(f"{a} < {b} →", a < b)# True
print(f"{a} >= {b} →", a >= b) # False
print(f"{a} <= {b} →", a <= b, "\n")  # True

# logical operators'
has_access = True
is_admin = False

print("has_access and is_admin →", has_access and is_admin) 
# true and false output is false
print("has_access or is_admin →", has_access or is_admin)
# true or false output is true
print("not has_access →", not has_access)
# not true output false
print("not is_admin →", not is_admin, "\n")
# not false output true

# operator presidence 
result = 3 + 4 * 2 ** 2
print("3 + 4 * 2 ** 2 =", result)  # 4**2 = 16; 4*4 = 16; 3 + 16 = 19 # PEMDAS # BODMAS