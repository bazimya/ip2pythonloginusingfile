from login import login
from signup import signup
print("please user select one you want her 'c' stand for create while 's' stands for sigin")
p=input("type her ")
c="c"
s="s"
if (p==str(c)):
	sig=signup()
elif(p==str(s)):
 	log=login()
else:
	print("you lost close and start")
