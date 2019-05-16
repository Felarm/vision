import json


def find_fifth(st):
	output = 'nah'
	pos = st.find('.')
	print(pos)
	if pos != -1:
		#if len(st[:pos + 5]) > 10:
		output = st[:pos + 6]
		print(output)
	return output


x = '123.123456673'
y = '123.12345789'
print(find_fifth(x)==find_fifth(y))
print(find_fifth('123.1234512345678901209234750918423429875'))