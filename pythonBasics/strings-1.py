string = "The quick brown fox jumps over to the lazy dog. Tit for Tat."

print ("string = " + string )
print ("\n")

print ("string[0] = " + string[0])
print ("string[5] = " + string[5])
print ("string[2:5] = " + string[2:7])
print ("\n")

print ( "len(string)= ", end=""), print (len(string))
print ( "string.upper() = " + string.upper())
print ( "string.lower() = " + string.lower())
print ( "strint.relpace('i','I') = " + string.replace('i', 'I'))
print ( "strint.relpace('the','THE') = " + string.replace('the', 'THE'))
print ("\n")

print ( "string.split(\"t\") = ", end = ""), print ( string.split("t"))
print ( "string.split(\' \') = ", end = ""), print ( string.split(' '))
print ("\n")
