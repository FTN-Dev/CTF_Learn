from Cryptodome.Util.number import *

longNumbers = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
ntahlah = b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'

print("Ini adalah hasil dari long integers to bytes: ",long_to_bytes(longNumbers))
print("Ini adalah hasil dari bytes to long integers: ",bytes_to_long(ntahlah))