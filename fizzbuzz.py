
ask=float(input("Enter a number:"))

if(ask%3==0 and ask%5==0):
	print('FIZZBUZZ')
elif(ask%3==0):
	print('FIZZ')
elif(ask%5==0):
	print('BUZZ')
else:
	print('invalid')