import sys


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('Format like this: python conASCII2Char.py "97, 101, 100"')
		sys.exit()
	str_input = sys.argv[1]
	char_set = str_input.split(',')
	str_output = ""
	for char_unit in char_set:
		try:
			char_code = int(char_unit)
			str_output += chr(char_code)
		except Exception as e:
			print("Input Error: ")
			print('Format like this: python conASCII2Char.py "97, 101, 100"')
			sys.exit()
	print("Result:")
	print(str_output)