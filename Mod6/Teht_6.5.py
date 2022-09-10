
# funktio poistaa listasta parittomat luvut
def remove_odd(a):
    for i in a[:]:
        if i % 2 != 0:
            a.remove(i)
    return a

a = [2, 5, 7 ,8, 4]

# lopuksi molempien listojen tulostus

print(f"alkuperäinen lista: {a}")
print(f"lista ilman parittomia: {remove_odd(a)}")