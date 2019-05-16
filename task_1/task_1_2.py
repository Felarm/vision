import json


def find_fifth(st):
	output = 'nah'
	pos = st.find('.')
	print(pos)
	if pos != -1:
		output = st[:pos + 6]
		print(output)
	return output


json1 = json.loads('{"arr": [1.1234567, 12.1234567, 123.1234567], "dict": {"a": 1234.1234561, "b": 1234.1234562}}',
				   parse_float=find_fifth)
json2 = json.loads('{"arr": [1.1234567, 12.1234567, 123.1234567], "dict": {"a": 1234.1234561, "b": 1234.1234562}}',
				   parse_float=find_fifth)

print(json1)
print(json2)

print(json1 == json2)