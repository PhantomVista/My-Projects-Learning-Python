# Conditional Structures

x = 7
if x < 2:
    print("small")
elif x < 10:
    print("Medium")
else:
    print("LARGE")
print('All Done!')

# Try and Except

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = 1

print('First, istr')

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', astr)

# Users input for Try/Except

rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice Work")
else:
    print('Not a number')
