# Assignment 2 Question 1
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

# Prompt for positive integer (includes 0)
# negative integer will stop program

#prints output of Maximum, Minimum and Average
def print_output(maxNum, minNum, avgNum):
    print("{0:>3}{1:>4}{2:>8}\n".format(maxNum,minNum,avgNum))

#calculates current average
def calulate_average(currentTotal, count):
    averageNum = currentTotal/count
    return averageNum

# check if user input number is bigger than maximum number
# if true, maximum will now be user input
# if false, maximum will remain the same
def check_maximum(currentNum, maximumNum):
    if (currentNum > maximumNum):
        maximumNum = currentNum
    else: 
        maximumNum = maximum
    return maximumNum

# check if user input number is smaller than minimum number
# if true, minimum will now be user input
# if false, minimum will remain the same
def check_minimum(currentNum, minimumNum):
    if (currentNum < minimum):
        minimumNum = currentNum
    else: 
        minimumNum = minimum
    return minimumNum

# Counts the number of times loop is run
count = 0

while True:
    number = int(input("Enter an integer:"))
     # When negative number is entered, program stops
    if (number < 0):
        break
    
    # Print header
    print("\nMax Min Average")
    
    count = count + 1
    
    # First time run
    if (count == 1):
        maximum = number
        minimum = number
        total = number
        average = calulate_average(total, count)
        print_output(maximum,minimum,int(average))
        
    else:
        maximum = check_maximum(number, maximum)
        minimum = check_minimum(number, minimum)
        total = total + number
        average = calulate_average(total, count)
        print_output(maximum, minimum, average)
        
# Print output when program stops    
print("\nProgram ends",end="")
