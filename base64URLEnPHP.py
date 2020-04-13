import sys,base64,getopt
from urllib.parse import urlencode

def usage():
	print(
	"""
		Usage:sys.args[0] [option]
			-h or --help：Show help info
			-f or --file：path_file   ex. python base64URLEnPHP.py -f 'C:\\users\\a\\Desktop\\1.php'
			-s or --str： string      ex. python base64URLEnPHP.py -s 'aaaaaaaaaaaaaaaaaaaaaaaa'
	"""
	)

def stripFile(oldFile):
	str_out = ""
	f = open(oldFile, 'r+')
	for eachline in f.readlines():
		eachline = eachline.strip()
		if eachline[:1] == "#" or eachline[:2] == "//":
			continue
		newStr = eachline.replace("\t"," ").strip() 
		str_out += newStr
	f.close()
	str_out = str_out.strip('<?php').strip('?>')
	return str_out

if __name__ == "__main__":
	
	if len(sys.argv) == 1:
		usage()
		sys.exit()
		
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hf:s:", ["help"])
	except getopt.GetoptError:
		print("argv error,please input")
	#if len(sys.argv) != 2:
	#	print('Format like this: python base64URLEnPHP.py php_file')
	#	sys.exit()
	#file_input = sys.argv[1]
	#file_input = "C:\\phpstudy_pro\\WWW\\1.php"
	for cmd, arg in opts:
		if cmd in ("-h", "--help"):
			print("help info")
			sys.exit()
		elif cmd in ("-f", "--file"):
			file_input = arg
			str_php = stripFile(file_input)
		elif cmd in ("-s", "--str"):
			str_php = arg
	
	print("Result:")
	print(str_php)

	str_base64 = str(base64.b64encode(str_php.encode("utf-8")), "utf-8")
	print("Base64:")
	print(str_base64)
	
	values={}
	values['output']=str_base64
	str_urlen = urlencode(values)
	print("Urlencode:")
	print(str_urlen)