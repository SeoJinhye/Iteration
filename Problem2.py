import random
secret = int(input("wirte the number"))
guess = random.randint(1,1000)
while(secret != guess):
	print(guess)
	answer = raw_input("")
	if(answer == "big"):
		#print(guess)
		guess = random.randint(1,guess)
	if(answer == "small"):
		#print(guess)
		guess = random.randint(guess,1000)
print("You are correct! You won!")
	