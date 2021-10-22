st = input("Enter the string: ").lower()

vow = dg = ws = cos = 0

for i in st:
	if i in 'aeiou':
		vow += 1
	elif i.isalpha():
		cos += 1
	elif i.isdigit():
		dg += 1
	elif i in ' \t\n':
		ws += 1
print("vowels : ",vow)
print("consonents : ",cos)
print("digits : ",dg)
print("word space : ",ws)
	
