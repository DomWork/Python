#You tend to use for loops for a fixed number of loops, unless a condition breaks you out.
# Most basic for loop using a range from zero to [one less than] the number stated
print("")
print("Basic numerical for loop - range of 10:")
for x in range(10):
    print(x)
# To go from a specific number to another number, specify both numbers in the range
print("")
print("Specifying specific number ranges to loop in for loop - range from 3 to 12:")
for x in range(3, 12):
    print(x)
# You can loop a for loop through characters in a string
print("")
print ("For loop scans through a string one character at a time:")
for x in "snorkel":
    print(x)
# You can loop through lists of strings too
print("")
print ("For loop scanning through items in a list:")
for x in ["The", "rain", "in", "Spain"]:
    print(x)
# Put the list into a list variable and do the same thing
print("")
print ("For loop scanning through items in a list variable:")
seven_dwarves = ["Aa", "Bb", "Cd", "Dd", "Ee", "Ff", "Gg"]
for a in seven_dwarves:
    print(a)
# Ok now for something more complex
# Putting a break into a for loop if a condition is met, to break out of the loop early
print("")
print("Breaking out of a for loop if some condition is met:")
seven_dwarves = ["Aa", "Bb", "Cd", "Dd", "", "Ff", "Gg"]
for a in seven_dwarves:
    if a == "":
        print("Blank entry in list, so BREAK command activated and early termination of for loop.")
        break
    print(a)
# Conversely this one continues with the loop, breaking out of just one iteration if a condition is met
print("")
print("Continuing past an iteration of the for loop if some condition is met:")
seven_dwarves = ["Aa", "Bb", "Cd", "Dd", "", "Ff", "Gg"]
for a in seven_dwarves:
    if a == "":
        print("Blank entry in list, so CONTINUE command jumps back to the next iteration instead.")
        continue
    print(a)
print("")
print("Nesting loops in loops:")
for outer in ["First", "Second", "Third"]:
    print(outer)
    for inner in range(3):
        print(inner)
print("")
