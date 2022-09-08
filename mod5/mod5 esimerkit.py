
nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
# tulostaa listan, jossa osa arvoista
print(nimet[1:3])
print(nimet[1:4])
# tulostaa yhden alkion arvon
print(nimet[1])
print(nimet[2])
print(nimet[3])


numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
#listan pituus eli koko
print(len(numbers))
#viimeisen alkion indeksi: pituus -1
print(numbers[len(numbers)-1])
print(numbers [-1])
# print(number[6]) # out of range error

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]


userInput = input("anna uusi nimi: ")
nimet.insert(1, userInput) # lisätään uusi arvo index-kohtaan 1
nimet.append(userInput)


#listan kaikkien arvojen tulstus
for nimi in nimet:
    print(nimi)
nimet.remove(userInput) # poistetaan käyttäjän lisäämä nimi listalta

# sama iteraattoria i käyttäen
for i in range, (len(nimet)):
    print(f"{i+1}.{nimet[i]}")

# Tulostaa kolmella jaolliset luvut välillä 0-1000
#for i in range(0, 1001, 3):
 #   print(i)

#for i in range(0, 101):
    #if i % 3 == 0:
        #print(i)

letters = ["a", "n"]
letters2 = letters[0:len(letters)]
letters2.reverse()
letters.extend(letters2)
print(letters)
word = ""
for letter in letters:
    word = word + letter
print(word)