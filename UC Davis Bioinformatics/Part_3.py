print("\nIF Statements\n")


print("\nIF Statement 1\n")
diffexp = 67
if (diffexp > 0):
    print("Upregulated")
else:
    print("Downregulated")

print("\nIF Statement 2\n")
diffexp = -9
if (diffexp > 0):
    print("Upregulated")
else:
    print("Downregulated")

print("\nIF Statement 3\n")
# An if statement doesn't need an else
if (diffexp < 0):
    print("Downregulated")

print("\nIF Statement 4\n")
# If statements can have multiple elif (else if)
# Try changing the value of diffexp to see how the output changes.
# The if statement below has a logical error, see if you can find it.
diffexp = 25
if (diffexp > 50):
    print("Very Upregulated")
elif (diffexp > 0):
    print("Upregulated")
elif (diffexp < 0):
    print("Downregulated")
elif (diffexp < -50):
    print("Very Downregulated")


###### BU KISMI BİL #####

print("\nIF Statement 5\n")
# You can use "and", "or", & "not" to write more complex conditions
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")


###### BU KISMI BİL #####

print("\nIF Statement 6\n")
if (diffexp < -50 or diffexp > 50):
    print("High Down or Up regulation")



print("\nIF Statement 7\n")
# The body of an if statement can have multiple lines of code
diffexp=25
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")
    print("Check the significance")

print("\nIF Statement 8\n")
# You can have nested if statements
sig = 0.049
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")

    if (sig < 0.05):
        print("It's significant!")






print("\nFor Loops\n")

# The range(n) function returns values from 0 to n-1
for i in range(5):
    print(i)



gene_list = ["DDX11L1","WASH7P","MIR6859-1","MIR1302-2HG","MIR1302-2","FAM138A"]

print("\nIterating through a list\n")

for id in gene_list:
    print(id + " is a gene of interest")






gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

print("\nIterating through a dictionary\n")

for gene in gene_exp_dict.keys():
    print("Gene", gene, "has expression value:", gene_exp_dict[gene])








print("\nWhile Loops\n")

n = 1
fact = 1
while (n < 8):
    fact = fact * n
    n += 1
print(fact)





gene_list = ["DDX11L1","WASH7P","MIR6859-1","MIR1302-2HG","MIR1302-2","FAM138A"]


print("\nBreak\n")

for id in gene_list:
    print(id + " is a gene of interest")
    if (id == "MIR1302-2HG"):
        break

print("\nContinue\n")

for id in gene_list:
    if (id == "MIR1302-2HG"):
        continue

    print(id + " is a gene of interest")




# imports are used to be able to use code from other libraries
import math

print("\nFunctions\n")

print("\nFunction 1\n")
# Functions can have zero parameters and return nothing
def hello():
    print("Hello, World!")

hello()

print("\nFunction 2\n")
# Or they can have multiple parameters and return something
def logfc(exp1,exp2):
    retval = math.log(exp2/exp1)
    return(retval)

gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

de = logfc(gene_exp_dict['WASH7P'], gene_exp_dict['FAM138A'])
print("The DE value is", de)

print("\nFunction 3\n")

# They can also have default values for any of the parameters
def logfc(exp1,exp2,sigdig=3):
    retval = math.log(exp2/exp1)
    retval = round(retval, sigdig)
    return(retval)

print(logfc(89,12,5))
print(logfc(89,12))