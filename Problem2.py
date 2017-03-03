import random
H = 1000
L = 1
guess = random.randint(L,H)
print(guess)
answer = raw_input("write 'lower' for lower number or 'bigger' for bigger number. \n type correct if it is the number.")

while(answer != "correct"):
	if(answer == "lower"):
		H = guess - 1
		guess = random.randint(L, H)
		print(guess)
		answer = raw_input("write 'lower' for lower number or 'bigger' for bigger number. \n type correct if it is the number.")
		
	if(answer == "bigger"):
		L = guess + 1
		guess = random.randint(L , H)
		print(guess)
		answer = raw_input("write 'lower' for lower number or 'bigger' for bigger number. \n type correct if it is the number.")
		

if(answer == "correct"):
	print("I am correct!")			