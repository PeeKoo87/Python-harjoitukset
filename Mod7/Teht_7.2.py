# listan testaus
def check_duplicates(name):
    if nameInput in name:
        return True
    else:
        return False
# pääkoodi etc.
nameInput = input("anna nimi: ")

name = set()
while nameInput != "":
    name.add(nameInput)
    nameInput = input("anna nimi: ")

    if check_duplicates(name) == True:
         print("nimi syötetty jo aiemmin!")

    if check_duplicates(name) == False:
            print("uusi nimi lisätty!")


# tulostus
for n in name:
    print(n)
