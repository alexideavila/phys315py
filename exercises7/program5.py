number =int(input("Please enter a number: "))
number2=number
print("If I increase your number by one I get: ")
for i in range(10):
	print(number2, end=' ')
	number2 += 1

number3=number
sqsum=0
print()
print("And squares of those numbers are: ")
for j in range(10):
	print(number3, end="^2 ")
	sqsum += number3**2
	number3 += 1

print()
print("The sum of those numbers are: ", sqsum)

