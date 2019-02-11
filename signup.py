class signup:
		"""docstring for login"""
		def __init__(self):
			g=input("email=")
			y=input("you name=")
			h=input("password=")
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