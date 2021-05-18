num1=int(input('Enter 1st number : '))
num2=int(input('Enter 2nd number : '))
mul=num1*num2
for i in range(1,mul+1) :
	if i%num1==0 and i%num2==0 :
		lcm=i
		print(f"The LCM of these two numbers is {lcm}")
		break