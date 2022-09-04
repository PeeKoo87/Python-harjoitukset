gender = input("sukupuoli (nainen/mies)?" )
hg_value = int(input("hemoglobiinisi (g/l)?"))

if gender == "nainen":
    if hg_value < 117:
        print("hemoglobiiniarvo on alhainen.")
    elif hg_value <= 175:
        print("hg-arvo normaali.")

    else:
        print("hemoglobiiniarvo on korkea" )

elif gender == "mies":

    if hg_value < 134:
        print("hemoglobiiniarvo on alhainen")

    elif hg_value <= 195:
        print("hemoglobiiniarvo on normaali")
    else:
        print("hemoglobiiniarvo on korkea")

else:
    print("virheellinen arvo")
