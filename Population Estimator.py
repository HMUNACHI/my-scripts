cp = int(input("What is the current population: "))
yr = int(input("How many years from now: "))
n = yr

while yr >= 1:
    cp = cp + (cp * 0.003)
    yr = yr - 1

print("Your estimated population in ", n)
print(" years time would be ", cp)

input("Press ENTER to exit")
