#a = input("Enter the string: ")
#b = input("Enter the character: ")
#c = 0
#for i in a:
#	if i == b:
#	   c = c + 1
#print(c)


#a = input("Enter the string: ")
#for i in a:
#	print(i, a.count(i))


a = input("Enter the string: ")
res = ''
for i in a:
	if i not in res:
		print(i, a.count(i))
		res += i
