# Python3 code to demonstrate yield keyword

# Use of yield
def printresult(String) :
	for i in String:
		if i == "e":
			yield i

# initializing string
String = "GeeksforGeeks"
ans = 0
print ("The number of 'e' in word is : ", end = "" )
String = String.strip()

for j in printresult(String):
	ans = ans + 1

print (ans)
