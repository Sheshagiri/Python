def main():
	print("########################")
	print("#######CALCUTATOR#######")
	print("########################")
	print("Enter an opration(+,-,/,*)")
	operation = raw_input()
	if(operation != '+' and operation != '-' and operation != '/' and operation != '*'):
		print("you have choseen invalid option!")
	else:
		n1 = int(raw_input("Enter number 1:"))
		n2 = int(raw_input("Enter number 2:"))
		if(operation == '+'):
			print(add(n1,n2))
		elif(operation == '-'):
			print(substract(n1,n2))
		elif(operation == '/'):
			print(divide(n1,n2))
		else:
			print(multiply(n1,n2))
def add(n1,n2):
	return n1 + n2
def substract(n1,n2):
	return n1 - n2
def divide(n1,n2):
	return n1 / n2
def multiply(n1,n2):
	return n1 * n2

main()
