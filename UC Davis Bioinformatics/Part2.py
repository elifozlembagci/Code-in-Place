gene_id = "BRCA2"
print("Gene ID is: ", gene_id)
hw = "HELLO!!! WORLD!!!"
print(hw)

tmpstr = "hello my name is Nik."

allcaps = tmpstr.upper()
print("tmpstr in all caps: ", allcaps)

newstr = tmpstr.replace("Nik","Joe")
print("After replacing Nik with Joe")
print(newstr)

# This is a comment. Comments are lines that being with a hashtag symbol.
# They are ignored by the python interpreter and are used to document your code.

# you can also use the + symbol to concatenate strings
tmpstr2 = "How are you doing?"
print(tmpstr + " " + tmpstr2)

# you can find the position of one string in another
# returns -1 if not found
print("Position of 'you' in tmpstr2")
print(tmpstr2.find("you"))
print("Position of 'california' in tmpstr2")
print(tmpstr2.find("california"))





print("\nBooleans\n")

control = False
treatment = True
print("Value of control: ", control)
print("Value of treatment: ", treatment)




print("The data type of the variable 'control' is:", type(control))
print("The data type of the variable 'hw' is:", type(hw))
print("The data type of the variable 'gene_id' is:", type(gene_id))


#Text Type: str
#Numeric Types: int, float, complex
#Sequence Types: list, tuple, range
#Mapping Type: dict
#Set Types: set, frozenset
#Binary Types: bytes, bytearray, memoryview
#Boolean Type: bool

