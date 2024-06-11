print("Entrer 3 nombres et le programme vérifiera si deux des trois sont égaux.")

def deux_egaux(a, b, c):
    if a == b or b == c or c == a:
        return True
    else:
        return False

x = int(input())
y = int(input())
z = int(input())

if deux_egaux(x, y, z) == True:
    print("True")
else:
    print("False")