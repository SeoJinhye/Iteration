import random
secret = int(input("wirte the number"))
H = 1000
L = 1
guess = random.randint(L,H)

while(secret != guess):
	print(guess)
	answer = raw_input("")
	if(answer == "lower"):
		H = guess - 1
		guess = random.randint(L, H)
	if(answer == "bigger"):
		L = guess + 1
		guess = random.randint(L , H)	
print(guess)		
print("You are correct! You won!")