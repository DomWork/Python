# While loop examples
# When a while loop rather than a for loop:
# You tend to use a while loop, rather than for a fixed number of loops, 
# instead for a permanent loop that continues while a contition is true.
# So you should make sure the condition is able to be met or it goes on for ever.
counter = 65
while counter < 91:
    print(str(counter) + "=" + chr(counter))
    counter += 1
print("All Done")

#You can use if-continue in while loops just like in for loops
import random
print("Odd Numbers")
counter = 0
counter2 = 0 #Count the total number of iterations including the failed "even" ones
while counter < 10:
    counter2 +=1
    number = random.randint(1,999) #Get a random number
    if int(number / 2) == number / 2:
        continue #If it is an even number don't print it, just carry on
    print(number) # but because of above, it will only print if odd number
    counter +=1
print("Loop is done after", counter2, "loops") #To get 10 odd numbers required this number of iterations
