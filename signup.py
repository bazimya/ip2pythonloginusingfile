import random
class signup:
		"""docstring for login"""
		def __init__(self):
			g=input("email=")
			y=input("you name=")
			print("do you want to create you password if yes type 'yes' if you want to be genelated by system typ 'NO'")
			checking=input("choose")
			yes="yes"
			no="NO"
			if (checking==yes):
				h=input("password=")
			else:
				h = str(random.randint(12345,123456789))
				print(h)
			
			print("your account created success full")

			insert=open("email.txt","w")
			insert.write(g)
			insert.close()

			paa=open("password.txt","w")
			paa.write(h)
			# insert.write(h)
			paa.close()
			addres=open("address.txt","w")
			addres.write(y)
			addres.close()