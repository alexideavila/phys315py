numb = int(input("Please enter an integer number: "))
numb2 = numb
print("If I add your number by one 10 times I get:")

x=11
while x!=0:
	print(numb2, end=' ')
	numb2 += 1
	x -= 1 

print()
print("If I show the squares:")

numb3=numb
sqsum=0
y=11
while y!=0:
	print(numb3, end='^2 ')
	sqsum += numb3**2
	numb3 += 1
	y -= 1

print()
print("The sum of those squares are:", sqsum)

