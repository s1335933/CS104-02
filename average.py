#Average.py
#Aidan Moxham

average, howManyEntered, total = 0,0,0
howMany = int(input("How many test scores would you like to average? "))

while howManyEntered < howMany:
    testscore = float(input("Enter test score: "))
    total = total + testscore
    howManyEntered+=1

average = total/howMany

print("The average for the test scores you entered is: ", average )

