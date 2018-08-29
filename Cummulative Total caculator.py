# A program to calculate the Cummulative total of a number

threshold = int(input("Enter the number you want to add cumulatively: "))
total = 0
count = 0

while count <= threshold:
    total = total + count
    count = count + 1

print ("Your total is ")
print (total)

input('Press ENTER to exit')
