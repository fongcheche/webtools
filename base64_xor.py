import base64

#Decode
base64_xored = 'Oz4rPj0+LDovPiwsKDAtOw=='
xored = base64.b64decode(base64_xored)
plain = ''.join([chr(ord(c)^ord('_')) for c in xored])
print plain
#Encode
enocoded = base64.b64encode(''.join([chr(ord(c)^ord('_')) for c in plain]))
print enocoded
print "Complete!"